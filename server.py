import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost',12345))
    server.listen(1)
    print('Сервер запущен и ждет клиента...')

    server_running = True
    while server_running:
        try:
            client,address = server.accept()
            print(f'Подключился клиент: {address}')

            while True:
                try:
                    data = client.recv(1024).decode('utf-8')
                    if not data:
                        continue

                    print(f'клиент прислал: {data} ')

                    if data == 'exit':
                        print('клиент решил отключиться')
                        break

                    if data == 'stop_server':
                        print('получена команда выключения сервера')
                        server_running = False
                        break

                    client.send('сообщение получено'.encode('utf-8'))

                except ConnectionResetError:
                    print('связь с клиентом разорвана')
                    break

            client.close()
        except Exception:
            break

    server.close()
    print("Сервер полностью остановлен.")


if __name__ == "__main__":
    run_server()
