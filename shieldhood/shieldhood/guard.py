import re
import base64
import math
import yaml
import os
from datetime import datetime
from typing import Dict, Any, Optional, Tuple

VERSION = "2.0.0"

class DeepDecoder:
    """Deep payload decoding with multi-layer re-scanning"""
    
    @staticmethod
    def try_decode(text: str) -> list[str]:
        candidates = [text]
        lower = text.lower().strip()

        # Base64
        if re.search(r'[A-Za-z0-9+/]{20,}={0,2}', text):
            try:
                decoded = base64.b64decode(text.strip(), validate=False).decode('utf-8', errors='ignore')
                candidates.append(decoded)
            except:
                pass

        # Hex
        if re.search(r'^(?:[0-9a-f]{2})+$', lower) or re.search(r'[0-9a-f]{8,}', lower):
            try:
                clean = re.sub(r'[^0-9a-f]', '', lower)
                decoded = bytes.fromhex(clean).decode('utf-8', errors='ignore')
                candidates.append(decoded)
            except:
                pass

        # ROT-N
        for shift in [13, 5, 7]:
            decoded = ''.join(
                chr((ord(c) - 65 + shift) % 26 + 65) if 'A' <= c <= 'Z' else
                chr((ord(c) - 97 + shift) % 26 + 97) if 'a' <= c <= 'z' else c
                for c in text
            )
            if decoded != text:
                candidates.append(decoded)

        return list(set(candidates))

class Shieldhood:
    def __init__(self, config_path: str = "bankr.config.yaml"):
        self.config = self._load_config(config_path)
        self.pending_confirmation: Optional[str] = None
        self.daily_spend = 0
        self.last_reset = datetime.now().date()
        
        spending = self.config.get('spending', {})
        self.daily_limit = spending.get('daily_limit_usd', 5000)
        self.tx_limit = spending.get('tx_limit_usd', 1000)
        
        self.allowlist = self.config.get('allowlist', {}).get('addresses', [])
        self.allowlist_enabled = self.config.get('allowlist', {}).get('enabled', False)

    def _load_config(self, path: str) -> Dict:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return yaml.safe_load(f) or {}
        return {}

    def _reset_daily_if_needed(self):
        today = datetime.now().date()
        if today > self.last_reset:
            self.daily_spend = 0
            self.last_reset = today

    def calculate_entropy(self, text: str) -> float:
        if not text or len(text) < 5:
            return 0.0
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
        entropy = -sum((count / len(text)) * math.log2(count / len(text)) 
                      for count in freq.values())
        return entropy

    def scan(self, text: str) -> Dict[str, Any]:
        self._reset_daily_if_needed()
        score = 0
        findings = []
        lower = text.lower()

        # Injection keywords
        injection_keywords = ["ignore all previous", "override", "jailbreak", "system prompt", "new instructions", "forget previous", "developer mode"]
        if any(kw in lower for kw in injection_keywords):
            score += 45
            findings.append("INJECTION_KEYWORD")

        # Deep decode
        decoded_versions = DeepDecoder.try_decode(text)
        for decoded in decoded_versions:
            d_lower = decoded.lower()
            if any(kw in d_lower for kw in injection_keywords):
                score += 50
                findings.append("DECODED_INJECTION")
                break

        if re.search(r'[A-Za-z0-9+/]{30,}={0,2}', text):
            score += 30
            findings.append("BASE64_PAYLOAD")

        if self.calculate_entropy(text) > 4.2:
            score += 25
            findings.append("HIGH_ENTROPY")

        if any(ord(c) > 0xE0000 for c in text):
            score += 40
            findings.append("INVISIBLE_UNICODE")

        verdict = "MALICIOUS" if score >= 60 else "SUSPICIOUS" if score >= 35 else "CLEAN"
        
        return {
            "verdict": verdict,
            "score": min(score, 100),
            "findings": findings,
            "decoded_versions": len(decoded_versions) - 1,
            "requires_confirmation": verdict != "CLEAN"
        }

    def handle_command(self, cmd: str, context: Dict = None) -> str:
        if cmd.startswith("/shieldhood scan"):
            text = cmd[15:].strip()
            result = self.scan(text)
            if result["requires_confirmation"]:
                self.pending_confirmation = text
                return f"🛡️ Shieldhood v{VERSION}\nVerdict: {result['verdict']}\nScore: {result['score']}\nFindings: {result['findings']}\n\n🔐 HUMAN CONFIRMATION REQUIRED"
            return f"🛡️ Shieldhood v{VERSION}\nVerdict: {result['verdict']}\nScore: {result['score']}"

        elif cmd == "/shieldhood confirm" and self.pending_confirmation:
            self.pending_confirmation = None
            return "✅ Action confirmed."

        elif cmd == "/shieldhood cancel" and self.pending_confirmation:
            self.pending_confirmation = None
            return "❌ Action cancelled."

        return "🛡️ Shieldhood is active."

if __name__ == "__main__":
    print(f"✅ Shieldhood v{VERSION} ready!")
