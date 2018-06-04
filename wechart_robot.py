#!/usr/bin/python

import wxpy
from design_patterns import singleton
import re


class WXUser:
    def __init__(self, user):
        self.user = user

    @property
    def nick_name(self):
        return self.user.nick_name

    @property
    def puid(self):
        return self.user.puid


class WXGroup:
    def __init__(self, gruop):
        self.group = gruop


@singleton
class WXRobot:
    def __init__(self):
        self.bot = wxpy.Bot()
        self.bot.enable_puid()
        self.users = dict()
        self.groups = dict()

    def get_user(self, puid):
        if puid in self.users:
            return self.users[puid]
        return None

    def get_group(self, puid):
        if puid in self.groups:
            return self.groups[puid]
        return None

    def listen_group_message(self, callback_func):
        @self.bot.register(wxpy.Group, wxpy.TEXT, except_self=False)
        def process_group_message(msg):
            if msg.member.puid not in self.users:
                self.users[msg.member.puid] = WXUser(msg.member)
            if msg.chat.puid not in self.groups:
                self.groups[msg.chat.puid] = WXGroup(msg.chat)
            if msg.is_at:
                index = re.search(r"[ \u2005]", msg.text).span()[1]
                callback_func(True, msg.text[index:], msg.member.puid)
            else:
                callback_func(False, msg.text, msg.member.puid)


if "__main__" == __name__:
    rob = WXRobot()

    def callback(is_at, content, puid):
        print(is_at, content, puid)

    rob = rob.listen_group_message(callback)
