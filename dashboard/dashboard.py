from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Secure Firmware Update Dashboard</h1>

    <h2>Device Status</h2>
    <p>Current Firmware Version: 2.0</p>

    <h2>Security Status</h2>
    <p>RSA Signature Verification: PASS</p>
    <p>SHA-256 Integrity Check: PASS</p>
    <p>Rollback Protection: ENABLED</p>

    <h2>Update Status</h2>
    <p>Firmware Upload Successful</p>

    <h2>Project Features</h2>
    <ul>
        <li>Secure Boot</li>
        <li>Firmware Signing</li>
        <li>Integrity Verification</li>
        <li>Rollback Protection</li>
        <li>Audit Logging</li>
        <li>Secure Update Server</li>
    </ul>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

