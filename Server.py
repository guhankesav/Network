import socket
from _thread import *
import threading
import pandas

print_lock = threading.Lock()

def threaded(c):
    while True:
        msggg = 'Welcome'
        c.sendall(msggg.encode('ascii'))
        data = c.recv(1024)
        if not data:
            print('Disconnected')
            break
        #processing
        dept = str(data.decode('ascii'))
        dept = dept.upper()
        data = c.recv(1024)
        ps = str(data.decode('ascii'))
        ps = ps.lower()
        df = pandas.read_csv('Lab2.csv')
        flag =0
        for i in range(0,len(df)):
            if(df.iloc[i,0]==dept and df.iloc[i,1]==ps):
                flag=1
                break
        if flag ==1:
            msg = 'You have connected to ' + dept + ' server'
            c.sendall(msg.encode('ascii'))
        else:
            msg = 'Sorry your password is wrong'
            c.sendall(msg.encode('ascii'))
        data = c.recv(1024)
        ss = str(data.decode('ascii'))
        if ss == 'y' :
            continue
        else:
            break
    print_lock.release()
    
        

def Main():
    HOST = '127.0.0.1'
    PORT = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print('Connected by', addr)
        start_new_thread(threaded,(c,))
    s.close()

if __name__== '__main__':
    Main()
                
                
