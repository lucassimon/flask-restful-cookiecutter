from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {"ping": "pong"}
