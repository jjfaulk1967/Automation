
# Dynamically login, choose client, server, and protocol for IPERF3

# Load modules and define parameters

from getpass import getpass                                  # Allow user to insert password.
from netmiko import ConnectHandler                           # Connection handler.
from time import time                                        # Module for tracking time of script execution.

# Allow tracking time of script execution

starting_time = time()                                       # Start script execution time tracking.

# Dynamic user input

client_input = raw_input('Enter in clients hostname: ')      # Ask user to pick client.
server_input = raw_input('Enter in servers hostname: ')      # Ask user to pick server.
protocol_input = raw_input('Enter in TCP or UDP: ')          # Asl user to pick protocol. 

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

if protocol_input == 'TCP':
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


else:
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

