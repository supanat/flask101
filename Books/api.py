from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/<int:id>/borrow')
class BorrowBookController(Resource):
    def post(self,id):
        return {'message':'OK'}



if __name__ == '__main__':
    app.run(debug=True)