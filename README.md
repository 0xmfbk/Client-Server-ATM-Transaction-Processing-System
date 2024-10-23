# ATM Transaction Processing System

This repository contains a simple ATM transaction processing system with a client-server architecture. The client application allows users to perform secure transactions such as deposits, withdrawals, and balance inquiries through a TCP/IP socket connection.

## Prerequisites

- Python 3.x installed on your system.
- The `pyfiglet` library for displaying banners (install using `pip install pyfiglet`).

## Files Included

- `client.py`: The client-side code for interacting with the ATM server.
- `server.py`: The server-side code that handles client requests.

## How to Run the Server

1. **Open a terminal (command prompt)** on your machine.

2. **Navigate to the directory** where `server.py` is located.

3. **Run the server code** by executing:
   ```bash
   python server.py

4- Input the port number on which the server will listen for incoming connections when prompted. For example:

Enter the port to listen on: 8080

5- The server will start and display a message indicating that it is listening for connections.

# How to Run the Client

1- Open another terminal on your machine (or a different machine if you are running the server and client separately).

2- Navigate to the directory where client.py is located.

3- Run the client code by executing:

` python client.py `

4- Input the server IP address and port when prompted. For example:


` Enter server IP address: 127.0.0.1 `

` Enter server port: 8080 `


5- The client will display a menu with options for deposit, withdraw, check balance, or exit. Follow the prompts to complete transactions.

# Usage

## Choose an operation by entering the corresponding number:

1: Deposit

2: Withdraw

3: Check Balance

4: Exit

After selecting an operation, follow any additional prompts for input (e.g., entering the amount for deposit or withdrawal).

# Closing the Application

` To exit the client application, select option 4 `

- The server will continue running and can handle multiple client connections until manually stopped (e.g., using Ctrl+C in the terminal).


# Troubleshooting

- Ensure that the server is running before starting the client.
- Make sure the port you are using is not blocked by a firewall.
- Verify that the IP address entered in the client matches the server's IP address.


# License

This project is licensed under the MIT License.

` 
You can copy and paste this Markdown content into a file named `README.md`. Let me know if you need any further assistance!
 ` 
