import requests
import json
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

OLLAMA_URL = "http://localhost:11434/api/generate"
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

MODEL_NAME = "qwen:7b-chat-v1.5-q6_K"   # <-- your model

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # Send prompt to Ollama with streaming enabled
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL_NAME, "prompt": user_text},
        stream=True
    )

    reply_text = ""
    for line in response.iter_lines():
        if line:
            try:
                json_data = json.loads(line.decode("utf-8"))
                if "response" in json_data:
                    reply_text += json_data["response"]
            except Exception as e:
                print("Parse error:", e)

    if not reply_text.strip():
        reply_text = "⚠️ Ollama did not return a response."

    await update.message.reply_text(reply_text)

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
