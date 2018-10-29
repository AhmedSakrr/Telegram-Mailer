# -*- coding: utf-8 -*-

from pyrogram import Client

def Send_Message(user, text):
    print('Sending to: {}'.format(user), end='\r')
    app.send_message(user, text)

if __name__ == '__main__':
    print('Don`t use for spam!')

    users = open('users.txt').read().split('\n') or 'me'
    text = input('Text: ') or 'Test message.'

    app = Client("my_account")
    app.start()

    for user in users:
        Send_Message(user, text)

    app.stop()
