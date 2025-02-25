# Bài 2
# 2. Viết chương trình quản lý học sinh thực hiện các chức năng sau:
# Nhập danh sách học sinh gồm các thông tin: Mã học sinh, tên học sinh, điểm toán, điểm tiếng Việt
# Tính điểm trung bình bằng (điểm Toán + điểm Tiếng Việt) / 2
# Xếp loại học sinh theo điểm trung bình, điều kiện xếp loại như sau:
# Nếu điểm trung bình lớn hơn hoặc bằng 9 thì xếp loại Xuất sắc
# Nếu điểm trung bình lớn hơn hoặc bằng 8 và nhỏ hơn 9 thì xếp loại Giỏi
# Nếu điểm trung bình ớn hơn hoặc bằng 7 và nhỏ hơn 8 thì xếp loại Khá
# Nếu điểm trung bình ớn hơn hoặc bằng 5 và nhỏ hơn 7 thì xếp loại Trung bình
# Nếu điểm trung bình nhỏ hơn 5 thì xếp loại Yếu
# In thông tin của các học sinh ra màn hình



def nhapTTHS():
    # Nhap ma HS
    while(True):
        maHS = input("Moi ban nhap ma HS: ")
        if(len(maHS.strip()) > 0):
            break
    # Nhap ma HS
    while(True):
        tenHS = input("Moi ban nhap ten HS: ")
        if(len(tenHS.strip()) > 0):
            break

    # Nhap diem toan 
    while(True):
        diemToan = float(input("Moi ban nhap vao diem Toan: "))
        if(0 <= diemToan <= 10):
            break
    # Nhap diem tieng Viet
    while(True):
        diemTV = float(input("Moi ban nhap vao diem Tieng Viet: "))
        if(0 <= diemTV <= 10):
            break    
    return {"MaHS" : maHS, "TenHS" : tenHS, "DiemToan" : diemToan, "DiemTV" : diemTV}

def nhapDSHS():
    dsHS = []
    while(True):
        n = int(input("Moi ban nhap vao so luong HS: "))
        if (n > 0):
            break

    for i in range(1, n + 1):
        print("Nhap vao thong tin cua hoc sinh thu", i)
        dsHS.append(nhapTTHS)

    return dsHS

def diemTB(diemToan, diemTV):
    return round((diemToan + diemTV) / 2,2)

def xepLoai(dtb):
    xl = ""
    if(9 <= dtb <= 10):
        xl = "Xuat sac"
    elif(8 <= dtb < 9):
        xl = "Gioi"
    elif(7 <= dtb < 8):
        xl = "Kha"
    elif(5 <= dtb < 7):
        xl = "Trung binh"
    else:
        xl = "Yeu"   

    return xl   

def inTTHS(dsHS):
    for i in range(len(dsHS)):
        print("Thong tin cua hoc sinh thu", i)
        print("Ma HS la:", dsHS[i]["MaHS"])                      
        print("Ten HS la:", dsHS[i]["TenHS"])                      
        print("Diem Toan la:", dsHS[i]["DiemToan"])                      
        print("Diem Tieng Viet la:", dsHS[i]["DiemTV"])                      
        dtb = diemTB( dsHS[i]["DiemToan"], dsHS[i]["DiemTV"])
        print("Diem trung binh la:", dtb)
        print("Hoc sinh xep loai:", xepLoai(dtb))

def main():
    dsHS = nhapDSHS()
    inTTHS(dsHS)

main()          