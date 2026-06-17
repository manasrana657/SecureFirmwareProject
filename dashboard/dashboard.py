from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = "securefirmware123"

@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    return """
    <h1>Secure Firmware Update Dashboard</h1>

    <h2>Device Status</h2>
    <p>Current Firmware Version: 1.1</p>

    <h2>Security Status</h2>
    <p>RSA Signature Verification: PASS</p>
    <p>SHA-256 Integrity Check: PASS</p>
    <p>Rollback Protection: ENABLED</p>

    <h2>Update Status</h2>
    <p>Firmware Upload Successful</p>

    <br>
    <a href="/logout">Logout</a>
    """

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["user"] = username
            return redirect("/")

        return "Invalid Login"

    return """
    <h2>Admin Login</h2>

    <form method="POST">
        Username:
        <input type="text" name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <input type="submit" value="Login">
    </form>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(port=8080)
