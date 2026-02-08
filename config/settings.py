import os

# --- AUTHENTICATION ---
TELEGRAM_TOKEN = "8145833691:AAG1kq1ntWNjkQQvZJra2oIOloykLclqQHY"
ADMIN_ID = 0  # 0 = Public Access (Dev Mode). Set to your ID for security.

# --- AI BRAIN (OLLAMA LOCAL) ---
OLLAMA_URL = "http://localhost:11434/api/generate"
AI_MODEL = "mistral" 

# --- SAFETY & PERFORMANCE ---
MAX_CONCURRENCY = 10
REQUEST_DELAY = 0.2
STOP_ON_CRITICAL = True
SAVE_STATE_INTERVAL = 60 # Seconds
