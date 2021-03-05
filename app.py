from flask import Flask, request, jsonify
import jwt
#setup

app=Flask(__name__)


#routes

#create

@app.route('/user', methods=['POST'])
def add_user():
    username=request.json['username']
    password=request.json['password']
    secstring=request.json['secstring']

    return jsonify(jwt.encode({'user':[{'username':username},{'password':password}]}, secstring))


#verify
@app.route('/user/<mytoken>/<mysecret>', methods=['GET'])
def verify(mytoken,mysecret):
    return jsonify(jwt.decode(mytoken,mysecret,algorithms="HS256"))


#run
if __name__ == '__main__':
    app.run(debug=True)
