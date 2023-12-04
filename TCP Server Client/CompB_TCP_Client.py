"""
Created on Fri Dec  1 07:46:12 2023

@author: kılıçaslan


Comp B TCP Client
"""

import scapy
import time

Targethost = '127.0.0.1' # IP address of  server
TargetPort = 200 #  server import socket

State = "CLOSED"  # initial state, always

Autom = {("CLOSED","APP_PASSIVE_OPEN"):"LISTEN",   # defines states of 3-way TCP Communication
          ("CLOSED","APP_ACTIVE_OPEN"):"SYN_SENT",
          ("LISTEN","RCV_SYN"):"SYN_RCVD",
          ("LISTEN","APP_SEND"):"SYN_SENT",
          ("LISTEN","APP_CLOSE"):"CLOSED",
          ("SYN_RCVD","APP_CLOSE"):"FIN_WAIT_1",
          ("SYN_RCVD","RCV_ACK"):"ESTABLISHED",
          ("SYN_SENT","RCV_SYN"):"SYN_RCVD",
          ("SYN_SENT","RCV_SYN_ACK"):"ESTABLISHED",
          ("SYN_SENT","APP_CLOSE"):"CLOSED",
          ("ESTABLISHED","APP_CLOSE"):"FIN_WAIT_1",
          ("ESTABLISHED","RCV_FIN"):"CLOSE_WAIT",
          ("FIN_WAIT_1","RCV_FIN"):"CLOSING",
          ("FIN_WAIT_1","RCV_FIN_ACK"):"TIME_WAIT",
          ("FIN_WAIT_1","RCV_ACK"):"FIN_WAIT_2",
          ("CLOSING","RCV_ACK"):"TIME_WAIT",
          ("FIN_WAIT_2","RCV_FIN"):"TIME_WAIT",
          ("TIME_WAIT","APP_TIMEOUT"):"CLOSED",
          ("CLOSE_WAIT","APP_CLOSE"):"LAST_ACK",
          ("LAST_ACK","RCV_ACK"):"CLOSED"}


# State transition function
def traverse_TCP_states(events):  
   
    for Event in Events:
        if (State,Event) in Autom:
            State = Autom[State,Event]
        else:
            return "ERROR"
    return State



Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket connection

# Client.connect((target_host, target_port)) # let the client connect

Msg = bytearray()

Msg.append(b'10001000100010001000100010001000') # CompB Client data


  

while(True):
        
    match state: # switch-case structure between states
        
        case "CLOSED":  #make client connection
   
            traverse_TCP_states("APP_ACTIVE_OPEN")
    
        case "SYN_SENT":   # SYN sent to server 
        
            
            SYN=Targethost/TCP(sport=TargetPort, dport=80, flags="S", seq=42)
            SYNACK=sr1(Targethost/SYN)  #send SYN
            
            
            ACK=Targethost/TCP(sport=SYNACK.TargetPort, dport=80, flags="A", 
                               seq=SYNACK.ack, ack=SYNACK.seq + 1) #receive SYN+ACK
            
            if(ACK)
                traverse_TCP_states("RCV_SYN_ACK")
            else:
                State = "SYN_SENT"
        
    
        case "ESTABLISHED":  #data communication block after handshake
     
            sr(Targethost/ACK) # Send 3rd handshake for start receiving data
                                  
            ServerData = bytearray(ans)   #receive CompA server data
            
            if(Server_data):
                ACK=Targethost/TCP(sport=ACK.TargetPort, dport=80, flags="A", 
                                   seq=ACK.ack, ack=ACK.seq + 1)  #send ACK for received data
                         
     
            sR(Targethost/TCP()/Msg)  #send CompB client data   
   
             
            if (ans):          # received ACK then start closing procedure
                traverse_TCP_states("APP_CLOSE")
            else:
                State = "ESTABLISHED" 
        
        
        case "FIN_WAIT_1":    # send finish command 
        
              FIN=Targethost/TCP(sport=TargetPort, dport=80, flags="FA", 
                                 seq=SYNACK.ack, ack=SYNACK.seq + 1)
          
             
              FINACK=sr(FIN)
             
              if(FINACK)
                  traverse_TCP_states("RCV_ACK") 
              else:
                  State := "FIN_WAIT_1"
                  
        case "FIN_WAIT_2":  # receive finish from server
            if(FINACK)
                   traverse_TCP_states("RCV_FIN")
            else:
                State := "FIN_WAIT_2"
                
        case "TIME_WAIT": #sent last ACK for finish after 100ms
            time.sleep(100)
            LASTACK=Targethost/TCP(sport=TargetPort, dport=80, 
                                   flags="A", seq=FINACK.ack, ack=FINACK.seq + 1)
            send(LASTACK)
            traverse_TCP_states("APP_TIMEOUT") # send back to close stated for new data communication
                   
        
         
         
         

                
          
    
             

             
             
              
            
            
            
          
            
        
            
         
    
            
           
        
        
        
         
        
    
        
    
    
       
    
    
    
    


