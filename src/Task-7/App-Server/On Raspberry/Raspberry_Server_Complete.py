import socket
import easygopigo3 as easy
my_gpg3 = easy.EasyGoPiGo3()
#HOST = '127.0.0.1'
HOST = '10.10.10.10'  # Standard loopback interface address (localhost)
PORT = 65439        # Port to listen on (non-privileged ports are > 1023)

my_distance_sensor = my_gpg3.init_distance_sensor('AD1')
gpg_servo = my_gpg3.init_servo('SERVO1')
servo_pos = 90
gpg_servo.rotate_servo(servo_pos)

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

def sliders(values):
    my_gpg3.set_motor_power(1, values[0])#left
    my_gpg3.set_motor_power(2, values[1])#right

def measure():
    return my_distance_sensor.read_mm()

def rotateservo(a,current_pos):
    if a == "h":
        current_pos = 90
    elif a == "l":
        current_pos=current_pos-10# If input is 'l' move the servo left 10 degrees.
    elif a=='r':
        current_pos=current_pos+10# If the input is 'r' move the servo right by 10 degrees.
    else:
        pass
    #Get the servo angles back to the normal 0 to 180 degree range
    if current_pos>180:
        current_pos=180
    if current_pos<0:
        current_pos=0

    gpg_servo.rotate_servo(current_pos)# This function updates the servo with the latest positon.  Move the servo.
    return current_pos

    

if __name__=="__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept() 
            with conn:
                print('Connected by', addr)
                while True:
                    rawdata = conn.recv(1024)
                    data = repr(rawdata)
                    datarefined = data[2:len(data)-1:]
                    print("Received",datarefined)
                    if not rawdata:
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
                            #print("Setting Left Motor to "+str(motors[0])+" and Right Motor to "+str(motors[1]))
                            m = "Setting Left Motor to "+str(motors[0])+" and Right Motor to "+str(motors[1])
                            conn.sendall(bytes(m, 'utf-8'))
                        except:
                            print("Error")
                    elif datarefined[0:5:] == "servo":
                        servo_pos = rotateservo(datarefined[5],servo_pos)
                        m = "Rotating Servo"
                        conn.sendall(bytes(m, 'utf-8'))
                    elif datarefined == "measure":
                        m = "sensor"+str(measure())
                        print(m)
                        conn.sendall(bytes(m, 'utf-8'))
                    else:
                        conn.sendall(bytes("Unknown", 'utf-8'))
