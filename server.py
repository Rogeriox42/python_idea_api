from flask import Flask, jsonify
import os

app = Flask(__name__)

#Main Route 
@app.route('/', methods=['GET'])
def root_route():
    return jsonify({"Message": "Hello Idea API!"})

#Get All Ideas Route 
@app.route('/idea', methods=['GET'])
def get_ideas():
    return jsonify({"Message": "IDEA LIST ROUTE"})

#Get Idea by ID
@app.route('/idea/<id>', methods=['GET'])
def get_idea_by_id(id):
    return jsonify({"Message": "IDEA SHOW ROUTE"})

#Create Idea
@app.route('/idea', methods=['POST'])
def create_idea():
    return jsonify({"Message": "IDEA POST ROUTE"})

#Update Idea
@app.route('/idea/<id>', methods=['PUT'])
def update_idea(id):
    return jsonify({"Message": "IDEA PUT ROUTE"})

#Delete Idea
@app.route('/idea/<id>', methods=['DELETE'])
def delete_idea(id):
    return jsonify({"Message": "IDEA DELETE ROUTE"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5005))
    app.run(debug=True, port=port)