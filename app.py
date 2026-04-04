from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Running 🚀"

def run_bot():
    from main import main
    main()

if __name__ == "__main__":
    t = threading.Thread(target=run_bot, daemon=True)
    t.start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
