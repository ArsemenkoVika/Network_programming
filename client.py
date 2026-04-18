import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    while True:
        message = input('введите сообщение для отправки:')

        if not message:
            print('пустое сообщение, введите снова')
            continue

        if message == 'exit':
            break

        response = client.recv(1024).decode('utf-8')
        print(f"получено: {response}")
    client.close()

if __name__ == '__main__':
    run_client()