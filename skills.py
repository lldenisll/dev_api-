from flask_restful import Resource

skills=['Python', 'Java', 'Flask', 'Django','Ruby']
class Skills(Resource):
    def get(self):
        return skills
