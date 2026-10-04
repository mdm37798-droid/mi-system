from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MI System - Supreme App Dashboard</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: monospace; padding: 15px; margin: 0; }
        h1 { color: #f0f6fc; font-size: 20px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
        .card { background: #161b22; border: 1px solid #30363d; padding: 12px; border-radius: 8px; margin-top: 15px; }
        .status { color: #3fb950; font-weight: bold; }
        button { background: #238636; color: white; border: none; padding: 10px 15px; border-radius: 6px; font-family: monospace; cursor: pointer; margin-top: 10px; width: 100%; }
        #output { margin-top: 10px; color: #ffa657; }
    </style>
</head>
<body>
    <h1>⚡ [M I System v3.0] ড্যাশবোর্ড</h1>
    <div class="card">
        <p>সিস্টেম স্ট্যাটাস: <span class="status">Operational & Secure</span></p>
        <p>কমান্ডার: <b>এম কমান্ড (মিজান)</b></p>
        <p>অবস্থান: তিলাকপুর পুরাতন বাজার, রাজশাহী</p>
    </div>
    <div class="card">
        <h3>কমান্ড ও ডায়াগনস্টিকস</h3>
        <button onclick="runDiagnostics()">হেলথ চেক ও ডায়াগনস্টিকস</button>
        <div id="output"></div>
    </div>
<script>
function runDiagnostics() {
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerHTML = `[Diagnostics]: ${data.status} | টাইমস্ট্যাম্প: ${data.timestamp}`;
        });
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/status')
def api_status():
    return jsonify({
        "status": "Operational & Secure",
        "commander": "এম কমান্ড (মিজান)",
        "timestamp": "2026-10-02"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
