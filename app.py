from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Running 🚀"

# Bot ko run karne ke liye function
def run_bot():
    import bot  # yaha tera bot.py run hoga

if __name__ == "__main__":
    import os
    
    # Bot thread me run hoga
    t = threading.Thread(target=run_bot)
    t.start()
    
    # Flask server (IMPORTANT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
