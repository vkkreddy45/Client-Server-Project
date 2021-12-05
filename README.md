# pro123

## File description
1. controller.py - consists custom mininet topology
2. server.py - python script to setup a custom server 
3. client.py - python script to setup a client to connect to server
4. input.txt - a simple file consisting of data packet info
 
## Instructions to run controller.py
1. navigate to floodlight folder and start the jar file
<code>java -jar target/floodlight.jar</code>
2. open a new terminal and start the custom mininet using the below 
<code>sudo mn --custom controller.py </code><br>
Note: make sure controller.py file is also available in the same directory

### make sure to clean the network before you close the terminal using the below command<br>
<code>sudo mn -c</code>


## Mininet commands to test the network
1. to test the switches and connections use 
<code>pingall</code>
2. to start xterm terminal use 
<code>xterm host_name</code> host can be either one or more<br>
ex: <code>xterm h0 h2</code> this will start two xterminals one for h0 and h2

## how to use xterm to implement client and server communciation
1. after starting mininet and floodlight controller, use mininet terminal to open xterm for any two hosts<br>
<code>mininet> xterm h0 h9</code>
2. Then two xterminals will pop up one for h0 and one for h9, use ifconfig command(in the xterm) to get the ipaddress of the host<br>
<code>ifconfig</code>
3. Now run the server.py script in any one of the two xterms that are available, for instance we will run server.py script in h0 xterm<br>
<code>python3 server.py</code><br>
make sure that server.py is in the same directory
4. Now run the client.py script in the remaining xterm, for running client.py we need the ip address of the server, refer to step 2 to get the ip address of the server
after having the ip address run the client.py with the server ip address as command line argument.<br>
<code>python3 client.py 10.0.0.1</code><br>
Note: your ip_address may be different from the one mentioned above
