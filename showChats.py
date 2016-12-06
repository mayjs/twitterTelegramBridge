import telegram
import config

bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
print('\n'.join(set(["%s %s: Chat-ID %d"%(update.message.from_user.first_name,update.message.from_user.last_name,update.message.chat.id) for update in bot.getUpdates()])))

