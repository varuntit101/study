from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data store for our product catalog
products = [
    {'id': 1, 'name': 'Cloud-Native Skateboard', 'sku': 'CNS-001'},
    {'id': 2, 'name': 'Microservices Mug', 'sku': 'MSM-002'},
    {'id': 3, 'name': 'Kubernetes Keychain', 'sku': 'K8K-003'}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Product Catalog API!'})

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Endpoint to get a single product by its ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    # Listen on all available network interfaces
    app.run(host='0.0.0.0', port=6000, debug=True)
