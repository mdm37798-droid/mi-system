from flask import Flask, render_template_string, request
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_PATH = os.path.join(BASE_DIR, 'science_vault.json')

# মেমোরি লোড করা
if os.path.exists(VAULT_PATH):
    try:
        with open(VAULT_PATH, 'r', encoding='utf-8') as f:
            science_vault = json.load(f)
    except Exception:
        science_vault = {}
else:
    science_vault = {"Physics": "শক্তি অবিনশ্বর এবং রূপান্তরিত হয়।"}

def save_vault():
    with open(VAULT_PATH, 'w', encoding='utf-8') as f:
        json.dump(science_vault, f, ensure_ascii=False, indent=4)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>M I System - Supreme Chat</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: sans-serif; margin: 0; padding: 20px; display: flex; flex-direction: column; height: 90vh; }
        h2 { text-align: center; color: #38bdf8; }
        #chat-box { flex: 1; overflow-y: auto; background: #1e293b; padding: 15px; border-radius: 10px; margin-bottom: 15px; border: 1px solid #334155; }
        .message { margin-bottom: 10px; line-height: 1.5; }
        .user { color: #60a5fa; font-weight: bold; }
        .system { color: #4ade80; font-weight: bold; }
        form { display: flex; gap: 10px; }
        input { flex: 1; padding: 12px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; font-size: 16px; }
        button { padding: 12px 20px; background: #0ea5e9; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
        button:hover { background: #0284c7; }
    </style>
</head>
<body>
    <h2>--- [ M I System v9.3 ] ---</h2>
    <div id="chat-box">
        {% for q, a in vault.items() %}
            <div class="message"><span class="user">প্রশ্ন:</span> {{ q }}</div>
            <div class="message"><span class="system">M I System:</span> {{ a }}</div>
        {% endfor %}
    </div>
    <form method="POST">
        <input type="text" name="query" placeholder="আপনার বৈজ্ঞানিক লজিক বা প্রশ্ন লিখুন..." required autocomplete="off">
        <button type="submit">প্রেরণ</button>
    </form>
    <script>
        const chatBox = document.getElementById('chat-box');
        chatBox.scrollTop = chatBox.scrollHeight;
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            response = f"বিশ্লেষণ সফল: '{query}' সিস্টেমে সংরক্ষণ করা হলো।"
            science_vault[query] = response
            save_vault()
    return render_template_string(HTML_TEMPLATE, vault=science_vault)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

# ==============================================================================
# MODULE: Radio Signal Receive and Phone Data Sharing
# ==============================================================================
import json
import time

class RadioSignalBridgeModule:
    def __init__(self, frequency=99.9):
        self.frequency = frequency
        self.is_active = False

    def start_signal_receiver(self):
        self.is_active = True
        print(f"[RadioModule] Receiver activated on frequency: {self.frequency} MHz")
        return True

    def capture_and_share_data(self):
        if not self.is_active:
            return "Receiver is inactive."
        captured_data = {
            "timestamp": time.time(),
            "frequency": self.frequency,
            "signal_status": "Connected",
            "payload": "Radio_Signal_Packet_OK"
        }
        print(f"[DataShare] Shared to phone: {json.dumps(captured_data)}")
        return captured_data

# ==============================================================================
# MODULE: Configuration Manager & File Runner
# ==============================================================================
import os
import json

class ConfigManagerModule:
    def __init__(self, config_filename="identity.json"):
        self.config_filename = config_filename
        self.settings = {}
        self.load_configuration()

    def load_configuration(self):
        if os.path.exists(self.config_filename):
            try:
                with open(self.config_filename, "r", encoding="utf-8") as f:
                    self.settings = json.load(f)
                print(f"[ConfigModule] Configuration loaded successfully from {self.config_filename}")
            except Exception as e:
                print(f"[ConfigModule] Error loading config: {e}")
        else:
            print(f"[ConfigModule] Config file not found. Creating default configuration...")
            self.settings = {"app_mode": "master", "status": "active", "version": "1.0.0"}
            self.save_configuration()

    def save_configuration(self):
        try:
            with open(self.config_filename, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=4)
            print(f"[ConfigModule] Configuration saved to {self.config_filename}")
        except Exception as e:
            print(f"[ConfigModule] Error saving config: {e}")

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

if __name__ == "__main__":
    cfg = ConfigManagerModule()
    print("Configuration status checked.")

# ==============================================================================
# MODULE: App Auto-Update & Dynamic Feature Loader
# ==============================================================================
import urllib.request
import json
import os

class AppUpdateManager:
    def __init__(self, current_version="1.0.0", update_manifest_url=""):
        self.current_version = current_version
        self.manifest_url = update_manifest_url

    def check_for_updates(self):
        print(f"[UpdateManager] Checking current version ({self.current_version}) against remote server...")
        # Placeholder for version check logic
        return {"update_available": False, "latest_version": self.current_version}

    def load_dynamic_feature(self, feature_name):
        print(f"[DynamicFeature] Loading feature module: {feature_name}")
        # Dynamic plugin or feature loading logic
        return True

if __name__ == "__main__":
    updater = AppUpdateManager()
    updater.check_for_updates()

# ==============================================================================
# MODULE: Notification Status Bar Live Foreground Service
# ==============================================================================
import time
import threading

class NotificationStatusBarModule:
    def __init__(self, app_name="Mi Super Power"):
        self.app_name = app_name
        self.is_running = False

    def start_live_status_bar(self):
        self.is_running = True
        print(f"[{self.app_name}] Foreground Status Bar Live Service Started.")
        # Simulating live status bar background runner loop
        while self.is_running:
            print(f"[{self.app_name} Status Bar] Running live... Status: Active")
            time.sleep(10)

    def stop_live_status_bar(self):
        self.is_running = False
        print(f"[{self.app_name}] Status Bar Service Stopped.")

if __name__ == "__main__":
    notif_service = NotificationStatusBarModule()
    # notif_service.start_live_status_bar()

# ==============================================================================
# MODULE: App Data Control & Traffic Limiter
# ==============================================================================
import json

class AppDataControlModule:
    def __init__(self, policy_file="data_policy.json"):
        self.policy_file = policy_file
        self.restricted_apps = {}
        self.load_policies()

    def load_policies(self):
        print("[DataControl] Loading application network restriction policies...")
        # Policy initialization for restricting background data or ads
        self.restricted_apps = {"ads_blocked": True, "background_data_restricted": True}

    def set_app_data_limit(self, app_name, allow_data=True):
        self.restricted_apps[app_name] = allow_data
        print(f"[DataControl] Policy updated for {app_name}: Data Access -> {allow_data}")

    def inspect_traffic(self, app_name, data_packet_size):
        if not self.restricted_apps.get(app_name, True):
            print(f"[DataControl] BLOCKED data packet for restricted app: {app_name}")
            return False
        print(f"[DataControl] ALLOWED {data_packet_size} bytes for {app_name}")
        return True

if __name__ == "__main__":
    controller = AppDataControlModule()
    controller.set_app_data_limit("UnwantedAdApp", False)

# ==============================================================================
# MODULE: Split Tunneling & App Data Traffic Control
# ==============================================================================
import json

class SplitTunnelingDataControl:
    def __init__(self, policy_file="split_config.json"):
        self.policy_file = policy_file
        self.routed_apps = {}
        self.initialize_tunnel_policy()

    def initialize_tunnel_policy(self):
        print("[SplitTunnel] Initializing split tunneling and data control rules...")
        # Default policy: bypass unwanted apps, route specific data
        self.routed_apps = {
            "VPN_Bypass_Apps": [],
            "Blocked_Background_Data": ["UnwantedAdApp", "HeavyLogger"],
            "Split_Mode_Active": True
        }

    def set_split_rule(self, app_name, route_through_vpn=True):
        self.routed_apps[app_name] = route_through_vpn
        print(f"[SplitTunnel] Rule updated for '{app_name}': VPN Route -> {route_through_vpn}")

    def evaluate_packet_routing(self, app_name, packet_size):
        if app_name in self.routed_apps.get("Blocked_Background_Data", []):
            print(f"[DataControl] Blocked data transfer for restricted app: {app_name}")
            return False
        
        is_routed = self.routed_apps.get(app_name, True)
        print(f"[DataControl] Routed {packet_size} bytes for {app_name} (VPN: {is_routed})")
        return True

if __name__ == "__main__":
    tunnel_controller = SplitTunnelingDataControl()
    tunnel_controller.set_split_rule("TargetApp", True)
