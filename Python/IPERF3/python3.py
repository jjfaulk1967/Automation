# Dynamic login & host to linux host to ping another linux host.

# Define connection parameters

from getpass import getpass
from netmiko import ConnectHandler

# Define dynamic host

host = raw_input('Enter host IP address: ')

# Define dynamic login

username = raw_input('Enter your SSH username: ')
password = getpass()

# Dynamic host and dynamic credentials

linux = {
    'device_type': 'linux',
    'ip': host,
    'username': username,
    'password': password,
}

# Connect to linux host

net_connect = ConnectHandler(**linux)

# Define command

command = "ping -c 5 192.168.122.82"

# Print to screen the hostname

print(net_connect.find_prompt())

# Send command

output = net_connect.send_command(command)

# Disconnect ssh session

net_connect.disconnect()

# Print results of command

print(output)
