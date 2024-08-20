from netmiko import ConnectHandler
import os
from dotenv import load_dotenv

ipr1 = '172.31.110.3'
ipr2 = '172.31.110.4'

load_dotenv()
username = os.environ.get('TELNET_USER')
password = os.environ.get('TELNET_PASSWORD')

device_params1 = {
    'device_type': 'cisco_ios',
    'ip': ipr1,
    'username': username,
    'password': password,
}

commands1 = [
    'router ospf 1 vrf control-data',
    'network 192.168.1.0 0.0.0.255 area 0',
    'network 192.168.2.0 0.0.0.255 area 0',
]

device_params2 = {
    'device_type': 'cisco_ios',
    'ip': ipr2,
    'username': username,
    'password': password,
}

commands2 = [
    'router ospf 1 vrf control-data',
    'network 192.168.2.0 0.0.0.255 area 0',
    'network 192.168.3.0 0.0.0.255 area 0',
    'default-information originate',
]

def configure_device(device_params, commands):
    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
        return result

result1 = configure_device(device_params1, commands1)
print(f"Device 1 configuration result:\n{result1}")

result2 = configure_device(device_params2, commands2)
print(f"Device 2 configuration result:\n{result2}")