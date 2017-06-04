import praw

reddit = praw.Reddit(client_id='your_id',
                     client_secret='your_client_secret_key',
                     password='your_user_password',
                     username='your_user_name',
                     user_agent = "Reddit Bot for watching titles")

addme = ['!add']
removeme = ['!remove']

def friend_bot():
    while True:
        for item in reddit.inbox.unread(limit=None):
            message = item.body.lower()
            addmatches = any(string in message for string in addme)
            removematches = any(string in message for string in removeme)
            if addmatches:
                if item.author.is_friend is False:
                    item.author.friend()
                    item.reply('You have been subscribed to soccerthreadbot. I will inform you if a new Match Thread appears.' + '\n\n' + 'If you want to unsubscribe, reply with the message "!remove".')
                    item.mark_read()
                else:
                    item.reply('You are already subscribed to soccerthreadbot.' + '\n\n' + 'If you want to unsubscribe, reply with the message "!remove".')
                    item.mark_read()
            elif removematches:
                if item.author.is_friend is True:
                    item.author.unfriend()
                    item.reply('You have been unsubscribed from soccerthreadbot.' + '\n\n' + 'No more Match Threads for you.')
                    item.mark_read()
                else:
                    item.reply('You are not currently subscribed to soccerthreadbot.' + '\n\n' + 'If you want to subscribe, reply with the message "!add".')
                    item.mark_read()
            else:
                item.reply('I am a bot, monitoring /r/soccer for Match Thread.' + '\n\n' + 'If you want to subscribe, reply to this PM with the message "!add".')
                item.mark_read()