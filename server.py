import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost',12345))
    server.listen(1)
    server.settimeout(1.0)

    print('Сервер запущен и ждет клиента...')
    return server

if _name_ == '_main':
    s = start_server()
    s.close()
