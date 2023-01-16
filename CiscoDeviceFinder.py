from netmiko import ConnectHandler
import getpass

ssh_pass = getpass.getpass(prompt="Enter the SSH key password: ")

def again():
 srch_mode = input("Search Mode: (IP/MAC): ")
 match srch_mode:
   case "MAC":
    macaddr = input("Enter the MAC address of the device (Format: ABCD.1234.4321): ")
    office = input("Enter the name of the office (Apple/Potato/Banana/All): ")
    sw1 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.1",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    sw2 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.2",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    sw3 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.3",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    sw4 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.4",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    sw5 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.5",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    sw6 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.6",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    sw7 = {
               'device_type': 'cisco_xe',
               'ip': "192.168.1.7",
               'username': 'user',
               'use_keys': True,
               'key_file': '~/.ssh/id_rsa',
               'passphrase': ssh_pass,
               'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    if office == "Apple":
                for device_apple in (sw1, sw2, sw3):
                    net_connect = ConnectHandler(**device_apple)
                    output = net_connect.send_command("show  mac address-table | include " + macaddr)
                    if device_apple == sw1:
                        print()
                        print("------------ sw1 --------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_apple == sw2:
                        print("------------- sw2 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_apple == sw3:
                        print("------------- sw3 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    net_connect.disconnect()
    elif office == "Potato":
                for device_potato in (sw4, sw5, sw6):
                    net_connect = ConnectHandler(**device_potato)
                    output = net_connect.send_command("show  mac address-table | include " + macaddr)
                    if device_potato == sw4:
                        print("------------- sw4 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_potato == sw5:
                        print("------------- sw5 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_potato == sw6:
                        print("------------- sw6 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    net_connect.disconnect()
    elif office == "Banana":
                with ConnectHandler(**sw7) as net_connect:
                    output = net_connect.send_command("show mac address-table | include " + macaddr)
                    print("------------- sw7 -------------")
                    print(output)
                    print("-------------------------------")
                    net_connect.disconnect()
    elif office == "All":
                for device_all in (sw1, sw2, sw3, sw4, sw5, sw6, sw7):
                    net_connect = ConnectHandler(**device_all)
                    output = net_connect.send_command("show  mac address-table | include " + macaddr)
                    if device_all == sw1:
                        print()
                        print("------------- sw1 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == sw2:
                        print("------------- sw2 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == sw3:
                        print("------------- sw3 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == sw4:
                        print("------------- sw4 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == sw5:
                        print("------------- sw5 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == sw6:
                        print("------------- sw6 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == sw7:
                        print("------------- sw7 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
    else:
        print("There is no such office.")
   case "IP":
    ipaddr = input("Enter the IP address of the device: ")
    office = input("Enter the name of the office (Apple/Potato/Banana/All): ")
    gw01 = {
                'device_type': 'cisco_xe',
                'ip': "192.168.2.1",
                'username': 'user',
                'use_keys': True,
                'key_file': '~/.ssh/id_rsa',
                'passphrase': ssh_pass,
                'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    gw02 = {
                'device_type': 'cisco_xe',
                'ip': "192.168.2.2",
                'username': 'user',
                'use_keys': True,
                'key_file': '~/.ssh/id_rsa',
                'passphrase': ssh_pass,
                'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
            }
    gw03 = {
                'device_type': 'cisco_xe',
                'ip': "192.168.2.3",
                'username': 'user',
                'use_keys': True,
                'key_file': '~/.ssh/id_rsa',
                'passphrase': ssh_pass,
                'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    gw04 = {
                'device_type': 'cisco_xe',
                'ip': "192.168.2.4",
                'username': 'user',
                'use_keys': True,
                'key_file': '~/.ssh/id_rsa',
                'passphrase': ssh_pass,
                'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    gw05 = {
                'device_type': 'cisco_xe',
                'ip': "192.168.2.1",
                'username': 'user',
                'use_keys': True,
                'key_file': '~/.ssh/id_rsa',
                'passphrase': ssh_pass,
                'disabled_algorithms': dict(pubkeys=['rsa-sha2-256', 'rsa-sha2-512'])
    }
    if office == "Apple":
        for device_apple in (gw01, gw02):
            net_connect = ConnectHandler(**device_apple)
            output = net_connect.send_command("show arp | include " + ipaddr)
            if device_apple == gw01:
                print()
                print("------------ gw01 -------------")
                print()
                print(output)
                print()
                print("-------------------------------")
                print()
            elif device_apple == gw02:
                print("------------- gw02 -------------")
                print()
                print(output)
                print()
                print("-------------------------------")
                print()
            net_connect.disconnect()
    elif office == "Potato":
                for device_potato in (gw03, gw04):
                    net_connect = ConnectHandler(**device_potato)
                    output = net_connect.send_command("show  arp | include " + ipaddr)
                    if device_potato == gw03:
                        print("------------ gw03 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_potato == gw04:
                        print("------------ gw04 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    net_connect.disconnect()
    elif office == "Banana":
                with ConnectHandler(**gw05) as net_connect:
                    output = net_connect.send_command("show arp | include " + ipaddr)
                    print("------------ gw05 -------------")
                    print(output)
                    print("-------------------------------")
                    net_connect.disconnect()
    elif office == "All":
                for device_all in (gw01, gw02, gw03, gw04, gw05):
                    net_connect = ConnectHandler(**device_all)
                    output = net_connect.send_command("show  arp | include " + ipaddr)
                    if device_all == gw01:
                        print()
                        print("------------ gw01 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == gw02:
                        print("------------ gw02 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == gw03:
                        print("------------ gw03 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == gw04:
                        print("------------ gw04 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
                    elif device_all == gw05:
                        print("------------ gw05 -------------")
                        print()
                        print(output)
                        print()
                        print("-------------------------------")
                        print()
again()
while True:
    flag = input('One more time? [Y/N]: ')
    if flag == 'Y':
        again()
    else:
        break
