from flask import Flask, jsonify, request
import json
app=Flask(__name__)

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

#return dev by id, change and delete
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response=devs[id]
        except IndexError:
            message = 'Dev of id {} dont exist'.format(id)
            response={'status': 'failed', 'message': message} #friendly error message
        except Exception:
            message='Unknown error, call the responsible for the API'
            response = {'status': 'error', 'message': message} #if the error is unknown
        return jsonify(response)
    elif request.method == 'PUT':
        data = json.loads(request.data) #request from body via api only for put, and convert to json
        devs[id]=data
        return jsonify(data) #ts possible to return an status message like sucess, but its commom to send the result
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'success','message': 'deleted'})

#return list of all devs, and include new dev
@app.route('/dev/', methods=['POST','GET'])
def lists():
    if request.method=='POST':
        data = json.loads(request.data)
        devs.append(data)
        return jsonify({'status': 'success','message': 'dev included'})
    elif request.method == 'GET':
        return jsonify(devs)

if __name__ == '__main__':
    app.run()