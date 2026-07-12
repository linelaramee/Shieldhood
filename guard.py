import re
import base64
import math

VERSION = "1.1.0"

def calculate_entropy(text: str) -> float:
    if not text:
        return 0.0
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    entropy = -sum((count / len(text)) * math.log2(count / len(text)) for count in freq.values())
    return entropy

def scan(text: str):
    score = 0
    findings = []
    lower = text.lower()

    # 1. Injection keywords
    if any(kw in lower for kw in ["ignore all previous", "override", "jailbreak", "forget previous", "new instructions"]):
        score += 50
        findings.append("INJECTION_KEYWORD")

    # 2. Base64 detection
    if re.search(r'[A-Za-z0-9+/]{30,}={0,2}', text):
        score += 35
        findings.append("BASE64_PAYLOAD")

    # 3. High entropy (hidden payload)
    if calculate_entropy(text) > 4.5:
        score += 25
        findings.append("HIGH_ENTROPY")

    # Verdict
    verdict = "MALICIOUS" if score >= 60 else "SUSPICIOUS" if score >= 30 else "CLEAN"

    return {
        "verdict": verdict,
        "score": score,
        "findings": findings,
        "requires_confirmation": verdict == "MALICIOUS"
    }

def handle_command(cmd: str, context=None):
    if cmd.startswith("/shieldhood scan"):
        text = cmd[15:].strip()
        result = scan(text)
        return f"🛡️ Shieldhood Scan v{VERSION}\nVerdict: {result['verdict']}\nScore: {result['score']}/100\nFindings: {result['findings']}\nRequires Confirmation: {result['requires_confirmation']}"
    return "🛡️ Shieldhood is active and protecting your agent on Robinhood Chain."

if __name__ == "__main__":
    print(f"✅ Shieldhood v{VERSION} ready to guard your agent!")
