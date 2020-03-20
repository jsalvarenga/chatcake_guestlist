from chatcake_client import Bot

from guestlist.commands import Confirm, Create, Out, Show
from .firebase import root


class GuestList(Bot):
    def __init__(self):
        super(GuestList, self).__init__(
            topic='guestlist',
            firebase=root.child('apps/guestlist'),
            cmds=[
                Confirm,
                Create,
                Out,
                Show
            ]
        )

    def define_trigger(self, message):
        words = message['text'].split()
        return words[0]
