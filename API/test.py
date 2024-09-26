from flask import Flask, request, jsonify
import os
app = Flask(__name__)

# Route to receive a list of tuples
@app.route('/tuples', methods=['POST'])
def receive_tuples():
    if not request.json or not isinstance(request.json, list):
        return jsonify({"error": "Invalid input, expected a list of tuples."}), 400

    # Convert list of lists to list of tuples
    tuples_list = [tuple(item) for item in request.json]

    # Process the list of tuples (for demonstration, we'll just return it)
    return jsonify({"received_tuples": tuples_list}), 200

# Run the app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
