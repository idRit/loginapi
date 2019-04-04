from pymongo import MongoClient
import bcrypt

class dbModel:
    
    def __init__(self):
        self.client = MongoClient("mongodb+srv://red:blxgre369@cluster0-oaiys.mongodb.net/test?retryWrites=true")
        self.cred_db = self.client.credentials
        self.endUserCollection = self.cred_db.endUser

    def insert_one(self, aadhaar, pwd): 
        if aadhaar is None:
            return "Enter aadhar"

        if pwd is None:
            return "Enter pwd"

        hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())    

        end_user_details = {
            "aadhaar" : aadhaar,
            "password" : hashed
        }

        self.endUserCollection.insert(end_user_details)

    def get_one_detail(self, aadhar, pwd):  
        if aadhaar is None:
            return 3 
        
        if pwd is None:
            return 2 

        cred = self.endUserCollection.find_one({"aadhaar" : aadhar})

        if cred:
            if bcrypt.checkpw(cred.get("password"), pwd) :
                return 1 #correct pwd

            else:
                return 0 #faltu pwd
        else :
            return 3 #user not found

    def connected(self):
        print('connected')
