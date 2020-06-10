from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

#Init app 
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init database 
db = SQLAlchemy(app)

#Init Marshmallow 
ma = Marshmallow(app) 

#Idea Class/Model 
class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(300))
    tags = db.Column(db.String(75))
    image_url = db.Column(db.String(500))
    importance_level = db.Column(db.Integer)
    effort_in_hours = db.Column(db.Integer)
    tech_stack = db.Column(db.String(75))

    def __init__(self, name, description, tags, image_url, importance_level, effort_in_hours, tech_stack):
        self.name = name 
        self.description = description 
        self.tags = talgs 
        self.image_url = image_url 
        self.importance_level = importance_level
        self.effort_in_hours = effort_in_hours
        self.tech_stack = techstack 

#Idea Schema 
class IdeaSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'description', 'tags', 'image_url', 'importance_level', 'effort_in_hours', 'tech_stack')

idea_schema = IdeaSchema()
ideas_schema = IdeaSchema(many=True)


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