# Port Scanner using Python 


#get user input for the target device hostname or IP
target = input("Enter the target IP address or hostname: ")

while True: 
    #get user input for the options of which ports to scan 
    option = input("Enter the option for which ports to scan: \n  1. Scan Common Ports \n  2. Scan a specific port \n option: ")

    if option == "1": 
        print("Scanning well known ports... ")
    elif option == "2":
        port = input("Enter the port number to scan: ") 
    else:
        print("Invalid option, Try again") 

def scan_ports(device, range):
    #here is the code


