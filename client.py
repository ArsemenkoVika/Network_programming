import socket
import sys

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
         client.connect(('localhost', 12345))
    except ConnectionRefusedError:
        print('Ошибка:сервер не запущен')
        return

    while True:
        try:
            message = input('введите сообщение для отправки:')

            if not message:
                continue

            client.send(message.encode('utf-8'))

            if message == 'exit':
                break

            response = client.recv(1024).decode('utf-8')
            print(f"получено: {response}")

        except (ConnectionAbortedError, ConnectionResetError):
            print('\nПрограмма разорвала установленное подключение')
            print('process finished with exit code 0')

        client.close()

if __name__ == '__main__':
    run_client()