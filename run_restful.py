from flask import Flask, request
from flask_restful import Resource,Api
import json

app=Flask(__name__)
api=Api(app)

desenvolvedores= [
    {"id":"0",
     "nome":"Ramon",
     "habilidades":["Python","Flask"]
     },
    {"id":"1",
     "nome":"Lucas",
     "habilidades":["Java","Javascript"]
     }
]

class dev(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro','mensagem':'ID {} inexistente'.format(id)}
        return response
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self,id):
        desenvolvedores.pop(id)
        return {"status": "sucess", "mensagem": "Registro Excluido"}


class listar(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        id= len(desenvolvedores)
        dados["id"] = id
        desenvolvedores.append(dados)
        return {"status": "sucess", "mensagem": "Registro Adicionado, o ID é {}".format(id)}


api.add_resource(dev,"/dev/<int:id>")
api.add_resource(listar,"/")

if __name__ == '__main__':
    app.run(debug=True)