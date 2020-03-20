from chatcake_client import Command
from guestlist.helpers import show


class Out(Command):

    keys = ['#out', '#ausente']

    @staticmethod
    def call(database, request):
        ref = database.child(request['group_id'])
        author = request['author']

        if ref.child('title').get():

            # remove author from will-show list
            ref.child(''.join(['will-show/', str(author)])).delete()

            # add author to wont-show list
            ref.child('wont-show').update({
                author: {".sv": "timestamp"}
            })

            return [show(database, request['group_id'])]

        else:
            raise KeyError
