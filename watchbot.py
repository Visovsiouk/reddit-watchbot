import praw
from threading import Thread
from friendbot import friend_bot
from hintbot import hint_bot

if __name__ == "__main__":
    t1 = Thread(target = friend_bot)
    t2 = Thread(target = hint_bot)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass