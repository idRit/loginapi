from databaseconnector.databaseModel import dbModel
from flask import Flask, url_for, request, json, Response, jsonify
from flask_cors import CORS, cross_origin

interactor = dbModel()
interactor.connected()

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def index():
    return 'kuchtoh'#jsonify({"Connected" : "Connected"})

@app.route("/api/insertEndUser", methods = ['POST'])
def insertEndUser():
    res = json.dumps(request.json)
    resDict = json.loads(res)

    aadhaar = resDict.get("aadhaar")
    password = resDict.get("password")

    error = interactor.insert_one(aadhaar, password)

    if error == 1:
        return jsonify({"notify" : "no error"})
    elif error == 0:
        print('password is wrong')
        return jsonify({"notify" : "faltu pwd"})
    elif error == 3:
        return jsonify({"notify" : "aadhaar does not exists"})
    elif error == 2:
        return jsonify({"notify" : "password does not exists"})
    else :
        return jsonify({"notify" : "error"})

@app.route("/api/checkUser", methods = ['POST'])
def checkUser():
    res = json.dumps(request.json)
    resDict = json.loads(res)

    aadhaar = resDict.get("aadhaar")
    password = resDict.get("password")

    error = interactor.get_one_detail(aadhaar, password)

    if error == 1:
        return jsonify({"notify" : "1"})
    elif error == 0:
        return jsonify({"notify" : "0"})
    elif error == 3:
        return jsonify({"notify" : "aadhaar does not exists"})


if __name__ == '__main__':
    app.run()