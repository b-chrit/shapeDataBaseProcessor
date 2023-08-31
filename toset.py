from savePython import saveObjects
def toSet(shapes):
    for shape, params_list in shapes.items():
        unique_params = list(set(params_list))
        shapes[shape] = unique_params

    # for shape,parameters in shapes.items():
    #     print(shape," ")
    #     for param in parameters:
    #         print(param," ")

    saveObjects("output.txt",shapes)

