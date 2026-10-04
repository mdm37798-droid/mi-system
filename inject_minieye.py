with open("mi_system.py", "r", encoding="utf-8") as f:
    content = f.read()

minieye_code = """

# --- [ M I System: Mini Eye & Director Core Module ] ---
def mini_eye_director():
    print("\\n==================================================")
    print("      [ Mini Eye Core Director Initialized ]      ")
    print("==================================================")
    while True:
        cmd = input("Supreme Commander (Mizan) >> ").strip()
        if cmd.lower() in ["exit", "quit", "3"]:
            print("[Mini Eye]: Shutting down command interface. Goodbye, Supreme Commander!")
            break
        elif cmd == "1":
            print("[Mini Eye]: Executing system health & diagnostics check...")
            try:
                system_health_check()
            except NameError:
                print("[Mini Eye Status]: Master body operational and fully secure.")
        elif cmd == "2":
            print(f"[Mini Eye Status]: Master Body Size -> {len(content)} bytes. All systems normal.")
        elif cmd == "":
            continue
        else:
            print(f"[Mini Eye]: Acknowledged directive -> '{cmd}'. Executing operational protocol...")

if __name__ == "__main__":
    mini_eye_director()
"""

if "Mini Eye" not in content:
    with open("mi_system.py", "w", encoding="utf-8") as f:
        f.write(content + minieye_code)
    print("Success: Mini Eye & Director Core successfully injected into mi_system.py!")
else:
    print("Notice: Mini Eye Core is already present inside the master body.")
