import sys
inputs = []
with open(sys.argv[1]) as f:
    commands = f.read().splitlines()
    for line in (commands):
        line = line.replace(":", ",")
        line = list(line.split(","))
        inputs.append(line)
        
    names = sys.argv[2]
    names = names.split(",")
    for aa in names:
        xount = 0
        try:
            for i in inputs:
                if i[0] == aa:
                    xount += 1 
                    print("Name: {name}, University: {University},{Department}".format(name=i[0],University=i[1],Department=i[2]))
                else:
                    pass
            if xount == 0:
                raise IndexError(aa)
        except IndexError as aa:
            print("No record of ‘{Name}’ was found!".format(Name=aa))