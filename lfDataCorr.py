import os


class Correction:

    def __init__(self):
        self.reviewsArray = []
        self.salesArray = []

    def replaceFile(self):
        pass

    def writeFile(self):
        pass

    def readFile(self):
        pass

    def findFileReview(self):
        for reviews in os.listdir():
            if "review" in reviews and "C" not in reviews:
                self.reviewsArray.append(reviews)
        return self.reviewsArray

    def findFileSales(self):
        for sales in os.listdir():
            if "sales" in sales and "C" not in sales:
                self.salesArray.append(sales)
        return self.salesArray


a = Correction()
r = a.findFileReview()
s = a.findFileSales()
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