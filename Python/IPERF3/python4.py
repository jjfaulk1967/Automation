# Dynamic login to linux box. Each box pings their loopback. 

# Define connection parameters

from getpass import getpass
from netmiko import ConnectHandler

# Define dynamic login

username = raw_input('Enter your SSH username: ')
password = getpass()

# Dynamic host and dynamic credentials

linux1 = {
    'device_type': 'linux',
    'ip': '192.168.122.76',
    'username': username,
    'password': password,
}

linux2 = {
    'device_type': 'linux',
    'ip': '192.168.122.82',
    'username': username,
    'password': password,
}

# Connect to linux hosts

all_devices = [linux1, linux2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)

# Define command

    command = "ping -c 5 127.0.0.1"

# Print to screen the hostname

    print(net_connect.find_prompt())

# Send command

    output = net_connect.send_command(command)

# Print results of command

    print(output)

# Disconnect ssh session

net_connect.disconnect()


