import os


def find_file(file_type):
    os.chdir(appPath)
    for filename in os.listdir():
        if file_type in filename:
            file_array.append(filename)
    return file_array


file_array = []
appPath = os.getcwd() + "/output"
file_array_all = find_file('txt')
for file_name in file_array:
    read_file = open(file_name, 'r')
    write_file = open('C' + file_name.replace('txt', 'json'), 'w')
    try:
        for line in read_file:
            print(line.replace("'", '"'), file=write_file, end="")
        os.remove(file_name)
        os.
    except (RuntimeError, TypeError, NameError, BrokenPipeError):
        print("Correction Error")
    finally:
        read_file.close()
        write_file.close()