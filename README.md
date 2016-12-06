# twitterTelegramBridge
Allows to send tweets from twitter to telegram using regular expressions to match tweets.

## Installing
This tool is written for Python 3.
Just clone this repo and make sure you have installed `python-telegram-bot` and `python-twitter`.
You can install these by using `pip install python-telegram-bot python-twitter`.

Now you can copy the file `config.py.example` to `config.py` and edit the values as needed.
Twitter consumer key and access token and secret must be generated at twitters website.

The Telegram bot token can be created by talking to https://telegram.me/BotFather.
Once you start a chat with your telegram bot, you can use `showChats.py` to list your latest updates
with their chat id, which must be inserted into the config aswell.

The `TWITTER_TARGET_USER` is the twitter account to search, it should start with an @.
The `TWEET_REGEX` can be used to filter tweets, something like `"#hashtag"` will only allow tweets
that contain #hashtag.

`ID_SET` is the name of a plaintext file used to store the IDs of already seen tweets.

After you configured everything in the config file, you can run the tool with `python main.py`.

To automate the script, create a cronjob for it, remember to set the working directory in the crontab entry.
