# Dynamically login, choose client, server, and protocol from list for IPERF3

# Load modules and define parameters

from getpass import getpass                                  # Allow user to insert password.
from netmiko import ConnectHandler                           # Connection handler.
from time import time                                        # Module for tracking time of script execution.

# Allow tracking time of script execution

starting_time = time()                                       # Start script execution time tracking.

# Define lists & variables

iperf3_servers = ['rnpiperf201', 'lvpiperf201']              # This is the iperf3 server list.
protocols = ['tcp', 'udp']                                   # This is the protocol list. 
client_input_validated = False                               # Create the var "client_input_validated" and sets it to false.
server_input_validated = False                               # Create the var "server_input_validated" and sets it to false.
protocol_input_validated = False                             # Create the var "protocol_input_validated" and sets it to false.
tcp_input = 'tcp'                                            # Create a var "tcp_input" for script executon

# User picks client, server, & protocol

while client_input_validated != True:                        # This line starts the while loop that can only be exited when "validated" is True.
    client_input = raw_input('Enter in clients hostname: ')  # Ask user to pick client.
    if client_input.lower() in iperf3_servers:               # Checks user input against "iperf3_servers" list. 
        client_input_validated = True                        # Sets the var "validated" to True which will exit loop.

while server_input_validated != True:                        # This line starts the while loop that can only be exited when "server_input_validated" is True.
    server_input = raw_input('Enter in servers hostname: ')  # Ask user to pick server.
    if server_input.lower() in iperf3_servers:               # Checks user input against "iperf3_servers" list. 
        server_input_validated = True                        # Sets the var "server_input_validated" to True which will exit loop.

while protocol_input_validated != True:                      # This line starts the while loop that can only be exited when "protocol_input_validated" is True.
    protocol_input = raw_input('Enter in TCP or UDP: ')      # Ask user to pick protocol.
    if protocol_input.lower() in protocols:                  # Checks user input against "protocols" list. 
        protocol_input_validated = True                      # Sets the var "protocol_input_validated" to True which will exit loop.

# Dynamic login configuraion.

username = raw_input('Enter your SSH username: ')            # Ask user to enter in their username.
password = getpass()                                         # Ask user for their password. 

# Server & Client Dictionaries

client = {                                                   # Dictionary name.
    'device_type': 'linux',                                  # Set device type to linux.
    'ip': client_input,                                      # Insert user choice for client.
    'username': username,                                    # Insert users username.
    'password': password,                                    # Insert users password.
}

server = {                                                   # Dictionary name.
    'device_type': 'linux',                                  # Set device type to linux.
    'ip': server_input,                                      # Insert users choice for server.
    'username': username,                                    # Insert users username.
    'password': password,                                    # Insert users password.
}

# Script execution

if protocol_input.lower() == tcp_input:                      # If user picks tcp, execute tcp in IPERF3
    net_connect = ConnectHandler(**server)                   # Connect to linux hosts
    command = "iperf3 -s -D -1"                              # Define command
    print '\nStarting up server'                             # Print to screen that server is starting up.
    print(net_connect.find_prompt())                         # Print to screen the hostname
    output = net_connect.send_command(command)               # Send command

    net_connect = ConnectHandler(**client)                   # Connect to linux hosts
    command = "iperf3 -c {} -t 5".format(server_input)       # Define command
    print '\nStarting up client'                             # Print to screen that client is starting up.
    print ('You chose TCP')                                  # Protocol choice. 
    print(net_connect.find_prompt())                         # Print to screen the hostname
    output = net_connect.send_command(command)               # Send command 
    print(output)                                            # Print results of command   


else:                                                        # If user picks udp, execute udp in IPERF3.
    net_connect = ConnectHandler(**server)                   # Connect to linux hosts
    command = "iperf3 -s -D -1"                              # Define command
    print '\nStarting up server'                             # Print to screen that server is starting up.
    print(net_connect.find_prompt())                         # Print to screen the hostname
    output = net_connect.send_command(command)               # Send command 

    net_connect = ConnectHandler(**client)                   # Connect to linux hosts
    command = "iperf3 -c {} -t 5 -u".format(server_input)    # Define command
    print '\nStarting up client'                             # Print to screen that client is starting up.
    print ('You chose UDP')                                  # Protocol choice.
    print(net_connect.find_prompt())                         # Print to screen the hostname
    output = net_connect.send_command(command)               # Send command 
    print(output)                                            # Print results of command   

net_connect.disconnect()                                     # Disconnect ssh session

print '\nEnd of script, elapsed time=', time()-starting_time # Print script execution time
