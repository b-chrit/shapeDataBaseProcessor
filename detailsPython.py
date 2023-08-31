def showDetails(shapes):
    for shape, parameters in shapes.items():
        if isinstance(parameters, list) and all(param is None for param in parameters):
            print(shape)
        elif isinstance(parameters, list) and all(isinstance(param, tuple) for param in parameters):
            for param in parameters:
                if param and any(p is not None for p in param):
                    param_str = ' '.join(str(p) for p in param if p is not None)
                    print(shape + " " + param_str)
        else:
            if isinstance(parameters, tuple):
                if parameters and any(p is not None for p in parameters):
                    param_str = ' '.join(str(p) for p in parameters if p is not None)
                    print(shape + " " + param_str)
            elif isinstance(parameters, list):
                for param in parameters:
                    if param is not None:
                        print(shape + " " + str(param))
            elif parameters is not None:
                print(shape + " " + str(parameters))
            else:
                print(shape)
