import socket
import easygopigo3 as easy
my_gpg3 = easy.EasyGoPiGo3()
#HOST = '127.0.0.1'
HOST = '10.10.10.10'  # Standard loopback interface address (localhost)
PORT = 65434        # Port to listen on (non-privileged ports are > 1023)
#GPG = gopigo3.GoPiGo3() 

def forward():
    my_gpg3.forward()

def backward():
    my_gpg3.backward()

def left():
    my_gpg3.left()

def right():
    my_gpg3.right()

def stop():
    my_gpg3.stop()

def forwardRight():
    my_gpg3.set_motor_power(1, 100)#left
    my_gpg3.set_motor_power(2, 80)#right

def forwardLeft():
    my_gpg3.set_motor_power(1, 80)#left
    my_gpg3.set_motor_power(2, 100)#right

def backwardRight():
    my_gpg3.set_motor_power(1, -100)#left
    my_gpg3.set_motor_power(2, -80)#right

def backwardLeft():
    my_gpg3.set_motor_power(1, -80)#left
    my_gpg3.set_motor_power(2, -100)#right

def program1():
    pass

def program2():
    pass

def program3():
    pass

def task2():
    pass

def task3():
    pass

def task4():
    pass

def task5():
    pass

def task6():
    pass

def sliders(values):
    my_gpg3.set_motor_power(1, values[0])#left
    my_gpg3.set_motor_power(2, values[1])#right

if __name__=="__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True: #Add timeout to this infinite loop
            conn, addr = s.accept() 
            with conn:
                print('Connected by', addr)
                while True:
                    rawdata = conn.recv(1024)
                    data = repr(rawdata)
                    datarefined = data[2:len(data)-1:]
                    print("Received",datarefined)
                    if not rawdata: #fix this so it isn't so brute force
                        break
                    if datarefined == "w":
                        conn.sendall(bytes("Forward", 'utf-8'))
                        forward()
                    elif datarefined == "s":
                        conn.sendall(bytes("Backward", 'utf-8'))
                        backward()
                    elif datarefined == "a":
                        conn.sendall(bytes("Left", 'utf-8'))
                        left()
                    elif datarefined == "d":
                        conn.sendall(bytes("Right", 'utf-8'))
                        right()
                    elif datarefined == "q":
                        conn.sendall(bytes("Forward Left", 'utf-8'))
                        forwardLeft()
                    elif datarefined == "e":
                        conn.sendall(bytes("Forward Right", 'utf-8'))
                        forwardRight()
                    elif datarefined == "z":
                        conn.sendall(bytes("Backward Left", 'utf-8'))
                        backwardLeft()
                    elif datarefined == "x":
                        conn.sendall(bytes("Backward Right", 'utf-8'))
                        backwardRight()
                    elif datarefined == " ":
                        conn.sendall(bytes("Stop", 'utf-8'))
                        stop()                    
                    elif datarefined == "1":
                        conn.sendall(bytes("Program 1", 'utf-8'))
                        program1()
                    elif datarefined == "2":
                        conn.sendall(bytes("Program 2", 'utf-8'))
                        program2()
                    elif datarefined == "3":
                        conn.sendall(bytes("Program 3", 'utf-8'))
                        program3()
                    elif datarefined[0] == "l":
                        try:
                            motors = []
                            motor = ""

                            for i in str(datarefined):
                                if i == "l":
                                    pass
                                elif i == "r":
                                    motors.append(int(motor))
                                    motor = ""
                                else:
                                    motor = motor+i

                            motors.append(int(motor))
                            
                            sliders(motors)
                            print("Setting Left Motor to "+str(motors[0])+" and Right Motor to "+str(motors[1]))
                            m = "Setting Left Motor to "+str(motors[0])+" and Right Motor to "+str(motors[1])
                            conn.sendall(bytes(m, 'utf-8'))
                        except:
                            print("Error")
                    elif datarefined[0:4:] == "task":
                        if datarefined[4] == "2":
                            task2()
                        elif datarefined[4] == "3":
                            task3()
                        elif datarefined[4] == "4":
                            task4()
                        elif datarefined[4] == "5":
                            task5()
                        elif datarefined[4] == "6":
                            task6()
                        
                        m = "Executing Task "+str(datarefined[4])
                        print(m)
                        conn.sendall(bytes(m, 'utf-8'))
                    else:
                        conn.sendall(bytes("Unknown", 'utf-8'))
