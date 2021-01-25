import socket

def Main():
    HOST = '127.0.0.1'
    PORT = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    print('Trying to Connect to the Server')
    while True:
        data = s.recv(1024)
        dt=''
        dt = str(data.decode('ascii'))
        print(dt)
        dept = input('\nEnter your Department:')
        ps = input('\nEnter the password:')
        s.send(dept.encode('ascii'))
        s.send(ps.encode('ascii'))
        msg = s.recv(1024)
        msgg = str(msg.decode('ascii'))
        print(msgg)
        ans = input('\nDo you want to continue(y/n) :') 
        s.send(ans.encode('ascii'))
        if ans == 'y': 
            continue
        else: 
            break
    s.close()

if __name__== '__main__':
    Main()
