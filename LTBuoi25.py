# Bài 1. Xây dựng hàm tìm số nguyên tố và in ra tất cả các số nguyên tố từ 2 đến 100.

import math
def soNT(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def main():
    for i in range(2, 1001):
        if(soNT(i) == True):
            print(i, " ", end = "")    

main()    