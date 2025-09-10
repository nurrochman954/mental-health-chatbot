"""
Discord Bot Integration V3 - Seamless Experience
Ditingkatkan untuk integrasi yang lebih mulus dengan alur percakapan
dari chatbot.py dan menampilkan ringkasan dengan lebih baik.
"""

import discord
from discord.ext import commands
import asyncio
import logging
import os
import sys
from dotenv import load_dotenv

# Menambahkan parent directory ke path untuk import
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from core.chatbot import MentalHealthChatbot, ConversationStage

load_dotenv()

class MentalHealthBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix='!',
            intents=intents,
            description="Mental Health Support Bot - Berbasis 'Feeling Good Together'",
            help_command=None
        )
        
        self.chatbots: Dict[int, MentalHealthChatbot] = {} # Kunci: user_id, Value: instance chatbot
        self.logger = logging.getLogger(__name__)

    async def on_ready(self):
        """Dipanggil saat bot siap."""
        self.logger.info(f'{self.user} telah terhubung ke Discord!')
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="ceritamu | DM untuk privasi"
            )
        )
        
    async def on_message(self, message: discord.Message):
        """Menangani pesan masuk."""
        if message.author == self.user:
            return
        
        # Jika di DM, atau jika sesi sudah aktif, langsung tangani sebagai pesan chat.
        if isinstance(message.channel, discord.DMChannel) or message.author.id in self.chatbots:
            # Abaikan command lain jika sedang dalam sesi chat
            if message.content.startswith('!') and not message.content.lower().startswith(('!stop', '!selesai')):
                return
            await self.handle_chat_message(message)
            return
        
        await self.process_commands(message)

    async def handle_chat_message(self, message: discord.Message):
        """Menangani semua pesan dalam sesi chat yang aktif."""
        user_id = message.author.id
        
        # Mulai sesi baru secara otomatis jika belum ada (terutama di DM)
        if user_id not in self.chatbots:
            self.chatbots[user_id] = MentalHealthChatbot(message.author.display_name)
            # Dapatkan sapaan pertama dari bot
            response = self.chatbots[user_id].get_response(f"halo, nama saya {message.author.display_name}")
            await message.channel.send(response)
            return

        chatbot = self.chatbots[user_id]
        
        try:
            async with message.channel.typing():
                response = chatbot.get_response(message.content)

            # Jika respons adalah penutup, akhiri sesi
            if chatbot.stage == ConversationStage.CLOSING:
                embed = discord.Embed(
                    title=f"Refleksi Sesi untuk {message.author.display_name}",
                    description=response,
                    color=discord.Color.dark_green()
                )
                embed.set_footer(text="Sesi telah berakhir. Mulai lagi kapan saja dengan mengirim pesan baru.")
                await message.channel.send(embed=embed)
                del self.chatbots[user_id]
                return

            # Kirim respons normal
            if len(response) > 2000:
                parts = [response[i:i+1900] for i in range(0, len(response), 1900)]
                for part in parts:
                    await message.channel.send(part)
            else:
                await message.channel.send(response)

        except Exception as e:
            self.logger.error(f"Error saat memproses pesan: {e}")
            await message.channel.send("Maaf, terjadi kesalahan internal. Sesi akan dihentikan.")
            if user_id in self.chatbots:
                del self.chatbots[user_id]

    @commands.command(name='chat', help='Mulai sesi chat kesehatan mental di server channel.')
    async def start_chat(self, ctx: commands.Context):
        """Memulai sesi chat di channel server."""
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("Kamu sudah di DM. Langsung saja mulai bercerita, tidak perlu perintah `!chat`.")
            return

        if ctx.author.id in self.chatbots:
            await ctx.send(f"{ctx.author.mention}, kamu sudah memiliki sesi aktif. Lanjutkan percakapanmu atau ketik 'stop' untuk mengakhiri.")
            return

        # Langsung mulai sesi dan kirim sapaan pertama dari bot
        self.chatbots[ctx.author.id] = MentalHealthChatbot(ctx.author.display_name)
        initial_response = self.chatbots[ctx.author.id].get_response(f"halo, nama saya {ctx.author.display_name}")

        embed = discord.Embed(
            title="Sesi Chat Dimulai!",
            description=(
                f"Halo {ctx.author.mention}! Sesi chat pribadimu telah dimulai di channel ini.\n\n"
                "**Untuk privasi maksimal, sangat disarankan untuk melanjutkan percakapan ini melalui DM (Private Message) denganku.**"
            ),
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
        await ctx.send(initial_response)

    @commands.command(name='stop', aliases=['selesai'], help='Mengakhiri sesi chat kesehatan mental.')
    async def stop_chat(self, ctx: commands.Context):
        """Mengakhiri sesi chat secara eksplisit."""
        user_id = ctx.author.id
        if user_id not in self.chatbots:
            await ctx.send(f"{ctx.author.mention}, kamu tidak sedang dalam sesi chat aktif.")
            return
        
        chatbot = self.chatbots[user_id]
        closing_response = chatbot.get_response('selesai')
        
        embed = discord.Embed(
            title=f"Refleksi Sesi untuk {ctx.author.display_name}",
            description=closing_response,
            color=discord.Color.dark_green()
        )
        embed.set_footer(text="Sesi telah berakhir. Mulai lagi dengan `!chat` (di server) atau kirim pesan (di DM).")
        await ctx.send(embed=embed)
        del self.chatbots[user_id]

    # ... (fungsi help_mental, info, techniques, dll bisa tetap sama)

def setup_logging():
    """Mengatur konfigurasi logging."""
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/bot.log'),
            logging.StreamHandler()
        ]
    )

async def main():
    """Fungsi utama untuk menjalankan bot."""
    setup_logging()
    bot = MentalHealthBot()
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        logging.error("DISCORD_TOKEN tidak ditemukan di environment variables!")
        return
    
    try:
        await bot.start(token)
    except Exception as e:
        logging.error(f"Bot error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
