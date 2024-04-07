from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __DBconnectionHandler:
    def __init__(self) -> None:
        #{}:///{} -> a primeira chaves serve para definir qual banco está usando (sqlite) e a segunda chaves serve para definir onde está a pasta principal do projeto (storage.db)
        self.__connection_string = '{}:///{}'.format(
            'sqlite',
            'storage.db'
        )
        self.__engine = None # motor de conexão com o banco de dados
        self.session = None # sessão para trabalhar com tudo que vai ser interessante para o projeto

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string) # passa a string de conexão para o mecanismo e armazena no engine(motor)

    def get_engine(self):
        return self.__engine # tornou privado e so pode acessar por esse get
    
    def __enter__(self): # ele funciona quando entra em um contexto do python
        session_maker = sessionmaker()
        self.session = session_maker(bind = self.__engine) # bind vai ligar a sessão para o mecanismo de conexão 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): # saindo do contexto
        self.session.close()

db_connection_handler = __DBconnectionHandler()