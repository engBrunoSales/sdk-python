import requests
import json

from src.test_sdk.domains.usuario import Usuario
from decouple import config
URL_BASE = config('URL_BASE', default='http://localhost.com')

class UsuarioController:
    def get_usuario(self, id):
        request = requests.get(URL_BASE + f"/usuarios/{id}")
        resposta_json = json.loads(request.content)
        return Usuario.from_json(resposta_json)
