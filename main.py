import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

async def reply_like_a_boss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.business_message:
        msg = update.business_message
        text = msg.text.lower().strip()
        
        # 1. Greetings & Pleasantries
        if any(word in text for word in ["hi", "hello", "hey", "yo", "sup", "whatsapp", "greetings"]):
            reply = "Yo. Talk to me. 🗿"
        elif "good morning" in text:
            reply = "Up early, securing the bag. What's the move? 🌅"
        elif "good night" in text or "bye" in text or "tc" in text:
            reply = "Rest up. We grind again tomorrow. 🔋"
            
        # 2. Status & Availability
        elif any(word in text for word in ["where are you", "u free", "busy", "available", "active"]):
            reply = "Currently locked in and executing. Leave your brief, I'll review it. 📈"
        elif any(word in text for word in ["how are you", "how r u", "hows it going", "wbu"]):
            reply = "Never better. Focused, blessed, and making moves. ⚡"
            
        # 3. Work, Business, & Commercials
        elif any(word in text for word in ["price", "cost", "how much", "rate", "fee", "charge", "buy"]):
            reply = "We secure the bag first. Let's talk numbers—what value are we creating? 💼"
        elif any(word in text for word in ["work", "project", "website", "code", "portfolio", "hire"]):
            reply = "I build things that scale. Drop the project scope, let's see if we match. 🛠️"
        elif any(word in text for word in ["free", "discount", "cheap"]):
            reply = "High standards require high value. No shortcuts here. ❌"

        # 4. Troubleshooting & Support
        elif any(word in text for word in ["help", "error", "issue", "bug", "broken", "not working", "stuck"]):
            reply = "We don't panic. Clear your mind, explain the issue, and we fix it. 🛠️"

        # 5. Casual Chit-Chat & Feedback
        elif any(word in text for word in ["thank", "thx", "tysm", "cool", "nice", "awesome", "great"]):
            reply = "Just standard protocol. Appreciate the energy. 🤝"
        elif any(word in text for word in ["lol", "haha", "xd", "lmao"]):
            reply = "Life's a game, you gotta laugh at it. ⚡"
        elif any(word in text for word in ["ok", "okay", "kk", "got it", "fine", "sure"]):
            reply = "Understood. Let's keep it moving. 🏎️💨"
        elif any(word in text for word in ["yes", "yeah", "yup"]):
            reply = "Exactly. Correct mindset. 👑"
        elif any(word in text for word in ["no", "nah", "nope"]):
            reply = "Fair enough. Respect the boundaries. 🛑"

        # 6. Ultimate Catch-All (For everything else)
        else:
            reply = "Got your text. Busy building. I'll get back to you when I'm free. Keep grinding. 🏎️💨"

        # Send the boss response
        await context.bot.send_message(
            chat_id=msg.chat.id,
            text=reply,
            business_connection_id=msg.business_connection_id
        )

def main():
    TOKEN = os.getenv("8600838156:AAFhjcEiT-_IzQ2VvvySF73ba5sVrrsUOmQ")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.BUSINESS_MESSAGE, reply_like_a_boss))
    print("Mega Chad Bot is ready...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
if __name__ == '__main__':
    main()
