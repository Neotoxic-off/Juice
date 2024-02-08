from server.database.connect import Database

class Crud:
    def __init__(self):
        self.db = Database()
        self.connect_db = self.db.Connect()

        self.collection = self.connect_db["scrappers"]

    def insert_one(self, user):
        return self.collection.insert_one(user)

    def insert_many(self, array_user):
        return self.collection.insert_many(array_user)

    def update_user(self, user):
        return self.collection.update_one({"id": user["id"]}, user)

    def replace_user(self, user):
        return self.collection.replace_one({"id": user["id"]}, user)

    def delete_user(self, id):
        return self.collection.delete_one({"id": id})

    def find_user(self, user):
        return self.collection.find_one({"id": user["id"]})
    
    def get_user(self, username):
        return self.collection.find_one({"username": username})

    def count_collection(self):
        return self.collection.count_documents({})
