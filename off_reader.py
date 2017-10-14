def read_file(path):
    ret_vertices = []
    ret_faces = []
    with open(path) as file:
        identifier = file.readline()
        if identifier != "OFF":
            return -1
        numbers = file.readline()
        numbers = numbers.split()
        vertices = int(numbers[0])
        faces = int(numbers[1])
        for i in range(vertices):
            line = file.readline()
            line = line.split()
            line = [float[i] for i in line]
            ret_vertices.append((line[0], line[1], line[2]))
        for i in range(faces):
            line = file.readline()
            line = line.split()
            line = [int[i] for i in line]
            ret_faces.append((line[0], line[1], line[2]))
    return (ret_vertices, ret_faces)


def off_print(data):
'''
Takes a tuple of lists of tuples representing an off file and nicely prints it
'''


def main():




if __name__ == "__main__":
    main()
