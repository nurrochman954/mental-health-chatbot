# Mental Health Support Chatbot

Chatbot berbasis aturan (rule-based) untuk dukungan kesehatan mental, menggunakan teknik-teknik dari buku *Feeling Good Together* oleh Dr. David D. Burns.

## Latar Belakang Singkat

Proyek ini terinspirasi dari buku *Feeling Good Together* oleh Dr. David D. Burns, yang menekankan bahwa banyak masalah hubungan berakar pada kurangnya keterampilan komunikasi, bukan kurangnya cinta.  

Berdasarkan prinsip Terapi Perilaku Kognitif (CBT), chatbot ini dibangun dengan filosofi inti:

**"Empati di Atas Segalanya."**

Chatbot ini dibuat sebagai latihan praktis sederhana untuk menerapkan prinsip komunikasi dari buku Feeling Good Together. Tujuannya adalah mengeksplorasi bagaimana validasi emosi dan pertanyaan reflektif dapat bekerja dalam suatu interaksi meskipun bot ini masih terbatas dan belum mampu memberikan solusi instan atau refleksi mendalam. Proyek ini berfokus pada pembelajaran dan eksperimen, sehingga interaksi yang dihasilkan lebih bersifat simulasi daripada terapi nyata.

## Konfigurasi & Menjalankan

### 1. Persiapan Awal

Pastikan Anda memiliki **Python 3.9** atau yang lebih baru.

- Clone repositori ini
   ```
   git clone https://github.com/nurrochman954/mental-health-chatbot.git
   cd mental-health-chatbot
   ```
   
- Buat dan aktifkan virtual environment (disarankan)  
    ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

- Install dependensi  
    ```bash
    pip install -r requirements.txt
    ```

### 2. Konfigurasi .env

- Salin `.env.example` menjadi `.env` lalu isi `DISCORD_TOKEN=your_discord_bot_token_here` (ganti dengan token Discord Anda)

- Untuk menjalankan Discord Bot:
  1. Buat aplikasi bot baru di [Discord Developer Portal](https://discord.com/developers/applications).
  2. Klik **New Application** → beri nama → buat **Bot**
  3. Salin **Bot Token** dari tab *Bot*. Token ini yang dipakai di kode Python Anda (DISCORD_TOKEN=...) dan masukkan ke dalam `.env`.
  4. Undang bot ke server Anda menggunakan URL OAuth2 yang dihasilkan.

### 3. Menjalankan Bot

Bot dapat dijalankan dalam dua mode:

- Mode CLI (Terminal):  
    ```bash
    python main.py
    ```

- Mode Discord Bot:  
    ```bash
    python main.py discord
    ```

Di Discord, Anda bisa memulai percakapan dengan mengirim *Direct Message (DM)* ke bot.  

**Balasan**: Jika bot diaktifkan melalui *Direct Message*, ia akan mengirim pesan konfirmasi bahwa bot sudah siap membantu.

### 4. Pengujian

Kualitas dan keandalan bot dapat diuji melalui unit testing.

- Menjalankan unit tests:  
    ```bash
    python -m unittest discover -v tests
    ```

**Cakupan Pengujian**:
- Validasi Empati: Memastikan bot selalu memvalidasi emosi pengguna terlebih dahulu.  
- Manajemen Konteks: Menguji kemampuan bot untuk tidak mengulangi pertanyaan.  
- Refleksi Proaktif: Memverifikasi bot beralih ke mode refleksi setelah ambang batas tercapai.  
- Pemahaman Sinyal Akhir: Menguji kemampuan bot mengenali frasa penutup.  
- Manajemen Memori: Memastikan bot tidak mengulang validasi untuk topik yang sama.  
- Alur Sesi Lengkap: Mensimulasikan percakapan dari awal hingga akhir untuk memastikan ringkasan berhasil dibuat.  

## Demo

Tampilan demo chatbot:

![Chatbot Demo](https://raw.githubusercontent.com/nurrochman954/mental-health-chatbot/c93692da3894dad7695bf0ced359ca29f8f8bf67/demo-chatbot.gif)