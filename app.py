from flask import Flask
import socket

app = Flask (__name__)

@app.route ('/')
def home():
    hostname = socket.gethostname()
    print(hostname)
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    return f'Hello World @{ip_address}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)