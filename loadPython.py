from collections import defaultdict
from classes import *

def loadObjects(fileName):
    invoke = 0
    shapes = defaultdict(list)
    error_count = 0
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        print("File does not exist, please try again and make sure the file you wish to read from exists!")
        return shapes

    try:
        file_contents = file.read()
        lines = file_contents.split("\n")

        for line_num, line in enumerate(lines, start=1):
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:
                continue  # Skip empty lines

            words = line.split()

            shape_type = words[0].lower()

            if shape_type == "circle":
                if len(words) < 2:
                    error_count += 1
                    print(f"Circle at line {line_num} does not have a radius.")
                    continue
                radius = int(words[1])
                if radius < 0:
                    error_count += 1
                    print(f"Circle at line {line_num} has a negative radius of {radius}.")
                    continue  # Skip negative radius
                shapes["circle"].append(radius)
            elif shape_type == "rhombus":
                if len(words) < 3:
                    error_count += 1
                    print(f"Rhombus at line {line_num} does not have sufficient parameters.")
                    continue  # Skip lines with insufficient data for rhombus
                diagonal1 = int(words[1])
                diagonal2 = int(words[2])
                if diagonal1 < 0 or diagonal2 < 0:
                    error_count += 1
                    print(f"Rhombus at line {line_num} has negative diagonals: {diagonal1}, {diagonal2}.")
                    continue  # Skip negative diagonals
                shapes["rhombus"].append((diagonal1, diagonal2))
            elif shape_type == "ellipse":
                if len(words) < 3:
                    error_count += 1
                    print(f"Ellipse at line {line_num} does not have sufficient parameters.")
                    continue  # Skip lines with insufficient data for ellipse
                semi_major = max(int(words[1]), int(words[2]))
                semi_minor = min(int(words[1]), int(words[2]))
                if semi_major < 0 or semi_minor < 0:
                    error_count += 1
                    print(f"Ellipse at line {line_num} has negative semi-major or semi-minor axes: {semi_major}, {semi_minor}.")
                    continue  # Skip negative semi-major or semi-minor
                shapes["ellipse"].append((semi_major, semi_minor))
            elif shape_type == "shape":
                if len(words) > 1:
                    error_count += 1
                    print(f"Shape at line {line_num} has a parameter")
                    continue
                shapes["shape"].append(None)

        num_rows = sum(1 for line in lines if line.strip())  # Count non-empty lines
        num_shapes = sum(len(params) for params in shapes.values())
        if invoke == 0:
            print(f"Processed {num_rows} row(s), {num_shapes} shape(s) added, {error_count} error(s).\n")

        invoke += 1
        return shapes
    finally:
        file.close()
