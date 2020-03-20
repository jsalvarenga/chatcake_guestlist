from chatcake_client import Command
from guestlist.helpers import show


class Show(Command):

    keys = ['#show', '#mostrar']

    @staticmethod
    def call(database, request):
        return [show(database, request['group_id'])]
