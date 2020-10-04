'''If là một từ tiếng Anh thường gặp, khi dịch nó ra tiếng Việt ta sẽ được nghĩa là “Nếu” hoặc 
là “Giá mà”, “Miễn là”,... Dĩ nhiên là “Nếu” là một từ chẳng mấy xa lạ với các bạn. 
Chúng ta sử dụng nó cả trăm, ngàn lần một ngày.'''

#if
print("câu lệnh if")
#if expression: 
#   # If-block
#Lưu ý: Tất cả các câu lệnh nằm trong if-block là các câu lệnh có lề thụt vào trong so với câu lệnh if.
#Ở đây, nếu expression là một giá trị khi đưa về kiểu dữ liệu Boolean là True thì Python sẽ nhảy vào thực hiện các câu lệnh trong if-block. 
# Còn nếu không thì không thì sẽ bỏ qua if-block đó.
a = 11 #int(input('Nhập vào số a: '))
if a >= 1:
    print(" a là số nguyên dương")

#If – else if
print("If – else if")
'''Ở đây, bạn có thể đặt bao nhiêu lần nếu cũng được. 
Và từ câu lệnh if đến lần elif lần thứ n – 1 (câu lệnh với n-expression) là một khối, 
ta sẽ đặt cho nó một cái tên là khối BIG để dễ hiểu.'''
if a < 0:
    print("a là số âm")
elif a == 0:
    print("a là số 0")
elif a >= 0:
    print("a là số dương")

#If - else
print("If - else")
#if expression: 
#   # If-block 
# else: 
#   # else-block
#Nếu expression là một giá trị Boolean True, thực hiện if-block và kết thúc. 
# Không quan tâm đến else-block. Còn nếu không sẽ thực hiện else-block và kết thúc.

if a >= 0:
    print("a là số dương")
else:
    print("a là số âm")

#If – else if - else
print("If – else if - else")
#Bạn có thể đặt bao nhiêu lần elif cũng được nhưng else thì chỉ một. 
# Và từ câu lệnh if đến câu lệnh else là một khối, ta cũng sẽ đặt cho nó một cái tên là khối BIG để dễ hiểu.
if 5 > a > 0:
    print("a nằm trong khoảng 0 -> 5")
elif 10 > a > 5:
    print("a nằm trong khoảng 5 ->10")
else:
    print("a không nằm trong khoảng 0 -> 10")