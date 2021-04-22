import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()
actions = []
vector = []

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
        is_valid = is_valid and structured_command["PARAMETERS"][1] < 100
        is_valid = is_valid and structured_command["PARAMETERS"][1] > 0
    
    if structured_command["NAME"] == "MV":
        is_valid = structured_command["PARAMETERS"][0] == "R" or structured_command["PARAMETERS"][0] == "L" or structured_command["PARAMETERS"][0] == "B" or structured_command["PARAMETERS"][0] == "F"
    if structured_command["NAME"] == "STOP":
        is_valid = True
    return is_valid


def execute_command(command):
    if structured_command["NAME"] == "SET":
        i = int(structured_command["PARAMETERS"][1])
        gpg.set_speed(i)
    if structured_command["NAME"] == "STOP":
        gpg.stop()
    if structured_command["NAME"] == "MV":
        actions.append("MV"+str(structured_command["PARAMETERS"]))
        if structured_command["PARAMETERS"][0] == "R":
            gpg.turn_degrees(90)
            gpg.forward()
        if structured_command["PARAMETERS"][0] == "L":
            gpg.turn_degrees(-90)
            gpg.forward()
        if structured_command["PARAMETERS"][0] == "F":
            gpg.forward()
        if structured_command["PARAMETERS"][0] == "B":
            gpg.turn_degrees(180)
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
        vector.clear()
        command = input("Introduce command: ")
        structured_command = parse_command(command)
        print(structured_command)
        is_valid = is_valid_command(structured_command)
        print(is_valid)
        if is_valid == True:
            execute_command(command)
        vector.append(structured_command["NAME"])
        vector.append(structured_command["PARAMETERS"])
        actions.append(vector)
    if structured_command["NAME"] == "STOP":
        print("The actions you did where: ")
        for i in range(len(actions)):
            for j in range(len(actions[i])):
                print(actions[i][j])
                print("")
    
    
    
    