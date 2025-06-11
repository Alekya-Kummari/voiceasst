from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Voice AI Assistant is running!"

# Endpoint to receive calls from Vapi AI or Twilio
@app.route("/handle-call", methods=["POST"])
def handle_call():
    data = request.json
    user_input = data.get("user_input", "")
    
    # You can add logic or call OpenAI API here
    response_text = f"You said: {user_input}. Based on that, here is some career advice..."
    
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
