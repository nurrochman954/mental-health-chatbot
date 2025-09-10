# src/core/chatbot.py
"""
Mental Health Chatbot V9 - The Polished Engine
Versi final dengan perbaikan logika untuk memastikan prioritas respons yang benar
dan transisi state percakapan yang andal, berdasarkan hasil unit test.
"""

import random
from typing import List, Dict, Optional, Set
from datetime import datetime
from enum import Enum, auto

from .knowledge_base import KnowledgeBase
from .analyzer import ConversationAnalyzer
from .patterns import get_pattern_response

class ConversationStage(Enum):
    GREETING = auto()
    EXPLORATION = auto()
    REFLECTION = auto()
    POST_REFLECTION = auto()
    CLOSING = auto()

class MentalHealthChatbot:
    def __init__(self, user_name: str = "User"):
        self.user_name = user_name
        self.conversation_history: List[Dict] = []
        
        self.knowledge_base = KnowledgeBase()
        self.analyzer = ConversationAnalyzer()
        
        # State Management
        self.stage = ConversationStage.GREETING
        self.last_topic: Optional[str] = None
        self.questions_asked: Set[str] = set()
        self.validated_topics: Set[str] = set()
        self.reflected_topics: Set[str] = set()
        
        self.topic_exploration_count = 0
        self.SUGGESTION_THRESHOLD = 3 

    def get_response(self, user_input: str) -> str:
        self.conversation_history.append({'user': user_input, 'timestamp': datetime.now()})
        
        if user_input.lower().strip() in ['stop', 'quit', 'exit', 'bye', 'keluar', 'selesai', 'ringkasan']:
            self.stage = ConversationStage.CLOSING
        
        response = ""
        if self.stage == ConversationStage.GREETING:
            response = self._handle_greeting()
            self.stage = ConversationStage.EXPLORATION
        elif self.stage == ConversationStage.EXPLORATION:
            response = self._get_exploration_response(user_input)
        elif self.stage == ConversationStage.REFLECTION:
            response = self._get_reflection_response()
        elif self.stage == ConversationStage.POST_REFLECTION:
            response = self._handle_post_reflection(user_input)
        elif self.stage == ConversationStage.CLOSING:
            response = self._handle_closing()

        self.conversation_history[-1]['bot_response'] = response
        return response

    def _get_exploration_response(self, user_input: str) -> str:
        """Logika inti V9: Memperbaiki alur deteksi dan transisi state."""
        
        end_phrases = ['sudah, itu saja', 'cukup', 'itu aja', 'ga ada lagi', 'tidak ada', 'entahlah', 'ga tau', 'tidak bisa', 'lumayan']
        if user_input.lower().strip() in end_phrases and self.last_topic:
            if self.last_topic not in self.reflected_topics:
                self.stage = ConversationStage.REFLECTION
                return self._get_reflection_response()
            else:
                self.stage = ConversationStage.POST_REFLECTION
                return self._handle_post_reflection(user_input)

        themes = self.knowledge_base.detect_emotional_themes(user_input)
        
        # PERBAIKAN LOGIKA FINAL: Konteks topik dibuat lebih "lengket" dan cerdas.
        current_theme = themes[0] if themes else self.last_topic
        
        if current_theme:
            if current_theme != self.last_topic:
                # Topik baru terdeteksi, reset state
                self._reset_topic_state(current_theme)
            
            # Selalu increment counter jika sebuah topik sedang aktif
            self.topic_exploration_count += 1
        
        # Memicu refleksi jika threshold tercapai
        if self.last_topic and self.topic_exploration_count >= self.SUGGESTION_THRESHOLD:
            if self.last_topic not in self.reflected_topics:
                self.stage = ConversationStage.REFLECTION
                return self._get_reflection_response()

        # Alur utama: Validasi lalu bertanya
        if self.last_topic:
            validation = ""
            if self.last_topic not in self.validated_topics:
                validation = self.knowledge_base.get_emotional_validation(self.last_topic) + " "
                self.validated_topics.add(self.last_topic)

            deep_inquiry = self.knowledge_base.get_deep_inquiry(self.last_topic, self.questions_asked)
            if deep_inquiry:
                self.questions_asked.add(deep_inquiry)
                return f"{validation}{deep_inquiry}"

        # Fallback HANYA jika semua logika di atas gagal
        return get_pattern_response(user_input)
            
    def _get_reflection_response(self) -> str:
        if not self.last_topic:
            self.stage = ConversationStage.EXPLORATION
            return "Tentu, aku mengerti. Ada hal lain yang ingin kamu ceritakan?"
        
        suggestion = self.knowledge_base.get_contextual_suggestion(self.last_topic)
        self.reflected_topics.add(self.last_topic)
        self.stage = ConversationStage.POST_REFLECTION
        
        return (f"Terima kasih sudah berbagi begitu dalam tentang {self.last_topic.replace('_', ' ')}. Aku bisa melihat betapa ini memengaruhimu.\n\n"
                f"**Sebuah Refleksi:** {suggestion}\n\n"
                "Ini bukan solusi instan, tapi semoga bisa memberikan sudut pandang baru. Bagaimana menurutmu?")

    def _handle_post_reflection(self, user_input: str) -> str:
        self.stage = ConversationStage.EXPLORATION
        self._reset_topic_state()
        
        return ("Baik, aku mengerti. Kita bisa membahas topik lain jika kamu mau. "
                "Atau, jika kamu merasa sesi ini sudah cukup, aku bisa membantumu merangkum semua yang telah kita bicarakan. "
                "Cukup katakan **'stop'** atau **'ringkasan'** untuk melihatnya.")
    
    def _reset_topic_state(self, new_topic: Optional[str] = None):
        self.last_topic = new_topic
        self.topic_exploration_count = 0

    def _handle_greeting(self) -> str:
        return (f"Halo {self.user_name}! Senang bisa ngobrol denganmu. Aku di sini untuk mendengarkan tanpa menghakimi. "
                "Silakan ceritakan apa yang sedang kamu rasakan atau pikirkan saat ini.")

    def _handle_closing(self) -> str:
        summary = self.analyzer.get_conversation_summary_insights(self.conversation_history)
        motivation = self.knowledge_base.get_motivational_quote()
        return (f"Tentu. Terima kasih banyak sudah meluangkan waktu untuk berbagi dan berefleksi, {self.user_name}.\n\n"
                f"{summary}\n\n"
                f"Sebagai penutup, ingatlah ini: **\"{motivation}\"**\n\n"
                "Jaga diri baik-baik, ya. Kamu tidak sendirian. 💙")

