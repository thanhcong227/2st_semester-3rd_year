#Nhóm 11_Bài tập 01
#Thành viên: Lê Thành Công - 20000530 - K65TT
#            Lã Mạnh Cường - 20000532 - K65TT
#            Nguyễn Tiến Đạt - 20000542 - K65TT

# Viết hàm liệt kê tất cả ước nguyên dương của một số nguyên cho trước

def uocso(n):
    print("Các ước số của",n,"la: ")
    for i in range(1,int(n/2)+1):
        if n%i==0:
            print(i,end=" ")
    print(n)

n=int(input("Nhập số nguyên dương n: "))
uocso(n)


