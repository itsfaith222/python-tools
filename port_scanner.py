# Port Scanner using Python 
import socket

#function for scanning the ports
def scan_ports(device, range):
    #here is the code
    print(f"Scanning the ports {range} on the device:{device} \nStarting the scan...")

    #iterate through each port in range list
    for port in range: 
        #create a tcp socket
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM) 

        #setting the timeout for the socket 
        timeout = 1 

        #try to connect to the ip port
        try: 
            sock.connect((device, port))
            #if the connection is successful, print port number and connection successful
            print(f'Connection to port {port} was susseful. {port}= Open')
            return 0
        except: 
            print(f'Connection to port {port} failed. {port}= Closed')
        finally: 
            sock.close()

        #end of all scans/program
        print(f'Ports {range} have been scanned and report if open or not. end of program')


    



#get user input for the target device hostname or IP
target = input("Enter the target IP address or hostname: ")


while True: 
    #get user input for the options of which ports to scan 
    option = input("Enter the option for which ports to scan: \n  1. Scan Common Ports \n  2. Scan a specific port \n option: ")

    if option == "1": 
        print("Scanning well known ports... ")
        common_ports = [80, 443, 21, 22, 23, 25, 53, 5353]
        scan_ports(target, common_ports) 
    elif option == "2":
        port = []
        port.append(input("Enter the port number to scan: "))
        scan_ports(target, port) 
    else:
        print("Invalid option, Try again") 


