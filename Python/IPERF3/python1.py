# Statically connect to linux host to ping another linux host.

# Define connection type

from netmiko import ConnectHandler

# Statically define host and credentials

linux = {
    'device_type': 'linux',
    'ip': '192.168.122.76',
    'username': 'python',
    'password': 'python',
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
