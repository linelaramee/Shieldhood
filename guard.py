import re
import base64
import math

VERSION = "1.3.0"

class Shieldhood:
    def __init__(self):
        self.pending_confirmation = None
        self.daily_spend = 0
        self.daily_limit = 5000
        self.tx_limit = 1000

    def calculate_entropy(self, text: str) -> float:
        if not text:
            return 0.0
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
        entropy = -sum((count / len(text)) * math.log2(count / len(text)) for count in freq.values())
        return entropy

    def scan(self, text: str):
        score = 0
        findings = []
        lower = text.lower()

        if any(kw in lower for kw in ["ignore all previous", "override", "jailbreak"]):
            score += 50
            findings.append("INJECTION_KEYWORD")

        if re.search(r'[A-Za-z0-9+/]{30,}={0,2}', text):
            score += 35
            findings.append("BASE64_PAYLOAD")

        if self.calculate_entropy(text) > 4.5:
            score += 25
            findings.append("HIGH_ENTROPY")

        verdict = "MALICIOUS" if score >= 60 else "SUSPICIOUS" if score >= 30 else "CLEAN"

        return {
            "verdict": verdict,
            "score": score,
            "findings": findings,
            "requires_confirmation": verdict in ["MALICIOUS", "SUSPICIOUS"]
        }

    def check_spending(self, amount_usd: float):
        if amount_usd > self.tx_limit:
            return False, f"Transaction exceeds single tx limit (${self.tx_limit})"
        if self.daily_spend + amount_usd > self.daily_limit:
            return False, f"Exceeds daily limit (remaining: ${self.daily_limit - self.daily_spend})"
        return True, "OK"

    def handle_command(self, cmd: str, context=None):
        if cmd.startswith("/shieldhood scan"):
            text = cmd[15:].strip()
            result = self.scan(text)
            if result["requires_confirmation"]:
                self.pending_confirmation = text
                return f"🛡️ Shieldhood v{VERSION}\nVerdict: {result['verdict']}\nScore: {result['score']}/100\nFindings: {result['findings']}\n\n🔐 HUMAN CONFIRMATION REQUIRED\nUse /shieldhood confirm to proceed."
            return f"🛡️ Shieldhood v{VERSION}\nVerdict: {result['verdict']}\nScore: {result['score']}/100\nFindings: {result['findings']}"

        elif cmd == "/shieldhood confirm" and self.pending_confirmation:
            self.pending_confirmation = None
            return "✅ Action confirmed and executed."

        elif cmd == "/shieldhood cancel" and self.pending_confirmation:
            self.pending_confirmation = None
            return "❌ Action cancelled."

        return "🛡️ Shieldhood is active and protecting your agent on Robinhood Chain."

if __name__ == "__main__":
    print(f"✅ Shieldhood v{VERSION} ready to guard!")
