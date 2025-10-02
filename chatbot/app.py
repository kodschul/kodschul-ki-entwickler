from flask import Flask, request, jsonify, send_from_directory
import openai
from config import OPENAI_API_KEY, OPENAI_MODEL
import os

app = Flask(__name__, static_folder="static")
openai.api_key = OPENAI_API_KEY

# Systemprompt laden
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.2
        )
        answer = response.choices[0].message.content
        if answer:
            answer = answer.strip()
        else:
            answer = "Entschuldigung, ich konnte keine Antwort generieren. Bitte wenden Sie sich an den Support oder das Wiki."
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "static"), "index.html")


if __name__ == "__main__":
    app.run(debug=True)
