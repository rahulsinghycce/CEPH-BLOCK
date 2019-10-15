#!/usr/bin/python

from flask import Flask,request,make_response,jsonify

from rdbservice import CephVol

app = Flask(__name__)

@app.route('/home')
def home():
    return '<h1>Welcome Home</h1>'

@app.route('/volume' , methods=['POST'])
def create_vol():
    vol_name = request.json['volume']
    pool_name = request.json['pool']
    size = request.json['size']
    print vol_name,pool_name,size
    vol = CephVol(size,pool_name,vol_name)
    vol.create()
    return make_response(jsonify({'volume':vol_name,'pool':pool_name,'size':size,'status':'successful'}), 200)



if __name__ == '__main__':
    app.run(host='10.59.18.42',debug=True,threaded=True)
