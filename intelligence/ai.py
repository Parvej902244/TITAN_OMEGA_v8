import requests
import json
from config.settings import OLLAMA_URL, AI_MODEL

class AIEngine:
    def think(self, prompt, context=""):
        full_prompt = f"Context: {context}\nTask: {prompt}\nAnswer strictly in JSON."
        try:
            r = requests.post(OLLAMA_URL, json={"model": AI_MODEL, "prompt": full_prompt, "stream": False, "format": "json"})
            return json.loads(r.json()['response'])
        except: return {"error": "AI_OFFLINE"}

    def critique_finding(self, bug_type, endpoint, evidence):
        """
        Layer 6: AI Self-Critique Loop.
        Arguments against itself to reduce False Positives.
        """
        prompt = f"""
        I found a potential {bug_type} at {endpoint}.
        Evidence: {evidence[:500]}...
        
        Act as a Senior Security Reviewer.
        1. Why might this be a False Positive? (e.g., Public data, intended behavior)
        2. Give a confidence score (0-100) after critique.
        
        Output format: JSON {{ "confidence": int, "reasoning": "string" }}
        """
        return self.think(prompt)
      
