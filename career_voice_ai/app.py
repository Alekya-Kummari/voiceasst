from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Voice AI Assistant is running!"

@app.route("/handle-call", methods=["POST"])
def handle_call():
    data = request.json
    user_input = data.get("user_input", "")
    response_text = f"You said: {user_input}. Based on that, here is some career advice..."
    return jsonify({"response": response_text})

# ✅ NEW ROUTE for Vapi
@app.route("/vapi", methods=["POST"])
def vapi_handler():
    data = request.json
    user_input = data.get("user_input", "")
    response_text = f"You said: {user_input}. Based on that, here is some career advice..."
    return jsonify({
        "type": "talk",
        "message": response_text
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
