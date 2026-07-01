import os
import random
import logging
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# -----------------------------
# Render Health Server
# -----------------------------

def health_server():
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print(f"Health server running on {port}")
    server.serve_forever()


# -----------------------------
# Reply Database
# -----------------------------

RESPONSES = {
    "greeting": [
        "Hey 👋",
        "Hello!",
        "Yo 😎",
        "What's up?",
        "Hi there!",
        "Welcome back.",
        "Good to see you.",
        "Talk to me.",
    ],

    "morning": [
        "Good morning ☀️",
        "Rise and shine.",
        "Hope today treats you well.",
        "Morning! What's the plan?",
    ],

    "night": [
        "Good night 🌙",
        "Sleep well.",
        "Take care.",
        "Rest up.",
    ],

    "thanks": [
        "You're welcome 😊",
        "Happy to help.",
        "Anytime!",
        "My pleasure.",
        "Glad I could help.",
    ],

    "howareyou": [
        "Doing great 😄",
        "Running perfectly.",
        "Feeling awesome.",
        "Always ready.",
    ],

    "work": [
        "Tell me more about the project.",
        "Sounds interesting.",
        "Let's build something awesome.",
        "What's the goal?",
    ],

    "price": [
        "Depends on the project.",
        "Let's discuss the requirements first.",
        "Every project is different.",
        "Tell me the scope.",
    ],

    "help": [
        "Describe the issue.",
        "Paste the error.",
        "Let's solve it together.",
        "I'm listening.",
    ],

    "laugh": [
        "😂",
        "Haha.",
        "🤣 Good one.",
        "Nice 😂",
    ],

    "compliment": [
        "Thanks 😄",
        "Appreciate it.",
        "Means a lot.",
        "You're awesome too.",
    ],

    "bye": [
        "See you 👋",
        "Take care.",
        "Catch you later.",
        "Have a great day.",
    ],

    "yes": [
        "Awesome.",
        "Great.",
        "Perfect.",
        "Sounds good.",
    ],

    "no": [
        "No problem.",
        "Fair enough.",
        "Understood.",
        "Alright.",
    ],

    "coding": [
        "Send me the code.",
        "Paste the error message.",
        "Let's debug it.",
        "Show me what's happening.",
    ],

    "bot": [
        "Yep 🤖",
        "I'm a Telegram bot.",
        "Built to help.",
        "Always online.",
    ],

    "busy": [
        "I'll reply as soon as I can.",
        "Currently busy but your message is noted.",
        "Working on something at the moment.",
    ],

    "fallback": [
        "Got it 👍",
        "Thanks for your message.",
        "Interesting.",
        "Tell me more.",
        "I'm listening.",
        "Message received.",
        "I'll get back to you soon.",
    ]
}


KEYWORDS = {
    "greeting": [
        "hi", "hello", "hey", "yo", "sup",
        "hola", "namaste"
    ],

    "morning": [
        "good morning",
        "gm"
    ],

    "night": [
        "good night",
        "gn"
    ],

    "thanks": [
        "thanks",
        "thank",
        "thx",
        "ty",
        "tysm"
    ],

    "howareyou": [
        "how are you",
        "how r u",
        "how's it going",
        "hows it going"
    ],

    "work": [
        "project",
        "website",
        "app",
        "developer",
        "work",
        "hire",
        "portfolio"
    ],

    "price": [
        "price",
        "cost",
        "budget",
        "fee",
        "charge",
        "rate",
        "how much"
    ],

    "help": [
        "help",
        "issue",
        "problem",
        "bug",
        "broken",
        "error",
        "fix"
    ],

    "laugh": [
        "lol",
        "haha",
        "lmao",
        "rofl",
        "xd"
    ],

    "compliment": [
        "awesome",
        "great",
        "amazing",
        "nice",
        "cool",
        "smart",
        "genius"
    ],

    "bye": [
        "bye",
        "goodbye",
        "see you",
        "cya"
    ],

    "yes": [
        "yes",
        "yeah",
        "yup"
    ],

    "no": [
        "no",
        "nah",
        "nope"
    ],

    "coding": [
        "python",
        "java",
        "javascript",
        "html",
        "css",
        "sql",
        "code",
        "coding"
    ],

    "bot": [
        "are you a bot",
        "who made you",
        "who are you"
    ],

    "busy": [
        "busy",
        "available",
        "free",
        "active"
    ]
}


def get_reply(text):
    text = text.lower()

    for category, words in KEYWORDS.items():
        for word in words:
            if word in text:
                return random.choice(RESPONSES[category])

    return random.choice(RESPONSES["fallback"])


# -----------------------------
# Telegram Handler
# -----------------------------

async def business_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.business_message:
        return

    msg = update.business_message

    if not msg.text:
        return

    reply = get_reply(msg.text)

    await context.bot.send_message(
        chat_id=msg.chat.id,
        text=reply,
        business_connection_id=msg.business_connection_id,
    )


# -----------------------------
# Main
# -----------------------------

def main():

    threading.Thread(
        target=health_server,
        daemon=True
    ).start()

    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.UpdateType.BUSINESS_MESSAGE,
            business_reply
        )
    )

    print("Bot is running...")

    app.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()