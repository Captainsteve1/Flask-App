from flask import Flask, jsonify, request, abort

app = Flask(__name__)
API_KEY = 'antoni_bot'
resources = {'access': 'Enable'}

def validate_api_key(api_key):
    return api_key == API_KEY

@app.route('/api/resources', methods=['GET'])
def get_resources():
    api_key = request.headers.get('API-Key')
    if not api_key or not validate_api_key(api_key):
        abort(403)  # Forbidden
    else:
        return jsonify(resources)

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):

    api_key = request.headers.get('API-Key')
    if not api_key or not validate_api_key(api_key):
        abort(403)  # Forbidden
    else:
        resource = next((res for res in resources if res['id'] == resource_id), None)
        if resource:
            return jsonify(resource)
        else:
            abort(404)

@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 403 - Forbidden
@app.errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden'}), 403

if __name__ == '__main__':
    app.run(debug=True)
