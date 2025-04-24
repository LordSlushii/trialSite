from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print("Username:", username)
        print("Password:", password)
        return f"Hello, {username}!"  # or redirect or render_template, etc.
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)