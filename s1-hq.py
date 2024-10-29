from netmiko import ConnectHandler

# Define the device information
cisco_switch = {
    'device_type': 'cisco_ios',  
    'host': '192.168.1.140',      
    'username': 'admin',         
    'password': 'admin',   
}


try:
    connection = ConnectHandler(**cisco_switch)
    print("Connected to the switch.")

    
    config_commands = [
        'interface GigabitEthernet0/1',
        ' switchport trunk encapsulation dot1q',
        ' switchport mode trunk',
        ' negotiation auto',
        'interface GigabitEthernet0/3',
        ' switchport access vlan 7',
    ]

    
    output = connection.send_config_set(config_commands)
    print("Configuration applied successfully:")
    print(output)

except Exception as e:
    print(f"Failed to connect or apply configuration: {e}")

finally:
    # Close the connection
    connection.disconnect()
