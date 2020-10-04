#kiểu số nguyên
a = 4
print(type(a))

#kiểu số thực
#Số thực trong Python có độ chính xác xấp xỉ 15 chữ số phần thập phân.
f= 1.43
print(type(f))
p = 10/3
print(p)

#Nếu bạn muốn có kết quả được chính xác cao hơn, bạn nên sử dụng Decimal
# lấy toàn bộ nội dung của thư viện Decimal
from decimal import*
getcontext().prec = 30
dec = Decimal(10)/Decimal(3)
print(dec)
print(type(dec))

'''Tuy Decimal có độ chính xác cao hơn so với float tuy nhiên nó lại khá rườm rà so với float. 
Do đó, hãy cân bằng sự tiện lợi và chính xác để chọn kiểu dữ liệu phù hợp.'''

#Để tạo phân số trong python, ta sử dụng hàm Fraction với cú pháp sau

from fractions import *
fac = Fraction(1,10)
print(fac)
print(type(fac))

#toán tử trong py
m =10
n=3
print("Toán tử trong Py")
print(m+n)
print(m-n)
print(m*n)
print(m/n)
print(m//n)
print(m%n)
print(m**n)

#Thư viện math trong Python hỗ trợ rất nhiều hàm tính toán liên quan đến toán học.
# lấy nội dung của thư viện math về sử dụng
import math
y =3.99
i = 3
x =2
print(math.trunc(y)) #trả về số nguyên là phần nguyên của số y
print(math.floor(y)) #trả về số nguyên được làm trong từ y, luôn nhỏ hơn hoặc bằng y
print(math.ceil(y)) #trả về số nguyên được làm tròn từ y, luôn lớn hơn hoặc bằng y
print(math.fabs(y)) #trả về số thực là giá trị tuyệt đối của y
print(math.sqrt(y)) #trả về số thực là căn bậc 2 của y
print(math.gcd(x,i)) #trả về số nguyên là ước số chung của x và i




