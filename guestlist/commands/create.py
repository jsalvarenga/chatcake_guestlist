from chatcake_client import Command
from guestlist.helpers import show


class Create(Command):

    keys = ['#create', '#new']

    @staticmethod
    def call(database, request):
        ref = database.child(request['group_id'])
        ref.set({
            'title': request['body'],
        })
        return [show(database, request['group_id'])]
