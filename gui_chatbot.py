from flask import Flask, request, render_template_string
import random
import datetime

app = Flask(__name__)

user_name = ""
chat_history = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Basic Web Chatbot</title>
</head>
<body>

    <h1>Basic Web Chatbot</h1>

    <form method="POST">
        <input type="text" name="message" placeholder="Type your message" autofocus>
        <button type="submit">Send</button>
    </form>

    <hr>

    {% for chat in chat_history %}
        <p><b>You:</b> {{ chat.user }}</p>
        <p><b>AI:</b> {{ chat.bot }}</p>
        <hr>
    {% endfor %}

</body>
</html>
"""

def get_bot_response(user_input):
    global user_name
    user_input = user_input.lower()

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}"

    elif "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name}"
        else:
            return "I don't know your name yet."

    elif "what time is it" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time} ⏰"

    elif "hello" in user_input:
        responses = [
            "Hello 😄",
            "Hi there 👋",
            "Hey!",
            "Nice to see you 😎"
        ]
        return random.choice(responses)

    elif "how are you" in user_input:
        return "I'm fine 😄"

    elif "your name" in user_input:
        return "I'm BasicBot!"

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "I don't understand."

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        user_message = request.form["message"]
        bot_response = get_bot_response(user_message)

        chat_history.append({
            "user": user_message,
            "bot": bot_response
        })

    return render_template_string(
        HTML,
        chat_history=chat_history
    )

if __name__ == "__main__":
    app.run(debug=True)
