with open("mi_system.py", "r", encoding="utf-8") as f:
    content = f.read()

print("--- [ M I System Master File Inspection ] ---")
print(f"Total Master Body Size: {len(content)} bytes")
print("Checking for Mini Eye / Command keywords...")
for kw in ["eye", "director", "command", "health"]:
    found = kw in content.lower()
    print(f" - Keyword '{kw}': {'Present' if found else 'Missing'}")
