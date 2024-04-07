class AlgumaCoisa:
    def __enter__(Self): # ele funciona quando entra em um contexto do python
        print('Estou entrando')

    def __exit__(self, exc_type, exc_val, exc_tb): # saindo do contexto
        print('Estou saindo')

with AlgumaCoisa() as ola: # with para quando ele estiver no meio
    print('Estou no meio')

