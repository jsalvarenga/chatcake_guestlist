import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(
    'chatcake-development-firebase-adminsdk-ltyy0-3494f26fc3.json'
)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatcake-development.firebaseio.com/'
})

root = db.reference()
