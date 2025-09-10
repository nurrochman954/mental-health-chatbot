# src/core/analyzer.py
"""
Conversation Analyzer V8 - Final
Menganalisis percakapan untuk menghasilkan ringkasan yang kaya dan bermanfaat.
"""

import re
from typing import List, Dict
from .knowledge_base import KnowledgeBase

class ConversationAnalyzer:
    def __init__(self):
        self.kb = KnowledgeBase()

    def get_conversation_summary_insights(self, conversation_history: List[Dict]) -> str:
        if not conversation_history:
            return "Tidak ada percakapan untuk direfleksikan."

        # Hapus sapaan awal agar tidak mengganggu analisis tema
        user_inputs = [h.get('user', '').lower() for h in conversation_history[1:] if h.get('user')]
        full_text = ' '.join(user_inputs)
        
        themes = self.kb.detect_emotional_themes(full_text)
        
        summary = "**Refleksi dari Percakapan Kita**\n\n"
        
        if themes:
            theme_list = [t.replace('_', ' ') for t in themes]
            summary += f"Fokus utama kita adalah seputar perasaan **{', '.join(theme_list)}**. Tampaknya ini adalah area yang paling membebani pikiranmu saat ini.\n\n"
        else:
            summary += "Kita telah membahas banyak hal penting dalam percakapan ini.\n\n"

        summary += "**Beberapa Observasi Penting:**\n"
        if len(conversation_history) > 5:
            summary += "- Kamu menunjukkan kemauan yang besar untuk berefleksi dan memahami perasaanmu lebih dalam. Itu adalah kekuatan yang luar biasa.\n"
        
        summary += "\n**Saran untuk Refleksi Lanjutan:**\n"
        if themes:
            unique_themes = set(themes)
            for theme in unique_themes:
                suggestion = self.kb.get_contextual_suggestion(theme)
                if suggestion:
                    summary += f"- **Terkait {theme.replace('_', ' ')}:** Ingatlah refleksi kita bahwa {suggestion[0].lower()}{suggestion[1:]}\n"
        
        summary += "- Teruslah berlatih mengenali dan menerima perasaan yang muncul, tanpa menghakiminya. Setiap emosi membawa pesan yang berharga.\n"
        
        return summary

