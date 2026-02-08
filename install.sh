#!/bin/bash
echo "🧬 INITIALIZING TITAN OMEGA v∞⁸ (HUMAN-GRADE)..."

# 1. Install System Deps
sudo apt update && sudo apt install -y python3-pip

# 2. Install Python Deps
pip3 install -r requirements.txt

# 3. Check AI
if ! pgrep -x "ollama" > /dev/null; then
    echo "⚠️ Starting Ollama (AI Brain)..."
    ollama serve &
fi

# 4. Start Bot
python3 bot.py
