import json
import subprocess
import sys

def run_composio(tool_slug, data):
    cmd = [
        "/Users/satyyy/.composio/composio",
        "execute",
        tool_slug,
        "-d",
        json.dumps(data)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout, res.stderr

print("1. Searching Apollo People Search by Phone Number +14088368647...")
out1, err1 = run_composio("APOLLO_PEOPLE_SEARCH", {
    "q_keywords": "4088368647"
})
print("Result 1:", out1[:1000])

print("\n2. Searching Apollo People Search by Name 'Sushma' in California / 408 area code...")
out2, err2 = run_composio("APOLLO_PEOPLE_SEARCH", {
    "q_keywords": "Sushma",
    "person_locations": ["California", "San Jose", "Bay Area", "United States"]
})
print("Result 2:", out2[:1500])

print("\n3. Searching Apollo People Search by Name 'Sushma Suvva'...")
out3, err3 = run_composio("APOLLO_PEOPLE_SEARCH", {
    "q_keywords": "Sushma Suvva"
})
print("Result 3:", out3[:1500])

print("\n4. Searching Apollo People Search for 'Thanvi Suvva'...")
out4, err4 = run_composio("APOLLO_PEOPLE_SEARCH", {
    "q_keywords": "Thanvi Suvva"
})
print("Result 4:", out4[:1500])
