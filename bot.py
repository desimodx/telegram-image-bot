from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import requests

BOT_TOKEN = "7898119257:AAGJUe7U-H0NYnvvftDZ1-nhbmoi8Rgo3Gs"

CHANNELS = ["apktitann","apktitann","apktitann","vipbrancho","apktitann"]

async def is_user_joined(bot, user_id):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(f"@{channel}", user_id)
            if member.status in ["left","kicked"]:
                return False
        except:
            return False
    return True

async def join_screen(update, context):
    buttons = []
    for ch in CHANNELS:
        buttons.append([InlineKeyboardButton(f"Join @{ch}", url=f"https://t.me/{ch}")])
    buttons.append([InlineKeyboardButton("✅ Joined", callback_data="check_join")])
    await update.message.reply_text(
        "🔒 Bot use karne ke liye pehle sab channels join karo:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joined = await is_user_joined(context.bot, update.effective_user.id)
    if not joined:
        await join_screen(update, context)
        return
    await update.message.reply_text("🎨 Prompt bhejo image generate karne ke liye")

async def check_join_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    joined = await is_user_joined(context.bot, query.from_user.id)
    if joined:
        await query.edit_message_text("✅ Verified! Ab prompt bhejo.")
    else:
        await query.answer("❌ Abhi bhi join nahi kiya!", show_alert=True)

async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joined = await is_user_joined(context.bot, update.effective_user.id)
    if not joined:
        await join_screen(update, context)
        return
    prompt = update.message.text
    img_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    await update.message.reply_photo(img_url, caption="🖼 Generated Image")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_join_callback, pattern="check_join"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))
    app.run_polling()

if __name__ == "__main__":
    main()    query = update.callback_query
    await query.answer()
    joined = await is_user_joined(context.bot, query.from_user.id)
    if joined:
        await query.edit_message_text("✅ Verified! Ab prompt bhejo.")
    else:
        await query.answer("❌ Abhi bhi join nahi kiya!", show_alert=True)

async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joined = await is_user_joined(context.bot, update.effective_user.id)
    if not joined:
        await join_screen(update, context)
        return
    prompt = update.message.text
    img_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    await update.message.reply_photo(img_url, caption="🖼 Generated Image")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_join_callback, pattern="check_join"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))
    app.run_polling()

if __name__ == "__main__":
    main()
