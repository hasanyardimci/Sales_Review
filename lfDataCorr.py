import os


class CorrectionReview:

    def __init__(self):
        self.file_array = []
        self.appPath = os.getcwd() + "/output"

    def replaceFile(self):
        pass

    def writeFile(self):
        pass

    def readFile(self):
        pass

    def find_file(self, file_type, flag_letter):
        self.file_array = []
        os.chdir(self.appPath)
        for file_name in os.listdir():
            if file_type in file_name and flag_letter not in file_name:
                self.file_array.append(file_name)
        return self.file_array


a = CorrectionReview()
r = a.find_file('review','C')
s = a.find_file('sales', 'S')
print(r)
print(s)

'''
reviewRead = open('/Users/hsn/Desktop/MyRepos/Sales_Review/output/review_1570448292.txt', 'r')
reviewWrite = open('/Users/hsn/Desktop/MyRepos/Sales_Review/output/review_1570448292C.json', 'w')

try:
    for line in reviewRead:
        print(line.replace("'", '"'), file=reviewWrite, end="")
        os.remove('/Users/hsn/Desktop/MyRepos/Sales_Review/output/review_1570448292.txt')
except (RuntimeError, TypeError, NameError, BrokenPipeError):
    print("Correction Error")
finally:
    reviewRead.close()
    reviewWrite.close()
'''