from classes import*
def printObjects(shapes):
    Shape.id=1
    # print(shapes)
    for shape in shapes.keys():
        if(shape.lower()=="circle"):
            circleParameters=shapes["circle"]
            for parameter in circleParameters:
                radius=parameter
                c=Circle(radius)
                c.print()
        elif(shape.lower()=="ellipse"):
            ellipse_param=shapes["ellipse"]
            for parameter in ellipse_param:
                semiMajor,semiMinor=parameter
                e=Ellipse(semiMajor,semiMinor)
                e.print()
        elif(shape.lower()=="rhombus"):
            rhombusParameter=shapes["rhombus"]
            for parameter in rhombusParameter:
                diagnol1,diagnol2=parameter
                r=Rhombus(diagnol1,diagnol2)
                r.print()
        elif(shape.lower()=="shape"):
            for shape, parameters in shapes.items():
                if isinstance(parameters, list) and all(param is None for param in parameters):
                    for _ in range(len(parameters)):
                        s=Shape()
                        s.print()
                    
