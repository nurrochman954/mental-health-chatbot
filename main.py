#!/usr/bin/env python3
"""
Mental Health Chatbot - Enhanced & Natural Version
Focus on genuine empathy and natural conversation
"""

import sys
import os

# Menambahkan src directory ke Python path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

def run_cli():
    """Menjalankan chatbot dalam mode CLI dengan pendekatan yang lebih natural."""
    
    try:
        from core.chatbot import MentalHealthChatbot
        
        print("="*60)
        print("MENTAL HEALTH SUPPORT CHATBOT")
        print("Versi Percakapan Natural Berbasis 'Feeling Good Together'")
        print("="*60)
        print("\nKetik 'selesai' atau 'stop' kapan saja untuk mengakhiri percakapan.")
        print()
        
        nama = input("Boleh aku tahu namamu? ").strip()
        if not nama:
            nama = "User"
        
        chatbot = MentalHealthChatbot(nama)
        
        # DITINGKATKAN: Sapaan pertama diambil langsung dari bot, bukan teks statis
        initial_response = chatbot.get_response(f"halo, nama saya {nama}")
        print(f"\nBot: {initial_response}\n")
        
        while True:
            try:
                user_input = input(f"{nama}: ").strip()
                
                if not user_input:
                    continue

                # DITINGKATKAN: Panggil bot dengan input 'selesai' untuk mendapatkan ringkasan
                if user_input.lower() in ['quit', 'exit', 'bye', 'keluar', 'selesai', 'stop']:
                    closing_response = chatbot.get_response('selesai')
                    print("\n" + "="*50)
                    print(f"Bot: {closing_response}")
                    print("="*50)
                    break
                
                response = chatbot.get_response(user_input)
                print(f"\nBot: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\nSampai jumpa, {nama}! Jaga diri baik-baik! 👋")
                break
            except Exception as e:
                print(f"\nOops, terjadi kesalahan: {e}")
                continue
                
    except ImportError as e:
        print(f"Import Error: {e}")
        print("Pastikan semua file inti ada di src/core/")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def run_discord():
    """Menjalankan Discord bot."""
    try:
        from integrations.discord_bot import main as discord_main
        import asyncio
        
        print("Starting Discord Bot...")
        print("Pastikan DISCORD_TOKEN sudah diatur di file .env\n")
        
        asyncio.run(discord_main())
        
    except ImportError as e:
        print(f"Import Error: {e}")
        print("Pastikan discord_bot.py ada di src/integrations/")
        sys.exit(1)
    except Exception as e:
        print(f"Discord Bot Error: {e}")
        sys.exit(1)

def show_help():
    """Menampilkan informasi bantuan."""
    print("="*60)
    print("MENTAL HEALTH SUPPORT CHATBOT - NATURAL VERSION")
    print("="*60)
    print("\nUSAGE:")
    print("  python main.py [mode]")
    print("\nMODES:")
    print("  cli      - Chat di terminal (default)")
    print("  discord  - Run as Discord bot")
    print("  help     - Show this help")
    print("\nEXAMPLES:")
    print("  python main.py")
    print("  python main.py discord")
    print("="*60)

def main():
    """Fungsi utama dengan UX yang lebih baik."""
    try:
        if len(sys.argv) > 1:
            mode = sys.argv[1].lower()
            if mode in ['help', '-h', '--help']:
                show_help()
            elif mode == 'discord':
                run_discord()
            elif mode == 'cli':
                run_cli()
            else:
                print(f"Mode tidak dikenal: {mode}")
                print("Mode yang valid: cli, discord, help")
                sys.exit(1)
        else:
            run_cli() # Default ke CLI
    except KeyboardInterrupt:
        print("\n\nSampai jumpa! 👋")
    except Exception as e:
        print(f"\nTerjadi error tak terduga: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
