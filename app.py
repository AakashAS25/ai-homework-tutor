from flask import Flask, render_template, request, session, redirect, url_for
from ai.tutor import get_tutor_response

app = Flask(__name__)
app.secret_key = "super-secret-key"  # needed for Flask session

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        question = request.form["question"]
        answer = get_tutor_response(question)

        session["chat_history"].append({"role": "user", "text": question})
        session["chat_history"].append({"role": "ai", "text": answer})
        session.modified = True

    return render_template("index.html", chat_history=session["chat_history"])


# Route to start a new chat session
@app.route("/new_chat", methods=["POST"])
def new_chat():
    session["chat_history"] = []
    session.modified = True
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)