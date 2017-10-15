def read_file(path):
    '''
    Takes a path to an off file. reads the data in and returns a tuple
    containing a list of points and a list of faces
    '''
    ret_vertices = []
    ret_faces = []
    with open(path) as file:
        identifier = file.readline().strip()
        if identifier != "OFF":
            return -1
        numbers = file.readline()
        numbers = numbers.split()
        vertices = int(numbers[0])
        faces = int(numbers[1])
        for i in range(vertices):
            line = file.readline()
            line = line.split()
            line = [float(i) for i in line]
            ret_vertices.append((line[0], line[1], line[2]))
        for i in range(faces):
            #DOESNT WORK
            #seems the first num on the line represents how many come after
            #need to account for that
            line = file.readline()
            line = line.split()
            line = [int(i) for i in line]
            ret_faces.append((line[0], line[1], line[2]))
    return (ret_vertices, ret_faces)


def off_print(data):
    '''
    Takes a tuple of lists of tuples representing an off file and nicely prints it
    '''
    for l in data:
        for points in l:
            print('x: {0}, y: {1}, z: {2}'.format(points[0], points[1], points[2]))


def main():
    test = read_file("chair_0890.off")
    if test == -1:
        print("Error")
        return -1
    off_print(test)




if __name__ == "__main__":
    main()
