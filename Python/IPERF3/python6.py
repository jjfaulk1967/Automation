# Dynamic login & host to linux box. Each box pings the other box.

# Define connection parameters

from getpass import getpass
from netmiko import ConnectHandler

# Define dynamic hosts

host1 = raw_input('Enter in IP address of host 1: ')
host2 = raw_input('Enter in IP address of host 2: ')

# Define dynamic login

username = raw_input('Enter your SSH username: ')
password = getpass()

# Dynamic host and dynamic credentials

linux1 = {
    'device_type': 'linux',
    'ip': host1,
    'username': username,
    'password': password,
}

linux2 = {
    'device_type': 'linux',
    'ip': host2,
    'username': username,
    'password': password,
}

# Connect to linux hosts

net_connect = ConnectHandler(**linux1)

# Define command

command = "ping -c 5 192.168.122.82"

# Print to screen the hostname

print(net_connect.find_prompt())

# Send command

output = net_connect.send_command(command)

# Print results of command

print(output)

net_connect = ConnectHandler(**linux2)

# Define command

command = "ping -c 5 192.168.122.76"

# Print to screen the hostname

print(net_connect.find_prompt())

# Send command

output = net_connect.send_command(command)

# Print results of command

print(output)

# Disconnect ssh session

net_connect.disconnect()


