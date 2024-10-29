from netmiko import ConnectHandler


cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.140',  
    'username': 'admin',       
    'password': 'admin',  
}


commands = [
    'interface GigabitEthernet0/1',
    ' switchport access vlan 154',
    ' switchport mode access',
    'interface Vlan7',
    ' ip address 10.195.7.1 255.255.255.0',
    'interface Vlan8',
    ' ip address 10.195.8.1 255.255.255.0',
    'interface Vlan154',
    ' ip address 10.195.199.34 255.255.255.248',
    'ip route 10.18.1.0 255.255.255.0 10.195.199.36',
    'ip route 10.63.0.0 255.255.0.0 10.196.199.36',
    'ip route 10.195.199.0 255.255.255.0 10.195.199.36',
    'interface GigabitEthernet1/1',
    ' no switchport',
    ' negotiation auto',
    ' channel-group 1 mode active',
    'interface GigabitEthernet1/2',
    ' no switchport',
    ' channel-group 1 mode active',
    'interface Port-channel1',
    ' no switchport',
    ' ip address 10.197.1.2 255.255.255.0',
]



try:
    connection = ConnectHandler(**cisco_device)
    print("Connected to the device successfully!")

    output = connection.send_config_set(commands)
    print("Configuration Output:")
    print(output)

    
    connection.disconnect()
    print("Disconnected from the device.")

except Exception as e:
    print(f"An error occurred: {e}")
