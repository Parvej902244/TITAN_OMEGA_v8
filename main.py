import asyncio
import sys
import logging
from core.logic.brain import TitanBrain

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("TITAN_CLI")

async def console_logger(text):
    """Simple callback to print updates to the console instead of Telegram."""
    print(f"\n{text}")

async def run_cli(target):
    print(f"""
    🧬 TITAN OMEGA v∞⁸ (CLI MODE)
    =============================
    Target: {target}
    Mode: Human-Grade Logic Hunter
    AI Brain: Active (Ollama)
    Real HTTP Engine: Active
    """)
    
    titan = TitanBrain()
    
    try:
        # Start the Scan Logic
        report_path = await titan.start_scan(target, console_logger)
        
        if report_path:
            print(f"\n🔥 CRITICAL FINDING REPORTED: {report_path}")
            print("Check the 'reports/active/' folder for details.")
        else:
            print("\n✅ Scan Complete. No Critical Logic Bugs found.")
            
    except KeyboardInterrupt:
        print("\n🛑 Scan Interrupted by User.")
    except Exception as e:
        logger.error(f"Critical System Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <target_domain>")
        print("Example: python3 main.py example.com")
        sys.exit(1)
    
    target_domain = sys.argv[1]
    asyncio.run(run_cli(target_domain))
  
