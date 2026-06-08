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

<style>
body{
    background:#121212;
    color:white;
    font-family:Arial,sans-serif;
    display:flex;
    justify-content:center;
    margin:0;
}

.container{
    width:800px;
    margin-top:30px;
}

h1{
    text-align:center;
}

.chat-box{
    background:#1e1e1e;
    border-radius:10px;
    padding:20px;
    min-height:400px;
}

.user{
    color:#4ea1ff;
}

.bot{
    color:#00ff99;
}

input{
    width:75%;
    padding:12px;
    background:#2b2b2b;
    color:white;
    border:none;
    border-radius:5px;
}

button{
    padding:12px;
    background:#00ff99;
    border:none;
    border-radius:5px;
    cursor:pointer;
}
</style>

</head>
<body>

<div class="container">

<h1>🤖 Basic Web Chatbot</h1>

<div class="chat-box">

{% for chat in chat_history %}
<p class="user"><b>You:</b> {{ chat.user }}</p>
<p class="bot"><b>AI:</b> {{ chat.bot }}</p>
<hr>
{% endfor %}

</div>

<br>

<form method="POST">
<input
type="text"
name="message"
placeholder="Type your message..."
autofocus>

<button type="submit">Send</button>
</form>

</div>

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

    elif "good morning" in user_input:
        return "Good morning! ☀️"

    elif "good night" in user_input:
        return "Good night! 🌙"

    elif "who made you" in user_input:
        return "Berke created me 😎"

    elif "bye" in user_input:
        return "Goodbye!"

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
