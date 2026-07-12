# Shieldhood Skill for Bankr.bot

## Description

Shieldhood is an AI Security Skill / Layer for **Bankr.bot**, specifically optimized for Robinhood Chain.  

It acts as the **last line of defence** at the AI level, protecting autonomous DeFi agents from prompt injection, jailbreaks, and malicious commands that could result in unauthorized transfers or dangerous executions.

## Key Features (v2.0)

- Deep multi-layer detection with recursive payload decoding (Base64, Hex, ROT-N, High Entropy, Invisible Unicode, etc.)
- Human confirmation gate for high-risk actions
- Configurable spending policy (daily and per-transaction limits)
- Address allowlist support
- YAML-based configuration
- Lightweight and fast (pure Python)

## Available Commands

- `/shieldhood scan <text>` → Run full security scan on prompt/command
- `/shieldhood status` → Show shield status, daily spending, and configuration
- `/shieldhood confirm` → Approve and proceed with pending action
- `/shieldhood cancel` → Cancel pending action
- `/shieldhood help` → Display command list

## Integration with Bankr.bot

```python
from guard import Shieldhood

# Initialize the shield (usually done during skill loading)
shield = Shieldhood(config_path="bankr.config.yaml")

# Inside Bankr.bot main command handler
def handle_user_command(command: str, context: dict = None):
    # Route Shieldhood commands
    if command.startswith("/shieldhood"):
        return shield.handle_command(command, context)
    
    # Optional: Auto-scan every incoming command
    scan_result = shield.scan(command)
    if scan_result["requires_confirmation"]:
        # Block execution and request human confirmation
        return "🛡️ Shieldhood detected potential risk. Use /shieldhood confirm or /shieldhood cancel."
    
    # Continue with normal Bankr.bot logic...

ConfigurationCopy the example configuration file:bash

cp bankr.config.yaml.example bankr.config.yaml

Then adjust limits, enable allowlist, etc. according to your risk tolerance.RequirementsPython 3.10+
PyYAML (pip install pyyaml)
Bankr.bot skill environment

Author: 0xPoyraz (@0xPoyraz
)


