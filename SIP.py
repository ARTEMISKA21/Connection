import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind(('localhost', 12345))
    
    server_socket.listen(1)
    print("Ожидание подключения клиента...")
    
    client_socket, addr = server_socket.accept()
    print(f"Подключено к {addr}")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Получено сообщение: {data.decode()}")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()