import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

CONFIG_FILE = "router_chain_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"routers": [], "bridge_status": "Active", "active_router": None}

def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

class RemoteBridgeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Mi System - Remote Data Bridge</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body { font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }
                    .card { background: #1e293b; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
                    input, button { width: 100%; padding: 12px; margin: 8px 0; box-sizing: border-box; border-radius: 6px; border: none; font-size: 16px; }
                    input { background: #334155; color: #fff; }
                    button { background: #3b82f6; color: white; font-weight: bold; cursor: pointer; }
                    button.danger { background: #ef4444; }
                    button.success { background: #10b981; }
                </style>
            </head>
            <body>
                <h2>Mi System - রিমোট রাউটার ও ডেটা ব্রিজ প্যানেল</h2>
                
                <div class="card">
                    <h3>নতুন রাউটার বা ইন্টারনেট সোর্স যুক্ত করুন</h3>
                    <input type="text" id="router_name" placeholder="রাউটারের নাম (যেমন: বাসা / বাজার রাউটার)">
                    <input type="text" id="ssid" placeholder="Wi-Fi SSID / Network Name">
                    <input type="password" id="password" placeholder="Wi-Fi Password">
                    <button onclick="addRouter()">চেইনে যুক্ত করুন</button>
                </div>

                <div class="card">
                    <h3>সংযুক্ত রাউটার ও ইন্টারনেট সুইচিং লিস্ট</h3>
                    <div id="routerList">লোড হচ্ছে...</div>
                </div>

                <script>
                    function loadData() {
                        fetch('/api/get')
                            .then(res => res.json())
                            .then(data => {
                                let html = '';
                                if(data.routers.length === 0) {
                                    html = '<p>কোনো রাউটার বা নেটওয়ার্ক যুক্ত করা হয়নি।</p>';
                                } else {
                                    data.routers.forEach((r, index) => {
                                        let isSelected = (data.active_router === index);
                                        html += `<div style="border-bottom:1px solid #334155; padding:10px 0;">
                                            📡 <b>${r.name}</b> (${r.ssid}) <br>
                                            স্ট্যাটাস: ${isSelected ? '<span style="color:#10b981"><b>[সক্রিয় / Active Bridge]</b></span>' : 'সংযুক্ত'}
                                            <br><br>
                                            <button class="success" onclick="setActive(${index})">এই রাউটার থেকে ইন্টারনেট নিন</button>
                                            <button class="danger" onclick="removeRouter(${index})">রিমুভ করুন</button>
                                        </div>`;
                                    });
                                }
                                document.getElementById('routerList').innerHTML = html;
                            });
                    }

                    function addRouter() {
                        const name = document.getElementById('router_name').value;
                        const ssid = document.getElementById('ssid').value;
                        const password = document.getElementById('password').value;
                        if(!name || !ssid) { alert('রাউটারের নাম এবং SSID দিন!'); return; }
                        fetch('/api/add', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({name, ssid, password})
                        }).then(() => {
                            document.getElementById('router_name').value = '';
                            document.getElementById('ssid').value = '';
                            document.getElementById('password').value = '';
                            loadData();
                        });
                    }

                    function setActive(index) {
                        fetch('/api/set_active', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({index})
                        }).then(() => loadData());
                    }

                    function removeRouter(index) {
                        fetch('/api/remove', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({index})
                        }).then(() => loadData());
                    }

                    loadData();
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
            
        elif parsed.path == "/api/get":
            data = load_config()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(length).decode('utf-8'))
        data = load_config()
        
        if self.path == "/api/add":
            data["routers"].append({
                "name": body.get("name"), 
                "ssid": body.get("ssid"), 
                "password": body.get("password")
            })
            if len(data["routers"]) == 1:
                data["active_router"] = 0
            save_config(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"success"}')
            
        elif self.path == "/api/set_active":
            data["active_router"] = body.get("index")
            save_config(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"updated"}')
            
        elif self.path == "/api/remove":
            idx = body.get("index")
            if 0 <= idx < len(data["routers"]):
                data["routers"].pop(idx)
                if data["active_router"] == idx:
                    data["active_router"] = 0 if len(data["routers"]) > 0 else None
                elif data["active_router"] and data["active_router > idx"]:
                    data["active_router"] -= 1
                save_config(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status":"removed"}')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), RemoteBridgeServer)
    print(f"Cloud-Ready Bridge Server running on port {port}")
    try:
        server.serve_forever()
    except:
        pass
