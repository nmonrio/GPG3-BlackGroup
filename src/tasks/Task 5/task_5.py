import time
import easygopigo3 as easy
import numpy as np

gpg = easy.EasyGoPiGo3()
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
        is_valid = is_valid and int(structured_command["PARAMETERS"][1]) < 255
        is_valid = is_valid and int(structured_command["PARAMETERS"][1]) > 0
    if structured_command["NAME"] == "MV":
        is_valid = structured_command["PARAMETERS"][0] == "R" or structured_command["PARAMETERS"][0] == "L" or structured_command["PARAMETERS"][0] == "B" or structured_command["PARAMETERS"][0] == "F"
    if structured_command["NAME"] == "STOP":
        is_valid = True
    return is_valid


def execute_command(command):
    structured_command = parse_command(command)
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

    actions.append(structured_command)
    
    return

if __name__=="__main__":
    f = open('HOLIII.txt', "w")
    lines = f.readlines()
    f.close()
    commands = []
    for i in range(len(lines)-1):
        commands.append(((lines[i])[:len(lines[i])-1:]).upper())
    commands.append("STOP")
    #print(commands)
    print("Specify the time parameters: ")
    t_direction = int(input("Time moving in the direction given (once is set to that direction): "))
    t_speed = int(input("Time moving when set new speed (the setting is inmediate): "))


    is_all_valid = True
    for command in commands:
        structured_command = parse_command(command)
        is_all_valid = is_all_valid and is_valid_command(structured_command)
    print(is_all_valid)
    if is_all_valid:
        for command in commands:
            print(command)
            execute_command(command)
            structured_command = parse_command(command)
            if structured_command['NAME'] == "SET":
                time.sleep(t_speed/1000)
            if structured_command['NAME'] == "MV":
                time.sleep(t_direction/1000)


        
