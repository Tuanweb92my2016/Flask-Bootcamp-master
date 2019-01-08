from flask import Flask
from flask_restful import Resource,Api


app = Flask(__name__)

# grabing
api = Api (app)

#create resource class
class HelloWorld(Resource):

    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld,'/')


if __name__ == '__main__':
    app.run(debug=True)
