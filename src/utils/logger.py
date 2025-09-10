#utlis/logger.py

"""
Logging utilities for the chatbot
"""

import logging
import os
from datetime import datetime
from typing import Optional

class ChatLogger:
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        # Create logger
        self.logger = logging.getLogger("MentalHealthBot")
        self.logger.setLevel(logging.INFO)
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        
        # File handler
        log_file = os.path.join(
            log_dir, 
            f"chat_{datetime.now().strftime('%Y%m%d')}.log"
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(file_formatter)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_conversation(self, user_id: str, user_input: str, bot_response: str):
        """Log a conversation exchange"""
        self.logger.info(f"User {user_id}: {user_input}")
        self.logger.info(f"Bot: {bot_response}")
    
    def log_session_start(self, user_id: str):
        """Log session start"""
        self.logger.info(f"Session started for user {user_id}")
    
    def log_session_end(self, user_id: str, duration: Optional[int] = None):
        """Log session end"""
        if duration:
            self.logger.info(f"Session ended for user {user_id} (Duration: {duration}s)")
        else:
            self.logger.info(f"Session ended for user {user_id}")
    
    def log_error(self, error: Exception, context: str = ""):
        """Log an error"""
        self.logger.error(f"Error in {context}: {str(error)}", exc_info=True)