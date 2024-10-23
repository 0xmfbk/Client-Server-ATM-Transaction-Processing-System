import socket
import os

# Function to handle client requests
def handle_client(client_socket):

    balance = 100.0  # Initial balance
    
    
    
    while True:
        # Receive the operation choice from the client
        data = client_socket.recv(1024).decode()


        if data == '1':  # Deposit
            client_socket.sendall(b'\n--> Amount to deposit <--')
            deposit = float(client_socket.recv(1024).decode())
            balance += deposit
            response = f'\nYou have successfully deposited ${deposit:.1f}  \n\n---------------------------'
            client_socket.sendall(response.encode())


        elif data == '2':  # Withdraw
            client_socket.sendall(b'\n<-- Amount to withdraw -->')
            withdraw = float(client_socket.recv(1024).decode())
            if withdraw > balance:
                response = f'\nInsufficient funds. Current balance: ${balance:.1f} \n\n---------------------------'
            else:
                balance -= withdraw
                response = f'\nYou have successfully withdrawn ${withdraw:.1f} \n\n---------------------------'
            client_socket.sendall(response.encode())



        elif data == '3':  # Check Balance
            response = f'\nYour current balance is ${balance:.1f} \n\n---------------------------'
            client_socket.sendall(response.encode())



        elif data == '4':  # Exit
            client_socket.sendall(b'\nThank you for using the ATM Machine!')
            break



        else:
            client_socket.sendall(b'\nInvalid option. Try again.')


    client_socket.close()




# Screen clear & Server banner by use figlet to display banner

os.system('clear')
os.system('figlet Mustafa.BK')


# Smaller title for the client
print("SERVER SIDE\n---------------------------")


# Ask user for port
port_number = int(input("Enter the port to listen on: "))


# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind to a specific address and port
server_socket.bind(('0.0.0.0', port_number))


# Listen for incoming connections
server_socket.listen(5)
print(f'Server listening on port {port_number}')


while True:
    # Accept a new client connection
    client_socket, addr = server_socket.accept()
    print(f'Connected by {addr}')
    
    # Handle the client's operations
    handle_client(client_socket)

