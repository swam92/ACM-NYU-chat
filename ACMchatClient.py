
import socket, select, string, sys, datetime
 
def prompt() :
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    this = 'acm_member_' + st + alias + ' >'
    sys.stdout.write(this)
    sys.stdout.flush()
 

if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python ACMchatClient.py hostname port alias'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
    alias = sys.argv[3]
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
   
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
           
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    
                    sys.stdout.write(data)
                    prompt()
             
        
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
                