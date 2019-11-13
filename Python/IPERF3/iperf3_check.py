# login. Choose client, server, and protocol from list. Then execute IPERF3 between any combination of servers.
# Default is 5 seconds at 10Mbps.

# Script introduction

print '\nIPERF3 CONNECTIVITY CHECK VERSION 1.0'                                                                                  # Script title.
print '\nPlease choose client, server & protocol'                                                                                # User instructions.
print '\nList of available clients & servers: [RNPIPERF201, RNDIPERF201, RNCIPERF201, LVPIPERF201, LVDIPERF201, LVCIPERF201]'    # List of available clients & servers.
print '\nList of available protocols: [TCP, UDP]'                                                                                # List of available protocols.

# Load modules and define parameters

from getpass import getpass                                  # Allow user to insert password.
from netmiko import ConnectHandler                           # Connection handler.
from time import time                                        # Module for tracking time of script execution.

# Allow tracking time of script execution

starting_time = time()                                       # Start script execution time tracking.

# Define lists & variables

iperf3_servers = ['rnpiperf201', 'rndiperf201',                  # This is the iperf3 client & server list.
                  'rnciperf201', 'lvpiperf201',
                  'lvdiperf201', 'lvciperf201'
                 ]                
protocols = ['tcp', 'udp']                                   # This is the protocol list. 
client_input_validated = False                               # Create the variable "client_input_validated" and sets it to false.
server_input_validated = False                               # Create the variable "server_input_validated" and sets it to false.
protocol_input_validated = False                             # Create the variable "protocol_input_validated" and sets it to false.
tcp_input = 'tcp'                                            # Create a variable "tcp_input" for main script executon.

# User chooses client, server, & protocol

while client_input_validated != True:                             # This line starts the while loop that can only be exited when "validated" is True.
    client_input = raw_input('\nEnter in clients hostname: ')     # Ask user to choose client.
    if client_input.lower() in iperf3_servers:                    # Checks user input against "iperf3_servers" list. 
        client_input_validated = True                             # Sets the variable "validated" to True which will then exit loop.

while server_input_validated != True:                             # This line starts the while loop that can only be exited when "server_input_validated" is True.
    server_input = raw_input('\nEnter in servers hostname: ')     # Ask user to choose server.
    if server_input.lower() in iperf3_servers:                    # Checks user input against "iperf3_servers" list. 
        server_input_validated = True                             # Sets the variable "server_input_validated" to True which will then exit loop.

while protocol_input_validated != True:                           # This line starts the while loop that can only be exited when "protocol_input_validated" is True.
    protocol_input = raw_input('\nEnter in TCP or UDP: ')         # Ask user to choose protocol.
    if protocol_input.lower() in protocols:                       # Checks user input against "protocols" list. 
        protocol_input_validated = True                           # Sets the variable "protocol_input_validated" to True which will then exit loop.

# Login configuraion.

username = raw_input('\nEnter in your username: ')           # Ask user to enter in their username.
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

# Main script execution

if protocol_input.lower() == tcp_input:                                  # If user chooses tcp, execute tcp in IPERF3
    net_connect = ConnectHandler(**server)                               # Connect to linux host choosen by user as server. 
    command = "iperf3 -s -D -1"                                          # Define command for IPERF3.
    print '\n'                                                           # Added spacing during display of script.
    print(net_connect.find_prompt())                                     # Print to screen the hostname of linux server. 
    print '\nStarting up server'                                         # Print to screen that server is starting up. 
    output = net_connect.send_command(command)                           # Send command.

    net_connect = ConnectHandler(**client)                               # Connect to linux host choosen by user as client.
    command = "iperf3 -c {} -t 5 -b 10M".format(server_input)            # Define command for IPERF3.
    print '\n'                                                           # Added spacing during display of script.
    print(net_connect.find_prompt())                                     # Print to screen the hostname of the linux server.
    print '\nStarting up client'                                         # Print to screen that client is starting up.
    print '\nTCP connectivity check will run for 5 seconds at 10Mpbs'    # Display connectivity check parameters.
    print '\n'                                                           # Added spacing during display of script.
    output = net_connect.send_command(command)                           # Send command. 
    print(output)                                                        # Print results of command.   

else:                                                                    # If user chooses udp, execute udp in IPERF3.
    net_connect = ConnectHandler(**server)                               # Connect to linux host choosen by user as server.
    command = "iperf3 -s -D -1"                                          # Define command for IPERF3.
    print '\n'                                                           # Added spacing during display of script.
    print(net_connect.find_prompt())                                     # Print to screen the hostname of linux server.
    print '\nStarting up server'                                         # Print to screen that server is starting up.
    output = net_connect.send_command(command)                           # Send command.

    net_connect = ConnectHandler(**client)                               # Connect to linux host choosen by user as client.
    command = "iperf3 -c {} -t 5 -u -b 10M".format(server_input)         # Define command for IPERF3.
    print '\n'                                                           # Added spacing during display of script.
    print(net_connect.find_prompt())                                     # Print to screen the hostname of linux server.
    print '\nStarting up client'                                         # Print to screen that client is starting up.
    print '\nUDP connectivity check will run for 5 seconds at 10Mpbs'    # Display connectivity check parameters.
    print '\n'                                                           # Added spacing during display for script.
    output = net_connect.send_command(command)                           # Send command.
    print(output)                                                        # Print results of command.  

# Disconnect SSH sessions

net_connect.disconnect()                                                 # Disconnect ssh sessions

# Print amount of time it took script to execute

print '\nEnd of script, elapsed time=', time()-starting_time             # Print script execution time
