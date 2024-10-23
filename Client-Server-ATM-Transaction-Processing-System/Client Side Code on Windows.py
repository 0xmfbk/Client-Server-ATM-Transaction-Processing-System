from socket import *
import pyfiglet
import os


# Screen Clear & Use pyfiglet to display the banner

os.system('cls')
banner = pyfiglet.figlet_format("Mustafa.BK")
print(banner)



# Smaller title for the client
print("CLIENT SIDE\n---------------------------")


# Ask user for IP address and port
server_ip = input("Enter server IP address: ")
port_number = int(input("Enter server port: "))



# Create a TCP/IP socket
socket_c = socket(AF_INET, SOCK_STREAM)



# Connect to the server
socket_c.connect((server_ip, port_number))



while True:
    # Display menu to the user
    print("\nChoose an operation:\n")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Check Balance")
    print("4: Exit")
    print("\nEnter the choice:", end=" ")


    # Take input from the user
    choice = input()


    # Send the choice to the server
    socket_c.sendall(choice.encode())


    # Exit if the user chooses to quit
    if choice == '4':
        response = socket_c.recv(1024).decode()
        print(response)  # Final message from server
        break


    # Receive a prompt or balance message from the server
    response = socket_c.recv(1024).decode()
    print(response)


    # If the operation is deposit or withdraw, take additional input
    if choice == '1' or choice == '2':
        amount = input()  # Get amount from user
        socket_c.sendall(amount.encode())
        result = socket_c.recv(1024).decode()
        print(result)



# Close the connection
socket_c.close()
print("Connection with server closed.\n")
