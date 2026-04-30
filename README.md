# Gemini CLI Chatbot

A simple stateful command-line chatbot powered by Google's Gemini 2.5 Flash model. Chat with an AI directly from your terminal with full conversation memory.

---

## Prerequisites

- Python 3.8+
- A [Google AI Studio](https://aistudio.google.com/) account with a Gemini API key

---

## Project Structure

```
week1-2-cli/
├── main.py          # Main chatbot script
├── .env             # Your API key (not committed to git)

```

---

## Setup

### 1. Clone the repository

```bash
git clone (https://github.com/binu59/cli-chat-bot.git)
cd week1-2-cli
```

### 2. Set up your API key

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

> Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Usage

```bash
python main.py
```

Once running, just type your message and hit Enter. The bot will respond instantly.

```
Chatbot ready! Type 'quit' to exit.

You: Hello! Who are you?
Bot: I'm a helpful AI assistant powered by Google Gemini. How can I help you today?

You: quit
Goodbye!
```

To exit, type `quit` or `exit`.

---


## Dependencies

| Package | Purpose |
|---|---|
| `google-genai` | Official Gemini Python SDK |
| `python-dotenv` | Load API key from `.env` file |

Install all at once:

```bash
pip install google-genai python-dotenv
```



```
google-genai
python-dotenv
``

## Known Limitations

- Conversation history is stored **in memory only** - it resets when you restart the script
- No support for multi-turn file or image input in this version
- Error handling exits the loop on first failure - consider adding retry logic for production use

---

## License

MIT License - free to use and modify.
