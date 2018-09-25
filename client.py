from flask import Flask
from os import popen
from requests import Session, post
from adaptor import ForcedIPHTTPSAdapter
from json import loads

from requestutils import makeRequest

# def checkName(cert, hostname):
#     print(cert)
#     print(hostname)
#     return True
#
# import ssl
# # ssl.match_hostname = lambda cert, hostname: True
# ssl.match_hostname = checkName

local_cert = ('cert2.pem', 'key2.pem')

server_addr = ('https://server.com:5001', 'https://127.0.0.1:5001', 'server.com', '127.0.0.1')
server_cert = "cert.pem"
server_api = {
    'register': {
        'url': '/registerClient',
        'method': 'post'
    }
}

app = Flask(__name__)

client_id = 0

@app.route("/")
def hello():
    return "Hello from client!"


@app.route("/getKernelInfo")
def getKernelInfo():
    return popen('uname -a').read()

@app.route('/shellCommand/<path:command>')
def executeShellCommand(command: str):
    return popen(command).read()


if __name__ == "__main__":
    # session = Session()
    # session.mount(server_addr[0] + server_api['register']['url'], ForcedIPHTTPSAdapter(dest_ip=server_addr[3]))
    response = post(server_addr[1] + server_api['register']['url'],
                    headers={'Host': server_addr[2]},
                    data={'addr': '127.0.0.1:5000'},
                    files=[('client_cert', ('cert.pem', open(local_cert[0], 'rb'), 'text/plain')), ],
                    verify=False)
    if response.status_code == 200:
        client_id = loads(response.text)['id']
        print(client_id)

    # app.run(ssl_context='adhoc')
    app.run(ssl_context=local_cert, debug=True)


