from flask import Flask

app = Flask(__name__)

#POST - used to receive data
#GET - used to send data back only
# from the perspective of a server

#POST to send data
#GET to receive data
#from perspective of a browser

#POST /store data: {name: } (create a new store)
@app.route('/store', method=['POST'])
def create_store():
    pass

#GET /store/<string: name> (Get a store for a given name)
@app.route('/store/<string:name>', method=['GET'])
def get_store(name):
    pass

#GET /store (return a list of all stores)
@app.route('/store/', method=['GET'])
def get_store():
    pass

#POST /store/<string: name>/item {name:, price:} (create an item inside a specific store with a given name)
@app.route('/store/<string:name/item>', method=['POST'])
def create_store(name):
    pass

#GET /store/<string: name>/item (get all the items in a specific store)
@app.route('/store/<string:name>/item', method=['GET'])
def get_store(name):
    pass

app.run(port=5000)