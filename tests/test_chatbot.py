# tests/test_chatbot.py
"""
Unit tests for the Mental Health Chatbot (V8 - The Relationship Expert, Final Version).
Verifies the final logic for natural conversation flow, memory, and proactive reflection.
"""

import unittest
import sys
import os

# Menambahkan direktori root ke path agar bisa mengimpor dari src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.chatbot import MentalHealthChatbot, ConversationStage

class TestMentalHealthChatbotV8Final(unittest.TestCase):

    def setUp(self):
        """Menyiapkan instance chatbot baru untuk setiap test."""
        self.chatbot = MentalHealthChatbot("TestUser")

    def test_01_empathy_first_on_relationship_issue(self):
        """
        Kasus 1: Menguji aturan "Empati di Atas Segalanya" pada topik putus cinta.
        """
        self.chatbot.get_response("halo")
        response = self.chatbot.get_response("aku baru putus cinta")

        self.assertIn("Putus cinta itu sangat menyakitkan", response, "Bot harus memberikan validasi spesifik untuk putus cinta.")
        self.assertEqual(self.chatbot.last_topic, 'masalah hubungan')
        self.assertIn('masalah hubungan', self.chatbot.validated_topics)
        self.assertTrue(any(q in response for q in self.chatbot.knowledge_base.deep_inquiries['masalah hubungan']), "Bot harus menanyakan pertanyaan mendalam tentang hubungan.")

    def test_02_maintains_context_and_avoids_repeating_questions(self):
        """
        Kasus 2: Memastikan bot menjaga konteks topik dan tidak mengulangi pertanyaan.
        """
        self.chatbot.get_response("halo")
        response1 = self.chatbot.get_response("aku capek banget sama kuliah")
        
        pertanyaan_pertama = None
        for q in self.chatbot.knowledge_base.deep_inquiries['kelelahan']:
            if q in response1:
                pertanyaan_pertama = q
                break
        self.assertIsNotNone(pertanyaan_pertama, "Pertanyaan pertama tidak ditemukan di respons.")

        response2 = self.chatbot.get_response("rasanya pusing dan ga bisa fokus")
        
        self.assertNotIn(pertanyaan_pertama, response2, "Bot seharusnya tidak mengulangi pertanyaan yang sama.")
        self.assertEqual(self.chatbot.last_topic, 'kelelahan')

    def test_03_proactive_reflection_after_threshold_is_met(self):
        """
        Kasus 3: Bot harus proaktif memberikan refleksi setelah topik dieksplorasi.
        """
        self.chatbot.get_response("halo")
        self.chatbot.get_response("pacarku marah-marah terus") # Count = 1, Topik: kemarahan
        self.chatbot.get_response("dia bilang aku nggak pernah dengerin") # Count = 2
        response = self.chatbot.get_response("aku jadi bingung harus gimana") # Count = 3, memicu refleksi
        
        self.assertEqual(self.chatbot.stage, ConversationStage.POST_REFLECTION, "Bot harus beralih ke state POST_REFLECTION.")
        self.assertIn("**Sebuah Refleksi:**", response, "Respons harus mengandung bagian refleksi.")
        self.assertIn("Bagaimana menurutmu?", response, "Respons refleksi harus diakhiri dengan pertanyaan terbuka.")
        self.assertTrue(len(response) > 100, "Respons refleksi harus cukup panjang dan mendalam.")

    def test_04_understands_end_phrases_and_offers_summary_path(self):
        """
        Kasus 4: Bot harus mengenali frasa akhir dan beralih ke refleksi, lalu menawarkan ringkasan.
        """
        self.chatbot.get_response("halo")
        self.chatbot.get_response("aku lagi cemas banget")
        
        reflection_response = self.chatbot.get_response("sudah, itu saja")
        self.assertEqual(self.chatbot.stage, ConversationStage.POST_REFLECTION)
        self.assertIn("**Sebuah Refleksi:**", reflection_response)

        post_reflection_response = self.chatbot.get_response("oke, aku mengerti")
        self.assertIn("Cukup katakan **'stop'** atau **'ringkasan'** untuk melihatnya.", post_reflection_response, "Bot harus menawarkan jalan untuk melihat ringkasan.")

    def test_05_avoids_repeating_validation_for_same_topic(self):
        """
        Kasus 5: Bot tidak boleh mengulang kalimat validasi untuk topik yang sama.
        """
        self.chatbot.get_response("halo")
        response1 = self.chatbot.get_response("aku lelah banget")
        validation_phrase = "Tentu saja kamu merasa lelah."
        self.assertIn(validation_phrase, response1)

        response2 = self.chatbot.get_response("pokoknya capek aja")
        self.assertNotIn(validation_phrase, response2, "Bot tidak boleh mengulangi validasi untuk topik yang sama.")

    def test_06_full_session_flow_to_closing_summary(self):
        """
        Kasus 6: Mensimulasikan alur percakapan lengkap yang diakhiri dengan ringkasan.
        """
        self.chatbot.get_response("halo")
        self.chatbot.get_response("aku stres karena skripsi")
        self.chatbot.get_response("rasanya buntu")
        
        closing_response = self.chatbot.get_response("stop")
        
        self.assertEqual(self.chatbot.stage, ConversationStage.CLOSING)
        self.assertIn("Refleksi dari Percakapan Kita", closing_response)
        self.assertIn("stres akademik", closing_response)
        self.assertTrue(any(quote in closing_response for quote in self.chatbot.knowledge_base.motivational_quotes))

if __name__ == '__main__':
    unittest.main()

