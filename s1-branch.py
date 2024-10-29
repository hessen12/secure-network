from netmiko import ConnectHandler


cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.140',  
    'username': 'admin',       
    'password': 'admin',  
}


commands = [
    'interface GigabitEthernet0/0',
    ' switchport access vlan 44',
    ' switchport mode access',
    ' negotiation auto',
    
    'interface GigabitEthernet0/1',
    ' switchport access vlan 44',
    ' switchport mode access',
    ' negotiation auto',
    
    'interface GigabitEthernet0/2',
    ' switchport access vlan 44',
    ' switchport mode access',
    ' negotiation auto',
    
    'interface GigabitEthernet0/3',
    ' switchport access vlan 55',
    ' switchport mode access',
    ' negotiation auto',

    'interface GigabitEthernet1/0',
    ' switchport access vlan 44',
    ' switchport mode access',
    ' negotiation auto',
    
    'interface GigabitEthernet1/1',
    ' switchport access vlan 55',
    ' switchport mode access',
    ' negotiation auto',

    'interface GigabitEthernet1/2',
    ' switchport access vlan 55',
    ' switchport mode access',
    ' negotiation auto',
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
