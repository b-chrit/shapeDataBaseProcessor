def showSummary(shapes):
    sortedShapes=dict(sorted(shapes.items()))
    for shape in sortedShapes.keys():
        print(shape.capitalize()+"(s)",":",end=" ")
        if(shape.lower()=="ellipse"):
            print(len(shapes["ellipse"]),end=" ")
            print()
        elif(shape.lower()=="rhombus"):
            print(len(shapes["rhombus"]),end=" ")
            print()
        elif(shape.lower()=="circle"):
            print(len(shapes["circle"]),end=" ")
            print()
        elif(shape.lower()=="shape"):
            print(len(shapes["circle"])+len(shapes["ellipse"])+len(shapes["rhombus"])+len(shapes["shape"]),end=" ")
            print()
