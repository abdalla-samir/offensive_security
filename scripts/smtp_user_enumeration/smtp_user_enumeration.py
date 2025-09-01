import sys
import socket
import subprocess

if len(sys.argv) != 3:
        print("Usage: ./smtp_user_enumeration <IP> <user>")
        sys.exit(1)

ip_address = sys.argv[1]
users_file = sys.argv[2]

ping = ["ping", "-c", "4", f"{ip_address}"]
ping_results = subprocess.run(ping, capture_output=True, text=True)

if ping_results.returncode == 0:
        usernames = []
        with open(users_file, "r") as f:
            for line in f:
                usernames.append(line.strip())
        for user in usernames:
            command = f"VRFY {user}\r\n".encode()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5)
            client_socket.connect((ip_address, 25))
            greeting_message = client_socket.recv(1024)
            print(greeting_message.decode())
            client_socket.sendall(command)
            result = client_socket.recv(1024).decode()
            print(result)
            client_socket.close()
else:
    print("Ping Failed: Provide a valid ip address")
