import socket
import easygopigo3 as easy
gpg = easy.EasyGoPiGo3()
import math
import time

HOST = '10.10.10.10'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023) 

factor = 1

def movement(grid):
    k = 1
    gpg.set_speed(255)
    initial = [0,0]
    final = [0, 0]
    while True:
        n = len(grid)
        initial = final
        for i in range(n):
            for j in range(n):
                if grid[i][j] == k:
                    final = [i, j]
                    x_diff = (final[0]-initial[0])*100
                    y_diff = (final[1]-initial[1])*100
                    print("y_diff:",y_diff)
                    print("x_diff:",x_diff)
                    angle = math.atan(x_diff/y_diff)*180/3.1415
                    print(round(angle,3))
                    gpg.rotate(angle)
                    wait_seconds(2)
                    gpg.forward()
                    wait_seconds((i**2+j**2)**0.5/50*factor)
                    gpg.stop()
                    gpg.rotate(-angle)
                    wait_seconds(5)
        k += 1

def wait_seconds(my_time):
    t0 = time.time()
    t_diff= 0
    while t_diff < my_time:
        t_diff = time.time()-t0
        gpg.forward()
        print(round(t_diff,5), end = "\r")
    print("Waited",t_diff,"seconds")

def string_to_list(string_list):
    l = string_list.split("[")
    l = [ [i.strip("],")] for i in l if i]
    for j in range(len(l)):
        l[j] = l[j][0].split(",")
        for k in range(len(l[j])):
            try:
                l[j][k] = int(l[j][k].strip("], "))
            except:
                l[j].remove(l[j][k])
    return l

if __name__=="__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept() 
            with conn:
                print('Connected by', addr)
                grid_string = ""
                while True:
                    rawdata = conn.recv(1024)
                    data = repr(rawdata)
                    datarefined = data[2:len(data)-1:]
                    #print("Received",datarefined)
                    conn.sendall(bytes("Executing", 'utf-8'))
                    if not rawdata:
                        break
                    else:
                        #print(datarefined)
                        #print(type(datarefined))
                        grid_string += datarefined
                    grid_list = string_to_list(grid_string)
                    
                    print(grid_list)
                    print(len(grid_list),len(grid_list[0]))
                    movement(grid_list)
                    #movement(datarefined)
                    #conn.sendall(bytes("Executing", 'utf-8'))