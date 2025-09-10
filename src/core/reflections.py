# src/core/reflections.py
"""
Simplified reflection untuk natural conversation flow
Fokus pada yang essential aja
"""

import re

# Basic pronoun reflections untuk Indonesian
BASIC_REFLECTIONS = {
    r'\bsaya\b': 'kamu',
    r'\baku\b': 'kamu', 
    r'\bku\b': 'mu',
    r'\bkamu\b': 'aku',
    r'\bmu\b': 'ku',
    r'\banda\b': 'saya'
}

def reflect_pronouns(text: str) -> str:
    """
    Simple pronoun reflection - hanya untuk kasus yang really needed
    """
    reflected = text.lower()
    
    for pattern, replacement in BASIC_REFLECTIONS.items():
        reflected = re.sub(pattern, replacement, reflected, flags=re.IGNORECASE)
    
    return reflected

def should_use_reflection(user_input: str) -> bool:
    """
    Tentukan apakah perlu pakai reflection atau tidak
    Seringkali natural response tanpa reflection lebih baik
    """
    # Hanya gunakan reflection untuk kasus spesifik
    reflection_triggers = [
        'saya merasa',
        'aku merasa', 
        'saya ingin',
        'aku ingin'
    ]
    
    user_lower = user_input.lower()
    return any(trigger in user_lower for trigger in reflection_triggers)