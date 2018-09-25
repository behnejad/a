from flask import Flask
from flask import request
from json import dumps

app = Flask(__name__)

local_cert = ('cert.pem', 'key.pem')

clients = []


@app.route("/")
def hello():
    return "Hello from server!"

@app.route("/registerClient", methods=('POST', ))
def registerClient():
    clients.append({'addr': request.form['addr'], 'cert': request.files['client_cert'].read().decode('ascii')})
    return '{"id": "%d"}' % (len(clients))

@app.route('/getClients')
def getClients():
    return dumps(clients)


if __name__ == "__main__":
    # app.run(ssl_context='adhoc')
    app.run(port=5001, ssl_context=local_cert, debug=True)