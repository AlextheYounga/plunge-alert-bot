# plungeAlertBot

You will first need to set up a bot with the BotFather
https://core.telegram.org/bots
Once your bot is made and you have received your Telegram API key from the BotFather, you may create a file called key.py and insert your key with the syntax TOKEN="INSERT-TOKEN-HERE"

This bot runs with python 3.
To activate, run python3 -m plunge_alert_bot.watcher

This bot is activated when a Telegram user sends the command /start to your bot.
From there, the cron will check the price of a particular stock at whatever rate the user wishes, but it is currently set to every 10 seconds.
If the price falls below a certain point, the bot will send a message to the Telegram user and the program will turn itself off. 

The bot is currently set up with a random number generator to demonstrate functionality, simply uncomment the commented code in watcher.py to set up your desired price ranges. 