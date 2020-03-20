from chatcake_client import Command
from guestlist.helpers import show


class Confirm(Command):

    keys = ['#confirm', '#confirmar', '#in', '#participar', '#dentro']

    @staticmethod
    def call(database, request):
        ref = database.child(request['group_id'])
        author = request['author']

        if ref.child('title').get() is not None:

            # remove author from wont-show list
            ref.child(''.join(['wont-show/', str(author)])).delete()

            # add author to wont-show list
            ref.child('will-show').update({
                author: {".sv": "timestamp"}
            })
            return [show(database, request['group_id'])]
        else:
            raise KeyError
