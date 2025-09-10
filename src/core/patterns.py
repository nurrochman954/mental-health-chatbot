# src/core/patterns.py
"""
Simplified patterns untuk response yang lebih natural
Fokus pada empati dan pertanyaan follow-up yang thoughtful
"""

import re

# Simplified patterns - lebih natural, kurang robotic
EMOTION_PATTERNS = {
    'greeting': {
        'patterns': [r'\b(hai|halo|hello|hi|selamat)\b'],
        'responses': [
            "Hai! Gimana kabarnya hari ini?",
            "Hello! Ada yang mau diceritain?",
            "Hai! Apa yang lagi ada di pikiran kamu?"
        ]
    },
    
    'gratitude': {
        'patterns': [r'\b(terima kasih|makasih|thanks|thank you)\b'],
        'responses': [
            "Sama-sama! Senang bisa dengerin kamu.",
            "Thanks juga udah mau sharing dengan jujur.",
            "Appreciate banget keterbukaan kamu."
        ]
    },
    
    'help_request': {
        'patterns': [r'\b(bantuan|help|tolong|gimana|bagaimana)\b'],
        'responses': [
            "Aku di sini untuk dengerin. Cerita aja apa yang kamu rasain.",
            "Mau mulai dari mana? Aku siap mendengarkan.",
            "Apa yang paling berat di pikiran kamu sekarang?"
        ]
    },
    
    'confusion': {
        'patterns': [r'\b(bingung|confused|tidak tahu|nggak tahu|lost)\b'],
        'responses': [
            "Bingung itu nggak enak ya. Apa yang bikin kamu ngerasa lost?",
            "Wajar kok merasa bingung. Mau cerita situasinya gimana?",
            "Kadang kita butuh waktu untuk clarity. Apa yang paling confusing?"
        ]
    }
}

# Simple topic-based responses
TOPIC_RESPONSES = {
    'academic': {
        'keywords': ['kuliah', 'kampus', 'tugas', 'skripsi', 'lulus', 'study'],
        'responses': [
            "Kuliah emang challenging ya. Apa yang paling berat sekarang?",
            "Academic life bisa overwhelming. Mau cerita lebih detail?",
            "Gimana experience kamu di kampus selama ini?"
        ]
    },
    
    'relationship': {
        'keywords': ['pacar', 'teman', 'keluarga', 'hubungan', 'relationship'],
        'responses': [
            "Hubungan dengan orang lain emang kompleks. Mau sharing?",
            "Sounds like ada dinamika yang tricky. Cerita dong.",
            "Gimana perasaan kamu tentang hubungan ini?"
        ]
    },
    
    'future': {
        'keywords': ['masa depan', 'future', 'rencana', 'goals', 'karier'],
        'responses': [
            "Mikirin masa depan kadang bikin anxious ya. Apa yang kamu khawatirin?",
            "Planning untuk future itu penting tapi juga bisa stressful. Gimana menurutmu?",
            "Apa yang bikin kamu excited atau worried tentang ke depannya?"
        ]
    }
}

# Empathetic fallback responses - natural dan varied
EMPATHETIC_RESPONSES = [
    "Hmm, kedengarannya important buat kamu. Mau cerita lebih detail?",
    "Aku pengen ngerti lebih dalam. Bisa explain lebih lanjut?",
    "Sounds like ada story di balik ini. Apa yang paling stick out?",
    "I hear you. Gimana perasaan kamu tentang situasi ini?",
    "Menarik yang kamu bilang. Help me understand better?",
    "Aku ngerasain ada something meaningful di situ. Cerita dong.",
    "That sounds significant. Apa yang bikin ini important buat kamu?",
    "Kayaknya ada complexity di sini. Mau elaborate?",
    "Tell me more. Aku curious sama perspective kamu.",
    "Aku dengerin. Apa yang paling challenging dari situasi ini?"
]

def get_pattern_response(user_input: str, conversation_context: dict = None) -> str:
    """
    Simple pattern matching yang menghasilkan response natural
    """
    user_input_lower = user_input.lower()
    
    # Check emotion patterns first
    for emotion, data in EMOTION_PATTERNS.items():
        for pattern in data['patterns']:
            if re.search(pattern, user_input_lower):
                import random
                return random.choice(data['responses'])
    
    # Check topic patterns
    for topic, data in TOPIC_RESPONSES.items():
        for keyword in data['keywords']:
            if keyword in user_input_lower:
                import random
                return random.choice(data['responses'])
    
    # Fallback to empathetic response
    import random
    return random.choice(EMPATHETIC_RESPONSES)