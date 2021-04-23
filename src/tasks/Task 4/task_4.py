import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()
actions = []

def parse_command(command):
    tokens = command.split()
    structured_command = {}
    name = tokens[0].upper()
    parameters = tokens[1::]
    structured_command["NAME"] = name
    structured_command["PARAMETERS"] = parameters
    return structured_command

def is_valid_command(command):
    is_valid = False
    if structured_command["NAME"] == "SET":
        is_valid = len(structured_command["PARAMETERS"]) == 2
        is_valid = is_valid and structured_command["PARAMETERS"][0].upper() == "SPEED"
        is_valid = is_valid and structured_command["PARAMETERS"][1].isnumeric()
        is_valid = is_valid and int(structured_command["PARAMETERS"][1]) < 100
        is_valid = is_valid and int(structured_command["PARAMETERS"][1]) > 0
    
    if structured_command["NAME"] == "MV":
        is_valid = structured_command["PARAMETERS"][0].upper() == "R" or structured_command["PARAMETERS"][0].upper() == "L" or structured_command["PARAMETERS"][0].upper() == "B" or structured_command["PARAMETERS"][0].upper() == "F"
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
        #actions.append("MV"+str(structured_command["PARAMETERS"]))
        if structured_command["PARAMETERS"][0].upper() == "R":
            gpg.turn_degrees(90)
            gpg.forward()
        if structured_command["PARAMETERS"][0].upper() == "L":
            gpg.turn_degrees(-90)
            gpg.forward()
        if structured_command["PARAMETERS"][0].upper() == "F":
            gpg.forward()
        if structured_command["PARAMETERS"][0].upper() == "B":
            gpg.turn_degrees(180)
            gpg.forward()

    actions.append(structured_command)
    
    return

if __name__=="__main__":
    time = 0
    while time < 100 or time > 2000:
        time = int(input("Tell me the time to wait between commands in ms, (100-2000) taking into account that you will not be able to enter a new command until the one running is finished."))
    print("The commands are:")
    print("For moving: MV and the direction (L, R, F, B)")
    print("For setting the speed: SET SPEED")
    print("For stopping the motion: STOP")
    
    
    command = input("Introduce command: ")
    structured_command = parse_command(command)
    is_valid = is_valid_command(structured_command)
    if is_valid == True:
        execute_command(command)
    while structured_command["NAME"] != "STOP":
        command = input("Introduce command: ")
        structured_command = parse_command(command)
        is_valid = is_valid_command(structured_command)
        if is_valid == True:
            execute_command(command)
            
    if structured_command["NAME"] == "STOP":
        print("The actions you have done are: ")
        #print(actions)
        for i in actions:
            if i['NAME'] == "MV":
                print("The robot has moved in direction: "+str(i["PARAMETERS"][0]))
            if i['NAME'] == "SET":
                print("The velocity was set to: "+str(i["PARAMETERS"][1]))
            if i['NAME'] == "STOP":
                print("The robot was stopped.")