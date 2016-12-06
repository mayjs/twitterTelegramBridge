import config
import twitter
import re
import telegram
import datetime
import os

def get_all_tweets(user=config.TWITTER_TARGET_USER):
	api = twitter.Api(consumer_key = config.TWITTER_CONSUMER_KEY,
						consumer_secret = config.TWITTER_CONSUMER_SECRET,
						access_token_key=config.TWITTER_ACCESS_TOKEN,
						access_token_secret = config.TWITTER_TOKEN_SECRET)
	return api.GetUserTimeline(screen_name=user)

def get_filtered_tweets(filter_function, user = config.TWITTER_TARGET_USER):
	return ( t for t in get_all_tweets(user) if filter_function(t) )

def load_set(file = config.ID_SET):
	try:
		with open(file, "r") as f:
			return set(line.strip() for line in f)
	except FileNotFoundError:
		return set()

def store_set(to_store, file = config.ID_SET):
	with open(file, "w") as f:
		for id in to_store:
			f.write("{}\n".format(id))

if __name__ == "__main__":
	tweets = get_filtered_tweets(filter_function = lambda t: re.search(config.TWEET_REGEX, t.text))
	bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
	timezone = datetime.timezone(datetime.timedelta(hours=1))
	id_set = load_set()
	for t in tweets:
		print("{}: {}".format(t.id, t.text))
		id_str = "{}".format(t.id)
		if not id_str in id_set:
			date = datetime.datetime.strptime(t.created_at, "%a %b %d %H:%M:%S %z %Y")
			date = date.astimezone(tz = timezone)
			bot.sendMessage(chat_id = config.TELEGRAM_CHAT_ID, text = "Am {0:%d.%m.%Y um %H:%M}:\n{1}".format(date, t.text))
			id_set.add(id_str)
	store_set(id_set)
