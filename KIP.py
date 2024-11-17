import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect(('localhost', 12345))
    
    message = "Привет, сервер!"
    client_socket.sendall(message.encode('utf-8'))
    
    client_socket.close()

if __name__ == "__main__":
    main()