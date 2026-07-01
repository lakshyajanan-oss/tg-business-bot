import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

async def reply_like_a_boss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.business_message:
        msg = update.business_message
        text = msg.text.lower()
        
        # Chad response logic mapping
        if "hey" in text or "hello" in text or "hi" in text:
            reply = "Yo. Talk to me. 🗿"
        elif "price" in text or "cost" in text or "buy" in text:
            reply = "We secure the bag first. Let's talk numbers. 💼"
        elif "help" in text:
            reply = "We don't panic. What's the issue? ⚡"
        else:
            reply = "Got your text. Busy building. I'll get back to you when I'm free. Keep grinding. 🏎️💨"

        await context.bot.send_message(
            chat_id=msg.chat.id,
            text=reply,
            business_connection_id=msg.business_connection_id
        )

def main():
    # Render automatically provides a PORT environment variable, keeping the bot alive via a web hook or simple loop
    TOKEN = os.getenv("BOT_TOKEN")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.BUSINESS_MESSAGE, reply_like_a_boss))
    print("Chad Bot is live...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
