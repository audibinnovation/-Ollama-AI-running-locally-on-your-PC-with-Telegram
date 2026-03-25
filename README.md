# Ollama Telegram Bot

A simple Telegram bot that connects to your locally running [Ollama](https://ollama.com) instance and uses the **Qwen:7B-Chat-v1.5-q6_K** model (or any other Ollama model you choose) to generate AI responses.

---

## 🚀 Features
- Runs on **Windows** with Python.
- Connects Telegram messages directly to Ollama’s local API.
- Streams responses from Ollama back to Telegram.
- Easy to swap models (default: `qwen:7b-chat-v1.5-q6_K`).

---

## 📦 Requirements
- Windows PC
- [Ollama](https://ollama.com) installed and running
- Python 3.10+
- Telegram bot token (from [BotFather](https://core.telegram.org/bots#botfather))

---

## 🔧 Installation

1. **Install Ollama**  
   Download and install Ollama for Windows.  
   Test it with:
   ```powershell
   ollama run qwen:7b-chat-v1.5-q6_K
