import random
import tkinter as tk

user_name = ""

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

    elif "hello" in user_input:
        responses = [
            "Hello 😄",
            "Hi there 👋",
            "Hey!",
            "Nice to see you 😎",
            "Hello human 🤖"
        ]
        return random.choice(responses)

    elif "how are you" in user_input:
        return "I'm fine 😄"

    elif "your name" in user_input:
        return "I'm BasicBot!"

    elif "good morning" in user_input:
        return "Good morning!"

    elif "good night" in user_input:
        return "Good night! 🌙"

    elif "who made you" in user_input:
        return "Berke created me 😎"

    elif "ai" in user_input:
        return "AI is the future 🤖"

    elif "machine learning" in user_input:
        return "Machine learning helps computers learn from data."

    elif "coding" in user_input:
        return "Coding gets easier with practice!"

    elif "sad" in user_input:
        return "I hope your day gets better ❤️"

    elif "happy" in user_input:
        return "That's great 😄"

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "I don't understand."

def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_message + "\n", "user")
    bot_response = get_bot_response(user_message)
    chat_box.insert(tk.END, "AI: " + bot_response + "\n\n", "bot")

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Basic Chatbot")
window.geometry("500x500")
window.configure(bg="#1e1e1e")

chat_box = tk.Text(window, height=25, width=60, bg="#121212", fg="white", insertbackground="white")
chat_box.tag_config("user", foreground="#4ea1ff")
chat_box.tag_config("bot", foreground="#00ff99")
chat_box.pack(pady=10)

entry = tk.Entry(window, width=45)
entry.pack(pady=5)

send_button = tk.Button(window, text="Send", command=send_message, bg="#3a3a3a", fg="white")
send_button.pack(pady=5)

entry.bind("<Return>", lambda event: send_message())


window.mainloop()