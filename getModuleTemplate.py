#!/usr/bin/env python3

import sys

def getModuleTemplate(moduleName):
    moduleTemplate = parseTemplate(moduleName);
    return moduleTemplate


def parseTemplate(moduleName):
    with open(f"./{moduleName}.v") as f:
        lines = f.readlines()

    print(lines)

    portListStart = 1
    for index, line in enumerate(lines):
        line = line.strip()
        if line[0:1] == "//":
            continue
        if(f"module {moduleName}") in line:
            portListStart = index + 1
            break  
    
    portList = []

    for index, line in enumerate(lines[portListStart:]):
        line = line.strip()
        portInfo = line.split(" ")

        if(portInfo[0] == ");"):
            break
        if(portInfo[0] == "input"):
            pass
        elif(portInfo[0] == "output"):
            pass
        else:
            pass

        print("Port Info")
        print(portInfo)

        # Check for a port with no width
        if len(portInfo) == 2:
            portList.append(portInfo[1].strip(","))


        # check to see if their is a port width
        endOfWidth = 1
        i = 0
        if "[" in portInfo[1]:
            if "]" in portInfo[1]:
                portList.append(portInfo[endOfWidth+1].strip(","))
                continue
            else:
                while "]" not in portInfo[i]:
                    endOfWidth = i
                    i += 1
                    print(portInfo[i])
                    continue
                portList.append(portInfo[i+1].strip(","))

        else:
            pass

        # get the port and add it to an array
        #portList.append(portInfo[endOfWidth])

    

    print("Port List")
    print(portList)
    template = formatPortList(moduleName, portList)
    return template

def formatPortList(moduleName, portList):
    template = ""

    # add in standard instantiation stuff
    template += f"{moduleName} your_inst_name (\n"

    for index, port in enumerate(portList):
        if index == len(portList)-1:
            print("here")
            template += f"\t.{port}()\n);\n"
        else:
            template += f"\t.{port}(),\n"
    
    return template


if __name__ == "__main__":
    if(len(sys.argv) != 2):
            print(f"Usage: python {sys.argc[0]} -<word>")
            sys.exit(1)

    input_word = sys.argv[1]
    result = getModuleTemplate(input_word)

    print(result)


