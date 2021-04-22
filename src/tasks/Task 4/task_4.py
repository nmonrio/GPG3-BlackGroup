import time
import easygopigo3 as easy
import gopigo

GPG = gopigo3.GoPiGo3()
actions = []


def parse_command(command):
    tokens = command.split()
    structured_command = {}
    name = tokens[0]
    parameters = tokens[1::]
    structured_command["NAME"] = name
    structured_command["PARAMETERS"] = parameters
    return structured_command

def is_valid_command(command):
    is_valid = False
    if structured_command["NAME"] == "SET":
        is_valid = len(structured_command["PARAMETERS"]) == 2
        is_valid = is_valid and structured_command["PARAMETERS"][0] == "SPEED"
        is_valid = is_valid and structured_command["PARAMETERS"][1].isnumeric()
    
    if structured_command["NAME"] == "MV":
        is_valid = structured_command["PARAMETERS"][0] == "R" or structured_command["PARAMETERS"][0] == "L" or structured_command["PARAMETERS"][0] == "B" or structured_command["PARAMETERS"][0] == "F"
    if structured_command["NAME"] == "STOP":
        is_valid = True
    return is_valid


def execute_command(command):
    if structured_command["NAME"] == "SET":
        i = int(structured_command["PARAMETERS"][1])
        gpg.robot(i)
    if structured_command["NAME"] == "STOP":
        gpg.stop()
    if structured_command["NAME"] == "MV":
        actions.append("MV"+str(structured_command["PARAMETERS"]))
        if structured_command["PARAMETERS"][0] == "R":
            gpg.rotate_degrees(90)
            gpg.forward()
            gpg.sleep(1)
        if structured_command["PARAMETERS"][0] == "L":
            gpg.rotate_degrees(-90)
            gpg.forward()
        if structured_command["PARAMETERS"][0] == "F":
            gpg.rotate_degrees(0)
            gpg.forward()
        if structured_command["PARAMETERS"][0] == "B":
            gpg.rotate_degress(180)
            gpg.forward()
    
    return

if __name__=="__main__":
    print("The commands are:")
    print("For moving: MV and the direction (L, R, F, B)")
    print("For setting the speed: SET SPEED")
    print("For stopping the motion: STOP")
    
    
    command = input("Introduce command: ")
    structured_command = parse_command(command)
    print(structured_command)
    is_valid = is_valid_command(structured_command)
    print(is_valid)
    if is_valid == True:
        execute_command(command)
    while structured_command["NAME"] != "STOP":
        command = input("Introduce command: ")
        structured_command = parse_command(command)
        print(structured_command)
        is_valid = is_valid_command(structured_command)
        print(is_valid)
        if is_valid == True:
            execute_command(command)
    
    
    
    