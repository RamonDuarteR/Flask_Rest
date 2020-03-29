from flask import Flask, request, jsonify
import json

app = Flask(__name__)

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

@app.route("/", methods=["GET","POST"])
def lista_dev():
    if request.method == "GET":
        return jsonify(desenvolvedores)
    elif request.method == "POST":
        dados= json.loads(request.data)
        ###################################### PRECISA DE JSON.LOADS PARA CARREGAR UM JSON
        id=len(desenvolvedores)
        dados["id"]=id
        desenvolvedores.append(dados)
        return jsonify({"status":"sucess","mensagem":"Desenvolvedor incluido com sucesso e seu ID é {}".format(id)})

@app.route("/dev/<int:id>", methods=["GET","PUT","DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro','mensagem':'ID {} inexistente'.format(id)}
        return jsonify(response)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)


if __name__ == "__main__":
    app.run(debug=True)return jsonify({"status":"sucess","mensagem":"Registro Excluido"})