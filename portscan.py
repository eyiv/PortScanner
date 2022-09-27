from socket import *
import argparse

parser = argparse.ArgumentParser(description="Scan specified ports, individual ports or a range of ports, on a host to check whether they are open or not.")
parser.add_argument("-t", help="Set the target host for the scan to be completed on. Input host either as an IP address or a domain.", required=True)
parser.add_argument("-po", help="Set the ports to be scanned on the host. Multiple ports should be separated by a comma.", required=True)
parser.add_argument("--range", help="Specify that the ports given is a range of ports to be scanned.\nExample: python portscan.py -t google.com -po 1,3 --range would scan ports 1 through 3.", action="store_true")
parser.add_argument("-p", help="Set the path/file name for the scan results to be saved.")
args = parser.parse_args()

host = args.t
p = str(args.po).split(',')
ports = []
isRangeP = args.range
path = args.p

for i in p:
    ports.append(int(i))

def portScan(host, ports, isRange, path):
    closedPorts = []
    openPorts = []
    
    try:
        IP = gethostbyname(host)
    except:
        print("Cannot resolve host: %s" % host)
        return

    try:
        hostName = gethostbyaddr(IP)
        print("\nScanning port(s) of host: %s\n" % hostName[0])
    except:
        print("\nScanning port(s) of host: %s\n" % IP)
        setdefaulttimeout(1)

    if isRange:
        for i in range(ports[0], ports[1] + 1, 1):
            print("Scanning port: %d" % i)
            try:
                connection = socket(AF_INET, SOCK_STREAM)
                connection.connect((host, i))
                openPorts.append(i)
                connection.close()
                print("Done.")
            except:
                closedPorts.append(i)
                print("Done.")
    else:
        for p in ports:
            print("Scanning port: %d" % p)
            try:
                connection = socket(AF_INET, SOCK_STREAM)
                connection.connect((host, p))
                openPorts.append(p)
                connection.close()
                print("Done")
            except:
                closedPorts.append(p)
                print("Done")
    writeToFile(host, closedPorts, openPorts, R"%s"% path)
    print("\nPort scan complete. Scan results can be found in: %s"% path)

def writeToFile(hostName, closedList, openList, path):
    with open(path, mode='w', encoding='utf-8') as file:
        file.write("Scan results for %s\n\n"% hostName)

        file.write("Open Ports:\n")
        for oP in openList:
            file.write("tcp/%d open\n"% oP)
        if not openList:
            file.write("No open ports.")
        
        file.write("\n\nClosed Ports: \n")
        for cP in closedList:
            file.write("tcp/%d closed\n"% cP)
        if not closedList:
            file.write("No closed ports.")

portScan(host, ports, isRangeP, path)
