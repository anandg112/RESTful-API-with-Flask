from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

#POST - used to receive data
#GET - used to send data back only
# from the perspective of a server

#POST to send data
#GET to receive data
#from perspective of a browser

#POST /store data: {name: } (create a new store)
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/<string: name> (Get a store for a given name)
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({"Message": "No store found!"})
    #iterate over stores
    #if store name matches, return that store
    #if none match, return an error msg

#GET /store (return a list of all stores)
@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores})

#POST /store/<string: name>/item {name:, price:} (create an item inside a specific store with a given name)
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'No store found'})

#GET /store/<string: name>/item (get all the items in a specific store)
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
        else:
            return jsonify({"Message": "No store found!"})

app.run(port=5000)