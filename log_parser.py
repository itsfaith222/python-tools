#This is the log parser file 

"""Steps for the log parser:
1. Read the file line by line using the open() function 
2. for each line. get all the information from each colum
3. We want to track the failed login attempts using the satus code also track toal requests and supisous ips 
4. Print output results summary and save supisous logs to separte log file"""

#this is the module for regular expressions, so i can take out the data from each line of the logs
import re 
from collections import Counter 

#important variables
failed_attempts= []     #list to store failed login attempts
ip_counter = Counter() 
failed_code_counts = 0 
total_lines = 0

#main function putting the log in the logfile variable then calling the parse_log function
def main(): 
    #main function where the log parsing will run 
    log_file = "access.log"
    parse_log(log_file)

    #output results summary
    print("-------------- Log Parsing Summary --------------")
    print(f"Total log lines scanned: {total_lines}")
    print(f"Total failed attemps: {failed_code_counts}")
    print(f"Unique ip: {len(ip_counter)}")

    print("\nTop 5 IP addresses")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

    with open("suspicious_logs.log", "w") as output_file:
        for i in failed_attempts:
            output_file.write(i + "\n")
    print("\nSuspicious entries saved to suspicious_output.txt")


#parse log function to open the log file and read it line by line
def parse_log(log):
    with open(log, 'r') as file:
        for line in file: 
            #print(line) #for testing purposes
            total_lines += 1 #increment total lines counter

        #used to extract the pattern for the ip address, timestamp and the other colums
        #Example: 192.168.1.5 - - [15/Dec/2025:14:52:10] "GET /admin HTTP/1.1" 403 498
        match = re.match(r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\] "(.*?)" (\d+)', line) 
        
        if match: 
            ip = match.group(1)
            timestamp = match.group(2)
            command = match.group(3)
            staus_code = int(match.group(4))

            #count the ips 
            ip_counter[ip] += 1

            #flags for supisous status codes
            if staus_code == 401: 
                failed_attempts.append(line)
                failed_code_counts += 1


#call the main function
if __name__ == "__main__":
    main()