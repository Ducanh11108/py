# Truyen tham so voi cac gia tri bat buoc
# def hoanVi(a, b):
#    a, b = b, a
#    return a, b

# def main():
#    print(hoanVi(100, 50))

# main()    # def main thì phải gọi main   


# Truyen tham so voi gia tri mac dinh

# import math

# def dienTichDuongTron(r = 1):
#    s = math.pi * r * r
#    return s

# def main():
#    print("Dien tich hinh tron la: ", dienTichDuongTron())

#main()    


# Truyen tham so la tu khoa
# def tinhDienTichHCN(a, b):
#    s = a * b
#    return s

# def main()

# Truyen tham so tuy y

# Tim gia lon nhat trong cac gia tri nhap vao tu ban phim

def MaxGT(*a):
    n = len(a)
    if(n == 0):
        return
    else:
        max =  a[0]
        for i in range(1, n):
            if(max < a[i]):
                max = a[i]

    return max

def main():
    print("Gia tri lon nhat la: ", MaxGT(2,3,4,5,1,7,10,9))

main()               

