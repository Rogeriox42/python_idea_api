from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_route():
    return jsonify({"Message": "Hello Idea API!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5005))
    app.run(debug=True, port=port)