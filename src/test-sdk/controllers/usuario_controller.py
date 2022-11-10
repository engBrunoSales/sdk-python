import requests
import json

class UsuarioController:
    def get_usuario(self, id):
        request = requests.get("Aqui vai a url para a chamada")
        resposta_json = json.loads(request.content)
        print(resposta_json)
