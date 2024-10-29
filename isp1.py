from netmiko import ConnectHandler


cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.140',  
    'username': 'admin',       
    'password': 'admin',  
}


commands = [
    'interface GigabitEthernet0/1',
    ' switchport access vlan 44',
    ' switchport mode access',
    ' negotiation auto',
    
    'interface GigabitEthernet0/2',
    ' switchport access vlan 55',
    ' switchport mode access',
    ' negotiation auto',
    
    'interface Vlan44',
    ' ip address 10.63.244.254 255.255.255.0',
    ' glbp 1 ip 10.63.244.1',
    ' glbp 1 priority 200',
    ' glbp 1 preempt',

    'interface Vlan55',
    ' ip address 10.63.255.254 255.255.255.0',
    ' glbp 1 ip 10.63.255.1',
    ' glbp 1 priority 200',
    ' glbp 1 preempt',

    'ip route 10.195.0.0 255.255.0.0 10.196.199.129',
    'ip route 10.195.0.0 255.255.0.0 10.195.199.129',
    'ip route 10.195.199.0 255.255.255.248 10.195.199.129',
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
