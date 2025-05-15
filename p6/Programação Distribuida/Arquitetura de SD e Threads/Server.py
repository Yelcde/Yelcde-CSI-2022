import hprose
import threading

_store = {}
_lock = threading.Lock()

def update(chave, valor):
    with _lock:
        existed = chave in _store
        _store[chave] = valor
        return not existed
    
def remove(chave):
    with _lock:
        if chave in _store:
            del _store[chave]
            return True
        return False
    
def get(chave):
    with _lock:
        if chave in _store:
            return _store[chave]
        return -1
    
if __name__ == "__main__":
    server = hprose.HttpServer()
    server.addFunction(update)
    server.addFunction(remove)
    server.addFunction(get)
    server.start()