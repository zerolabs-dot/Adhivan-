#!/usr/bin/env python3
"""
Debug script to test regex patterns
"""

import re

# Sample text
text = """Forest Rights Act Claim Application

Claim ID: FRA/2023/MP/12345
Applicant Name: Ramesh Kumar Gond
Tribe/Community: Gond
Village: Khairwani
District: Mandla
State: Madhya Pradesh

Type of Claim: Individual Forest Rights (IFR)
Land Area Claimed: 2.5 hectares
Application Date: 15-07-2023"""

# Test patterns
patterns = {
    'claimant_name': [
        r'(?:applicant\s+name|name)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
    ],
    'village': [
        r'(?:village)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
    ],
    'district': [
        r'(?:district)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
    ],
    'state': [
        r'(?:state)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
    ],
}

print("Testing regex patterns:")
print("=" * 50)

for entity_type, pattern_list in patterns.items():
    print(f"\n{entity_type.upper()}:")
    for pattern in pattern_list:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        print(f"  Pattern: {pattern}")
        print(f"  Matches: {matches}")

# Test individual lines
print("\n" + "=" * 50)
print("Testing individual lines:")
lines = text.split('\n')
for i, line in enumerate(lines):
    print(f"{i}: {line}")