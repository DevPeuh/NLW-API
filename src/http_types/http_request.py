from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None: # body vai ser o parametro de body q irá enviar, param vai ser o paramentro de URL que irá capitar.
        self.body = body
        self.param = param