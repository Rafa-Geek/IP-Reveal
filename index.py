from flask import Flask, render_template
import socket
import requests

ip_local = socket.gethostbyname(socket.gethostname())
ip_publico = requests.get('https://api.ipify.org/').text

app = Flask(__name__)

@app.route('/my-ip')
def showIp():
    return render_template('showIp.html', ip_local = ip_local, ip_publico = ip_publico)

@app.route('/password-generator')
def generatePassword():
    return render_template('generatePassword.html')

app.run(debug=True)