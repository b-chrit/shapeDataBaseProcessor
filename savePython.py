def saveObjects(fileName, shapes):
    savedFile = open(fileName, "w")
    for shape, parameters in shapes.items():
        if isinstance(parameters, list) and all(param is None for param in parameters):
            for _ in range(len(parameters)):
                savedFile.write(shape + "\n")
        elif isinstance(parameters, list) and all(isinstance(param, tuple) for param in parameters):
            for param in parameters:
                if param and any(p is not None for p in param):
                    param_str = ' '.join(str(p) for p in param if p is not None)
                    savedFile.write(shape + " " + param_str + "\n")
        else:
            if shape == "circle":
                if isinstance(parameters, tuple):
                    for param in parameters:
                        if param is not None:
                            savedFile.write(shape + " " + str(param) + "\n")
                elif isinstance(parameters, list):
                    for param in parameters:
                        if param is not None:
                            savedFile.write(shape + " " + str(param) + "\n")
                elif parameters is not None:
                    savedFile.write(shape + " " + str(parameters) + "\n")
                else:
                    savedFile.write(shape + "\n")
            else:
                if isinstance(parameters, tuple):
                    param_str = ' '.join(str(p) for p in parameters if p is not None)
                    savedFile.write(shape + " " + param_str + "\n")
                elif isinstance(parameters, list):
                    param_str = ' '.join(str(p) for p in parameters if p is not None)
                    savedFile.write(shape + " " + param_str + "\n")
                elif parameters is not None:
                    savedFile.write(shape + " " + str(parameters) + "\n")
                else:
                    savedFile.write(shape + "\n")
    savedFile.close()
