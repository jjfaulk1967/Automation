# Dynamic login & host to linux box. Iperf3 test. Pick client & server.

# Define connection parameters

from getpass import getpass
from netmiko import ConnectHandler
from time import time

# Allow tracking time of script execution

starting_time = time()

# Define dynamic hosts

client_input = raw_input('Enter in clients hostname: ')
server_input = raw_input('Enter in servers hostname: ')


# Define dynamic login

username = raw_input('Enter your SSH username: ')
password = getpass()

# Dynamic host and dynamic credentials

client = {
    'device_type': 'linux',
    'ip': client_input,
    'username': username,
    'password': password,
}

server = {
    'device_type': 'linux',
    'ip': server_input,
    'username': username,
    'password': password,
}

# Connect to linux hosts

net_connect = ConnectHandler(**server)

# Define command

command = "iperf3 -s -D -1"

# Print to screen that server is starting up.

print '\nStarting up server'

# Print to screen the hostname

print(net_connect.find_prompt())

# Send command

output = net_connect.send_command(command)

# Print results of command

print(output)

net_connect = ConnectHandler(**client)

# Define command

command = "iperf3 -c {} -t 5".format(server_input)

# Print to screen that client is starting up.

print '\nStarting up client'

# Print to screen the hostname

print(net_connect.find_prompt())

# Send command

output = net_connect.send_command(command)

# Print results of command

print(output)

# Disconnect ssh session

net_connect.disconnect()

# Print script execution time

print '\nEnd of script, elapsed time=', time()-starting_time
