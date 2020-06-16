from pymongo import MongoClient
import bcrypt

class dbModel:
    
    def __init__(self):
        self.client = MongoClient("")
        self.cred_db = self.client.credentials
        self.endUserCollection = self.cred_db.endUser

        self.aadhaar_data = self.client.aadaar_data
        self.data = self.aadhaar_data.a_data

    #def insert_one(self, aadhaar, pwd): 
    #    if aadhaar is None:
    #        return 3
#
    #    if pwd is None:
    #        return 0
#
    #    cred = self.endUserCollection.find_one({"aadhaar" : aadhaar})
#
    #    if cred is not None:
    #        if bcrypt.checkpw(pwd.encode(), cred.get("password")) :
    #            return 1 #correct pwd
#
    #        else:
    #            return 0 #faltu pwd
#
    #    else :
    #        self.get_one_detail(aadhaar, pwd)
#
    #def get_one_detail(self, aadhar, pwd):  
    #    if aadhar is None:
    #        return 3 
    #    
    #    if pwd is None:
    #        return 2 
#
    #    cred = self.data.find_one({"aadaar_no" : aadhar})
#
    #    if cred is not None: 
    #        hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())    
#
    #        end_user_details = {
    #            "aadhaar" : aadhar,
    #            "password" : hashed
    #        }
    #        
    #        self.endUserCollection.insert(end_user_details)
    #        return 1
    #    else :
    #        return 3 #user not found
#
    #def hybrid_insert(self, ad, pwd):
    #    cred = self.endUserCollection.find_one({"aadhaar" : ad})
    #    if cred is None:
    #        cred = self.data.find_one({"aadaar_no" : ad})
    #        if cred is not None: 
    #            hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())    
#
    #            end_user_details = {
    #                "aadhaar" : ad,
    #                "password" : hashed
    #            }
    #        
    #            self.endUserCollection.insert(end_user_details)
    #            return 0#user added
    #        else:
    #            return 3#adhar not exist
    #    else: 
    #        if bcrypt.checkpw(pwd.encode(), cred.get("password")) :
    #            return 1 #correct pwd
    #        else:
    #            return 2#faltu pwd    


    def insertOne(self, ad, pwd):
        credOurDb = self.endUserCollection.find_one({"aadhaar" : ad})
        credGlobal = self.data.find_one({"aadaar_no" : ad})

        if credOurDb is not None and credGlobal is not None:
            if bcrypt.checkpw(pwd.encode(), credOurDb.get("password")) :
                return 1 #correct pwd
            else:
                return 2#faltu pwd 
        elif credGlobal is not None and credOurDb is None:
            hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())    

            end_user_details = {
                "aadhaar" : ad,
                "password" : hashed
            }
        
            self.endUserCollection.insert(end_user_details)
            return 0#user added
        else :
            return 3 #adhar not exist


    def connected(self):
        print('connected')
