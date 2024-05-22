                                                    #***********  NORTHEASTERN UNIVERSITY  **************
                                                            #Fundamentals of Computer Networks.
                                        # “I (We) have read and understood the course academic integrity policy.
                                                                #TCP Socket Programming 1:

                            #Generated FLAG (NUID: 002528871): 'EECE7374', 'SUCC', '26d79c08a24c275405f0601d54f49abb2b2e7e4f7f62e4cb342256a8c627276c'

                                        #************************************************************************************

import hashlib                                          #Importing the required libraries
import random
import socket
import sys

                                                            #here we need to assign the server details as this is the TCP protocol and need to make the connection
server_hostname='kopi.ece.neu.edu'
server_port=5210
                                                                #connection needs to be made  with the following loc
s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((server_hostname,server_port))                        #providing the hostname and serverport is required for the three way handshake
                                                                #defining the required variables to be used further
flag=""
secret_key="EECE7374 INTR 002725871"                             # this is the secret code which has NUID 
rmsg=""
listexp=""
                                                                #first message which is important and secret  has to be send
s.send(secret_key.encode('utf-8'))

                                                                #loop executing infinitly 
while True:
    
    rmsg=s.recv(4096).decode("utf-8")                           #recieving the message which is the expression
    listexp=rmsg.split()                                        #splitting the message into list with spaces 
    if listexp[1]=="SUCC":                                      #the message which is going to be sent after the 100 correct answers to the expression
        print(listexp)
        break
                                                                #else executes if the succ msg isnt sent by the server
    else:
        listexp[2]=int(listexp[2])                              #list index 2 and list index 4 are converted from string to int
    listexp[4]=int(listexp[4])
                                                                #here we check for the operators selected by the server to send to the client 
    if listexp[3]=='+':
        sol=listexp[2]+listexp[4]
    elif listexp[3]=='-':
        sol=listexp[2]-listexp[4]
    elif listexp[3]=='*':
        sol=listexp[2]*listexp[4]
    elif listexp[3]=='/':
       sol= listexp[2]/listexp[4]
    
    result="EECE7374 RSLT " +str(sol)                        #as soon as the result is calculated it is sent to the server in the format "EECE7374 rslt and answer"
    s.send(result.encode("utf-8"))

                                                            # whenever the flag is printed from line 34 loop gets break and the connection is closed here 
s.close()







  
    


    
    



    

    




    
    
        


    





    
