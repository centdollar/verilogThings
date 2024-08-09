#!/usr/bin/env python3
import re
import sys

# get the module instantiation template
def getModuleTemplate(moduleName):
    moduleTemplate = parseTemplate(moduleName);
    return moduleTemplate

# Splits the file into valid tokens for creating the module template
def tokenize(file):
    tokens = []
    for line in file:
        splitLine = re.split(r'[ \t]', line)

        
        #splitLine = line.split('\t')
        while len(splitLine):
           token = splitLine[0]
           token = re.sub(r'[\n\t]', '', token)

           # handle comments
           if "//" in token:
               splitLine = []
               continue
           else:
               if token:
                   tokens.append(token)
               splitLine = splitLine[1:]
    return tokens

def createModuleTemplate(tokens):
    template = ""
    print(tokens)
    for index, token in enumerate(tokens):
        # Find module header
        if "module" in token and "endmodule" not in token:
            moduleDeclStart = index
        if ");" in token:
            moduleDeclEnd = index
            break
    tokens = tokens[moduleDeclStart:moduleDeclEnd+1]
    paramsList = []
    portList = []
    while len(tokens):
        if "module" in tokens[0]:
            template += tokens[1]
            tokens = tokens[2:]
            continue
        if "#(" in tokens[0]:
            numParamTokens = 1
            paramTokens = tokens[1:]
            err = 0
            while paramTokens[0] != ")":
                if "parameter" in paramTokens[0] and "=" in paramTokens[2]:
                    paramsList.append([paramTokens[1], paramTokens[3].strip(",")])
                    paramTokens = paramTokens[4:]
                    numParamTokens += 4
                    continue
                else:
                    print("Error")
                    err += 1
                    if(err > 5):
                        quit()
            tokens = tokens[numParamTokens+1:]

        if "(" in tokens[0]:
            portTokens = tokens[1:]

            portSize = ""
            portType = ""
            reg = "" 
            while ");" not in portTokens[0]:
                if "input" or "output" in portTokens[0]:
                    portType = portTokens[0]
                    portTokens = portTokens[1:]
                    continue
                elif "reg" in portTokens[0]:
                    portTokens = portTokens[1:]
                    reg = "reg"
                    continue
               

                elif '[' in portTokens[0]:
                    print(portTokens[0])
                    if ']' in portTokens[0]:
                        portSize = portTokens[0]
                        portTokens = portTokens[2:]
                        continue
                    else:
                        for tok, idx in portTokens:
                            if ']' in tok:
                                portSize += ''.join(portTokens[:idx])
                                print("here")
                                portTokens = portTokens[:idx]
                                break
                        continue
                        
                else:
                    portName = portTokens[0].strip(',')
                    portList.append([portName,portType,portSize,reg])
                    portTokens = portTokens[1:]
                    reg = ''
                    continue


        tokens = []

        if paramsList:
            template += " #(\n"
            for index, param in enumerate(paramsList):
                if index == len(paramsList)-1:
                    template += f"\t.{param[0]}()\t// defualt={param[1]}\n)\n"
                else:
                    template += f"\t.{param[0]}(),\t// defualt={param[1]}\n"

        template += "inst_name\n"
        template += "(\n"
        for index, port in enumerate(portList):
            if index == len(portList)-1:
                template += f"\t.{port[0]}()\t// {port[2]} {port[3]}:{port[1]}\n);\n"
            else:
                template += f"\t.{port[0]}(),\t// {port[2]} {port[3]}:{port[1]}\n"
    return (template)

'''
                if "[" in portTokens[0] and "]" in portTokens[0]:
                    portSize += portTokens[0]
                    portList.append([portTokens[1].strip(","), ':'+portSize, portType])
                    portTokens = portTokens[2:]
                    continue
                if "[" in portTokens[0]:
                    portSize += portTokens[0]
                    portTokens = portTokens[1:]
                    while "]" not in portTokens[0]:
                        portSize += portTokens[0]
                        portTokens = portTokens[1:]
                    portSize += portTokens[0] 
                    portList.append([portTokens[1].strip(","), ':'+portSize, portType])
                    portTokens = portTokens[2:]
                    continue
                else:
                    portList.append([portTokens[0].strip(","), "", portType])
                    portTokens = portTokens[1:]
                    continue
                    '''


# Return a inst template from a given module name
def parseTemplate(moduleName):

    # open file based
    with open(f"./{moduleName}.v") as f:
        lines = f.readlines()

    tokens = tokenize(lines)

    template = createModuleTemplate(tokens)
    return template 


if __name__ == "__main__":
    if(len(sys.argv) != 2):
            print(f"Usage: python {sys.argc[0]} -<word>")
            sys.exit(1)

    input_word = sys.argv[1]
    result = getModuleTemplate(input_word)

    print(result)


