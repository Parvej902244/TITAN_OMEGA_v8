import asyncio

class LogicSequencer:
    def __init__(self, network_manager):
        self.net = network_manager

    async def check_race_condition(self, url, data):
        """
        Layer 4: Sends 5 simultaneous requests to check for Race Conditions.
        """
        # Create 5 identical tasks
        tasks = [self.net.fetch(url, "POST", "UserA", data) for _ in range(5)]
        responses = await asyncio.gather(*tasks)
        
        # Analyze: Did all 5 succeed? (If business logic says only 1 should)
        success_count = sum(1 for r in responses if r and r['status'] == 200)
        
        if success_count > 1:
            return {
                "bug": "Race Condition",
                "details": f"{success_count}/5 requests processed successfully (Should be 1)."
            }
        return None
      
