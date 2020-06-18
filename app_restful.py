from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills
app=Flask(__name__)
api=Api(app)

devs=[
    {
        'name': 'denis',
        'skils': ['Python', 'Flask']
    },
    {
        'name': 'deniss',
        'skills': ['Python', 'Django']
    }
]

class Devs(Resource): #this way you dont need to use the if methods == 'GET'
    def get(self,id):
        try:
            response=devs[id]
        except IndexError:
            message = 'Dev of id {} dont exist'.format(id)
            response={'status': 'failed', 'message': message} #friendly error message
        except Exception:
            message='Unknown error, call the responsible for the API'
            response = {'status': 'error', 'message': message} #if the error is unknown
        return response

    def put(self,id):
        data=json.loads(request.data)
        devs[id]=data
        return data
    def delete(self,id):
        devs.pop(id)
        return ({'status': 'success','message': 'deleted'})

class ListDevs(Resource):
    def get(self):
        return devs
    def post(self):
        data = json.loads(request.data)
        devs.append(data)
        return ({'status': 'success', 'message': 'dev included'})



api.add_resource(Devs,'/dev/<int:id>/') #route
api.add_resource(ListDevs,'/dev/')
api.add_resource(Skills,'/skills/')


if __name__ == '__main__':
    app.run()
