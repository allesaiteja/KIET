from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "Nerchuko"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = request.form['usr_name']
        session['user'] = user  # Store the username in the session
        return redirect(url_for("user"))
    else:
        if 'user' in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']  # Retrieve the username from the session
        return f"You are logged in as {user}!"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove the username from the session
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
