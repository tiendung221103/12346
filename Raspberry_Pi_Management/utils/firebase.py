import firebase_admin 
from firebase_admin import credentials, db

class Firebase:
    def __init__(self):
        # Initialize the Firebase app with the provided credentials and database URL
        cred = credentials.Certificate("/home/asus/Desktop/Raspberry_Pi_Management/models/smart-home-8f1e8-firebase-adminsdk-fbsvc-2b93094056.json")
        firebase_admin.initialize_app(cred, {'databaseURL': "https://smart-home-8f1e8-default-rtdb.firebaseio.com/"})
        self.db = db

    def get_data(self, path):
        # Retrieve data from the specified path in the Firebase Realtime Database
        ref = self.db.reference(path)
        return ref.get()

    def set_data(self, path, data):
        # Set data at the specified path in the Firebase Realtime Database
        ref = self.db.reference(path)
        ref.set(data)
    def listen_to_data(self, path, callback):
        # Listen for real-time updates at the specified path
        ref = self.db.reference(path)
        ref.listen(callback)
        

