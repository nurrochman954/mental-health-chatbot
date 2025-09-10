# src/core/knowledge_base.py
"""
Knowledge Base V8 - The Relationship Expert (Final Version)
Diperkaya secara masif dengan konten hubungan, konflik, dan self-esteem.
Logika disempurnakan untuk mendukung alur percakapan yang natural.
"""

import random
from typing import List, Dict, Optional, Set

class KnowledgeBase:
    def __init__(self):
        # ... (five_secrets dan cognitive_distortions tetap sama seperti versi V8 sebelumnya) ...
        self.five_secrets = {
            'disarming': {
                'name': 'Teknik Melucuti Senjata (The Disarming Technique)',
                'description': 'menemukan butir kebenaran dalam kritik yang kamu terima, bahkan jika terasa tidak adil, untuk meredakan ketegangan.',
                'example': 'Kamu benar, aku sadar akhir-akhir ini aku memang kurang mendengarkan. Maafkan aku.',
                'when_to_use': 'Saat menerima kritik, keluhan, atau saat lawan bicara dalam posisi menyerang.'
            },
            'empathy': {
                'name': 'Empati Pikiran dan Perasaan (Thought and Feeling Empathy)',
                'description': 'mencoba memahami apa yang orang lain pikirkan (empati pikiran) dan rasakan (empati perasaan) secara tulus.',
                'example': 'Kedengarannya situasi itu membuatmu sangat frustrasi dan kecewa ya. Aku bisa membayangkan betapa beratnya itu untukmu.',
                'when_to_use': 'Saat seseorang mengekspresikan emosi yang kuat, baik positif maupun negatif.'
            },
            'inquiry': {
                'name': 'Pertanyaan Mendalam (Inquiry)',
                'description': 'mengajukan pertanyaan yang lembut dan tulus untuk membantu orang lain (dan dirimu) lebih memahami perasaan dan pikiran mereka.',
                'example': 'Bisa ceritakan lebih banyak, bagian mana yang terasa paling berat untukmu?',
                'when_to_use': 'Untuk mendorong seseorang berbagi lebih dalam, atau saat mereka tampak bingung dan tertutup.'
            },
            'i_feel': {
                'name': 'Pernyataan "Aku Merasa" (I Feel Statements)',
                'description': 'mengekspresikan perasaanmu sendiri secara jujur tanpa menyalahkan atau mengkritik orang lain.',
                'example': 'Aku merasa sedikit cemas dan sedih saat kita membahas masa depan.',
                'when_to_use': 'Saat kamu perlu mengungkapkan emosimu secara konstruktif tanpa memicu pertengkaran.'
            },
            'stroking': {
                'name': 'Pujian Tulus (Stroking)',
                'description': 'menyampaikan rasa hormat, penghargaan, dan kebaikan, bahkan di tengah perbedaan pendapat yang tajam.',
                'example': 'Aku sangat menghargai kejujuran dan keberanianmu untuk menceritakan ini kepadaku.',
                'when_to_use': 'Di sepanjang percakapan untuk menjaga hubungan tetap positif, terutama saat membahas topik yang sulit.'
            }
        }
        self.cognitive_distortions = {
            'all_or_nothing': {
                'name': 'Pemikiran Hitam-Putih (All-or-Nothing Thinking)',
                'description': 'Melihat segala sesuatu sebagai hitam atau putih, tanpa ada area abu-abu. Jika tidak sempurna, maka gagal total.',
                'example': '"Kalau aku tidak dapat nilai A di ujian ini, aku adalah mahasiswa gagal."',
                'reframe_question': 'Adakah kemungkinan lain di antara "sukses sempurna" dan "gagal total"? Di mana posisi pencapaianmu jika dilihat dalam skala 1 sampai 100?'
            },
            'overgeneralization': {
                'name': 'Generalisasi Berlebihan (Overgeneralization)',
                'description': 'Menganggap satu kejadian negatif sebagai pola kekalahan yang tidak akan pernah berakhir.',
                'example': '"Aku ditolak sekali, artinya aku tidak akan pernah punya pacar."',
                'reframe_question': 'Apakah satu pengalaman ini benar-benar bisa memprediksi seluruh masa depanmu? Bisakah kamu mengingat saat di mana hasilnya berbeda?'
            },
            'mental_filter': {
                'name': 'Filter Mental (Mental Filter)',
                'description': 'Memilih satu detail negatif dan memikirkannya terus-menerus, sehingga pandangan terhadap realitas menjadi gelap.',
                'example': 'Dosen memuji presentasiku, tapi dia memberi satu kritik kecil. Aku tidak bisa berhenti memikirkan kritik itu, presentasiku pasti buruk sekali.',
                'reframe_question': 'Selain detail negatif itu, apa lagi yang terjadi? Mari kita coba lihat gambaran yang lebih besar dan seimbang.'
            },
            'discounting_the_positive': {
                'name': 'Mengesampingkan Hal Positif (Discounting the Positive)',
                'description': 'Menolak pengalaman positif dengan bersikeras bahwa itu "tidak dihitung" karena suatu alasan.',
                'example': '"Aku lulus ujian itu, tapi itu cuma keberuntungan saja, bukan karena aku pintar."',
                'reframe_question': 'Bagaimana jika kamu mencoba menerima pujian atau pencapaian itu tanpa "tapi"? Apa peran usahamu sendiri dalam hasil positif tersebut?'
            },
            'jumping_to_conclusions': {
                'name': 'Lompat ke Kesimpulan (Jumping to Conclusions)',
                'description': 'Membuat interpretasi negatif tanpa ada fakta yang mendukung, termasuk Membaca Pikiran (Mind Reading) dan Meramal (Fortune Telling).',
                'example': '"Dia tidak membalas pesanku, dia pasti marah padaku." (Mind Reading) atau "Aku pasti akan gugup dan mengacaukan wawancara besok." (Fortune Telling)',
                'reframe_question': 'Apa bukti nyata yang kamu miliki untuk kesimpulan itu? Adakah penjelasan alternatif yang lebih mungkin?'
            },
            'magnification_minimization': {
                'name': 'Pembesaran dan Pengecilan (Magnification and Minimization)',
                'description': 'Membesar-besarkan kesalahan sendiri (magnification) dan mengecilkan kelebihan diri sendiri (minimization).',
                'example': '"Aku membuat kesalahan ketik di email, ini memalukan sekali!" sambil berpikir "Prestasi yang kuraih kemarin itu bukan apa-apa."',
                'reframe_question': 'Jika temanmu yang melakukan kesalahan ini, apakah kamu akan melihatnya sebesar ini? Bagaimana jika kamu mencoba melihat kelebihanmu sebesar caramu melihat kesalahanmu?'
            },
            'emotional_reasoning': {
                'name': 'Penalaran Emosional (Emotional Reasoning)',
                'description': 'Menganggap bahwa apa yang kamu rasakan pastilah cerminan dari kenyataan.',
                'example': '"Aku merasa seperti pecundang, jadi aku pasti seorang pecundang."',
                'reframe_question': 'Perasaan adalah sinyal, bukan fakta. Selain perasaan itu, apa fakta dari situasi ini? Apakah perasaan bisa berubah?'
            },
            'should_statements': {
                'name': 'Pernyataan "Harusnya" (Should Statements)',
                'description': 'Menyiksa diri sendiri atau orang lain dengan kata "harusnya", "seharusnya", "wajib". Ini menimbulkan rasa bersalah dan frustrasi.',
                'example': '"Aku seharusnya lebih rajin belajar." atau "Dia seharusnya tidak berkata seperti itu padaku!"',
                'reframe_question': 'Apa yang terjadi jika kata "harusnya" diganti dengan "aku berharap" atau "akan lebih baik jika"? Bagaimana itu mengubah perasaanmu?'
            },
            'labeling': {
                'name': 'Melabeli (Labeling and Mislabeling)',
                'description': 'Bentuk ekstrem dari generalisasi berlebihan. Bukannya berkata "aku membuat kesalahan", kamu melabeli diri: "aku adalah seorang yang bodoh".',
                'example': '"Aku bodoh." "Dia orang yang jahat."',
                'reframe_question': 'Apakah satu tindakan bisa mendefinisikan keseluruhan dirimu atau diri orang lain? Bisakah kita fokus pada perilakunya ("aku membuat kesalahan") daripada melabeli individunya?'
            },
            'blame': {
                'name': 'Menyalahkan (Blame)',
                'description': 'Menyalahkan orang lain atas masalah yang kita hadapi, atau sebaliknya, menyalahkan diri sendiri atas sesuatu yang bukan sepenuhnya salah kita.',
                'example': '"Hubungan ini gagal karena salahnya dia!" atau "Semua ini salahku."',
                'reframe_question': 'Dalam situasi ini, berapa persen tanggung jawabmu, tanggung jawabnya, dan tanggung jawab faktor lain? Mari kita lihat peran masing-masing pihak secara adil.'
            }
        }

        self.theme_patterns = {
            'masalah hubungan': ['putus', 'pacar', 'cinta', 'diputusin', 'pasangan', 'bertengkar', 'konflik', 'berantem', 'hubungan', 'dijauhi', 'diselingkuhi'],
            'self-esteem rendah': ['jelek', 'gagal', 'bodoh', 'pecundang', 'payah', 'gak berguna', 'gak pantes', 'insecure'],
            'stres akademik': ['kuliah', 'tugas', 'deadline', 'semester', 'nilai', 'lulus', 'skripsi', 'dosen', 'ujian', 'kampus'],
            'kelelahan': ['lelah', 'capek', 'burnout', 'exhausted', 'kewalahan', 'ga ada energi', 'drain', 'nggak sanggup'],
            'kecemasan': ['cemas', 'khawatir', 'anxious', 'takut', 'panik', 'overthinking', 'gugup', 'gelisah'],
            'kesedihan': ['sedih', 'down', 'putus asa', 'hampa', 'kecewa', 'nangis', 'hancur', 'patah hati'],
            'kebingungan': ['bingung', 'tersesat', 'confused', 'tidak tahu', 'galau', 'bimbang', 'arah'],
            'kemarahan': ['marah', 'kesal', 'jengkel', 'frustrasi', 'benci', 'dongkol', 'muak'],
        }

        self.deep_inquiries = {
            'masalah hubungan': [
                "Bagaimana perpisahan ini memengaruhi caramu memandang dirimu sendiri?",
                "Apa satu hal yang paling kamu rindukan dari hubungan itu?",
                "Dalam hubungan itu, kapan kamu merasa paling didengarkan dan kapan kamu merasa paling tidak didengarkan?",
                "Terlepas dari apa yang terjadi, hubungan seperti apa yang sebenarnya kamu dambakan di masa depan?"
            ],
            'self-esteem rendah': [
                "Sejak kapan suara kritis di kepalamu itu mulai berkata seperti itu?",
                "Jika kamu berbicara kepada seorang teman yang merasakan hal yang sama, apa yang akan kamu katakan padanya?",
                "Selain perasaan 'gagal' atau 'jelek' ini, bisakah kamu menyebutkan satu saja kualitas atau pencapaian yang kamu banggakan dari dirimu, sekecil apapun itu?",
                "Perasaan ini, apakah ia terasa seperti 100% fakta, atau ada sedikit bagian dari dirimu yang meragukannya?"
            ],
            'kelelahan': [
                "Selain lelah fisik, adakah kelelahan emosional yang kamu rasakan? Seperti apa rasanya?",
                "Kelelahan ini, apakah datang tiba-tiba atau sudah menumpuk sejak lama?",
                "Aktivitas apa yang biasanya bisa membuatmu kembali bersemangat, yang sekarang terasa tidak mempan lagi?",
                "Jika tubuh dan pikiranmu bisa bicara, kira-kira istirahat seperti apa yang paling mereka butuhkan saat ini?",
                "Pikiran apa yang membuatmu merasa paling terkuras energinya?"
            ],
            'stres akademik': [
                 "Pikiran apa yang paling sering muncul di kepalamu saat kamu merasa tertekan karena urusan akademik?",
                 "Bagaimana stres akademik ini memengaruhi kehidupanmu di luar kampus, misalnya hubungan dengan teman atau keluarga?",
                 "Jika kamu bisa mengubah satu hal tentang situasimu di kuliah saat ini, apa itu dan mengapa?",
                 "Seperti apa rasanya stres itu di tubuhmu? Di mana kamu paling merasakannya?",
                 "Apa yang biasanya kamu lakukan untuk mengatasi stres itu? Apakah cara itu membantu?"
            ]
        }
        
        # PERBAIKAN: Memastikan list ini tidak kosong
        self.motivational_quotes = [
            "Perubahan sejati datang dari kemauan untuk melihat diri sendiri dengan jujur dan welas asih.",
            "Setiap langkah kecil untuk memahami perasaanmu adalah sebuah kemenangan besar.",
            "Kamu memiliki kekuatan untuk mengubah dinamika hubunganmu, dimulai dari caramu berkomunikasi.",
            "Keberanian bukanlah ketiadaan rasa takut, tetapi kemauan untuk menghadapinya demi hubungan yang lebih baik."
        ]
        
    def get_emotional_validation(self, theme: str) -> str:
        """Memberikan validasi empatik untuk tema emosional yang terdeteksi."""
        validations = {
            'masalah hubungan': "Putus cinta itu sangat menyakitkan dan rumit. Wajar sekali jika kamu merasa hancur. Perasaanmu sangat valid.",
            'self-esteem rendah': "Sakit sekali rasanya ketika suara di dalam kepala kita sendiri menyerang diri kita. Terima kasih sudah berani membagikan perasaan yang sangat personal ini.",
            'kelelahan': "Tentu saja kamu merasa lelah. Beban yang kamu pikul itu nyata, dan kelelahan adalah sinyal bahwa kamu butuh jeda.",
            'stres akademik': "Tekanan akademik itu nyata dan sangat menguras energi. Wajar sekali jika kamu merasa stres dan terbebani.",
        }
        return validations.get(theme, f"Aku dengar kamu. Merasa {theme.replace('_', ' ')} itu pasti tidak mudah. Perasaanmu penting dan valid.")

    def get_contextual_suggestion(self, theme: str) -> str:
        """Memberikan saran/refleksi yang relevan dengan topik."""
        suggestions = {
            'masalah hubungan': "Seringkali dalam konflik, kita terjebak dalam menyalahkan. Coba refleksikan: selain menyalahkan, apa satu hal kecil yang bisa kamu lakukan untuk merawat dirimu sendiri saat ini? Mungkin melakukan hobi yang sempat terlupakan, atau menghubungi teman yang bisa memberimu energi positif.",
            'self-esteem rendah': "Pikiran negatif seringkali terasa seperti fakta, padahal sebenarnya hanya 'opini' dari otak kita. Coba identifikasi tiga kualitas positif dalam dirimu, sekecil apapun itu. Menuliskannya bisa membantu melatih otak untuk melihat sisi lain dari dirimu.",
            'kelelahan': "Kelelahan yang menumpuk seringkali bukan hanya soal kurang tidur, tapi juga terkurasnya energi emosional. Mungkin akan membantu jika kamu menjadwalkan 'waktu istirahat tanpa rasa bersalah' selama 15-30 menit setiap hari, di mana kamu melakukan sesuatu yang kamu nikmati tanpa memikirkan kewajiban.",
        }
        return suggestions.get(theme, "Mengakui perasaan ini adalah langkah pertama yang sangat kuat. Teruslah bersikap baik pada dirimu sendiri.")

    def detect_emotional_themes(self, text: str) -> List[str]:
        """Mendeteksi tema emosional dari teks."""
        themes = []
        text_lower = text.lower()
        # Mengurutkan berdasarkan panjang kata kunci untuk prioritas (misal: 'putus cinta' > 'cinta')
        sorted_themes = sorted(self.theme_patterns.items(), key=lambda x: -len(x[0]))
        for theme, keywords in sorted_themes:
            if any(keyword in text_lower for keyword in keywords):
                themes.append(theme)
        return list(set(themes))

    def get_deep_inquiry(self, theme: str, asked_questions: Set[str]) -> Optional[str]:
        """Mengambil pertanyaan mendalam yang relevan dan belum ditanyakan."""
        possible_questions = self.deep_inquiries.get(theme, [])
        unasked_questions = [q for q in possible_questions if q not in asked_questions]
        
        if not unasked_questions:
            return None # Mengembalikan None jika kehabisan pertanyaan
            
        return random.choice(unasked_questions)
        
    def get_motivational_quote(self) -> str:
        """Mengambil kutipan motivasi secara acak."""
        return random.choice(self.motivational_quotes)

