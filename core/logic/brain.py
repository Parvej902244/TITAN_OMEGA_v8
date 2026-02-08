import asyncio
from core.network.session_manager import SessionManager
from intelligence.ai import AIEngine
from core.logic.sequencer import LogicSequencer
from reports.narrator import ReportNarrator

class TitanBrain:
    def __init__(self):
        self.net = SessionManager()
        self.ai = AIEngine()
        self.seq = LogicSequencer(self.net)
        self.reporter = ReportNarrator()
        self.is_active = False
        self.queue = []

    async def start_scan(self, target, update_callback):
        self.is_active = True
        await update_callback(f"🧠 **TITAN v∞⁸ STARTED:** `{target}`")
        
        # 1. DISCOVERY (Mocking list for brevity, real usage employs Subfinder)
        # In production: run subfinder and populate this list
        endpoints = ["/api/v1/user/profile", "/api/v1/transfer", "/admin/settings"]
        
        for ep in endpoints:
            if not self.is_active: break
            
            full_url = f"https://{target}{ep}"
            await update_callback(f"🔍 **Analyzing Logic:** `{ep}`")

            # 2. LOGIC TEST: IDOR (User A vs User B)
            resp_a = await self.net.fetch(full_url, "GET", "UserA")
            resp_b = await self.net.fetch(full_url, "GET", "UserB")
            
            # Differential Analysis: If B gets 200 OK and data looks like A's data structure
            if resp_a and resp_b and resp_b['status'] == 200:
                # 3. AI CRITIQUE
                critique = self.ai.critique_finding("IDOR", full_url, resp_b['body'])
                
                if critique.get('confidence', 0) > 80:
                    # 4. REPORT
                    bug = {
                        "title": "Broken Access Control (IDOR)",
                        "severity_label": "HIGH",
                        "severity_score": 2,
                        "confidence": critique['confidence'],
                        "url": full_url,
                        "param": "Auth Header",
                        "logic_type": "Ownership Bypass",
                        "simple_explanation": "User B can see User A's data because the server doesn't check ownership.",
                        "victim_id": "UserA_ID",
                        "response_len": resp_b['length'],
                        "business_impact": "Data Leakage of PII.",
                        "fix": "Implement Object-Level Permission Checks."
                    }
                    path = self.reporter.write_report(bug)
                    return path

            # 5. LOGIC TEST: RACE CONDITION
            if "transfer" in ep:
                race = await self.seq.check_race_condition(full_url, {"amount": 10})
                if race:
                    # Logic to report race condition...
                    pass

        await update_callback("✅ **Logic Exhausted. Scan Complete.**")
        self.is_active = False
        return None
      
