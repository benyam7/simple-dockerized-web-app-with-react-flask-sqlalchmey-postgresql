from config import Config
from model import db

from flask_cors import CORS
from flask import Flask
from flask import jsonify, request
from sqlalchemy.orm import Session
from flask_restful import Resource, Api

from model import BussinessNewsModel, to_dict

app = Flask(__name__)
api = Api()


class BusinessNews(Resource):
    def get(self):
        return jsonify([to_dict(sport) for sport in BussinessNewsModel.query.all()])

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return "not worked"

        dataToUpdate = {BussinessNewsModel.shares: json_data['shares'] + 1}

        businessData = db.session.query(BussinessNewsModel).filter(
            BussinessNewsModel.id == json_data['id'])
        businessData.update(dataToUpdate)
        db.session.commit()
        return {'worked': "yes"}


api.add_resource(BusinessNews, '/business', )


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)  # confi ps gress
    api.init_app(app)
    db.init_app(app)
    return app


app = create_app(Config)


# Run the application
if __name__ == '__main__':
    app = create_app(Config)
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
