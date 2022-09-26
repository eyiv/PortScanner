# Port Scanner
#### As the name suggests, scan to check open TCP ports on a host. Results are shown and saved on a text file, the path and name of which are determined by the user.


### Usage:
You can set the host (IP address or domain), ports to be scanned, set whether or not the ports are a range of ports to be scanned, and set the path for the file to be saved through command line arguments as follows
  #### Setting the target host (```-t```)
  ```
  python portscan.py -t google.com
  ```
  #### Setting the ports to be scanned (```-po```)
  ```
  python portscan.py -t google.com -po 80
  ```
  If you want to scan more ports, separate them with commas. This will scan both ports specified:
  ```
  python portscan.py -t google.com -po 80,22
  ```
  This will scan ports 80 and 22. If you want to scan a range of ports, add the ```--range``` command line argument after you specify the ports
  ```
  python portscan.py -t google.com -po 1,33 --range
  ```
  This scans ports 1 through 33.
  ### Setting the file path
  Results are saved and written to a text file with a name and path passed to the CLI using the argument ```-p```
  ```
  python portscan.py -t google.com -po 80,22 -p scanresultsgoogle.txt
  ```
  or
  ```
  python portscan.py -t google.com -po 80,22 -p C:\Users\Documents\scanresults.txt
  ```
  