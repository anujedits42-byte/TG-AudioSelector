from flask import Flask
import threading
import os
import asyncio

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Running 🚀"

def run_bot():
    from main import main

    try:
        # ✅ Fix asyncio error (VERY IMPORTANT)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        main()
    except Exception as e:
        print(f"Bot Error: {e}")

# ✅ Thread ko yahin start karo (Gunicorn ke liye best)
threading.Thread(target=run_bot, daemon=True).start()

# ✅ Port setup (Render fix)
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
