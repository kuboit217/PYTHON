'''Trong Python, chuỗi là những thứ được đặt trong cặp dấu ‘ ’, 
hoặc “ ”, có thể cũng là trong cặp ‘’’ ‘’’, “”” “””. 
Nhưng cơ bản và thường đường sử dụng nhất là cặp ‘ ‘ và “ “.'''
s1 = 'string'
s2 ="String"
print(s1,'\n',s2)

#chuỗi nhiều dòng

s = '''dong 1
dong 2
dong 3'''
print(s)

#chuỗi trần
# chuỗi trần, bỏ qua Escape Sequence \n
chuoiTran = r"\nếu một ngày nào đó"
print(chuoiTran)

#toán tử + chuỗi

s3 = "Python"
s3 += " Xin chào"
print(s3)

#toán tử * chuỗi
s4 ="Việt"
s4 *=4
print(s4)

#toán tử in chuỗi
#Khi sử dụng toán tử này, bạn chỉ có thể nhận được một trong hai đáp án đó là True hoặc False.

s5 ="Đinh Lang Việt"
s6 ="Việt"
s7 = s6 in s5
print(s7)

#Trong một chuỗi của Python, các kí tự tạo nên chuỗi đó sẽ được đánh số từ 0 tới n – 1 từ trái qua phải với n là số kí tự có trong chuỗi.
s8 = "abcd efgh"
print(s8[2])

'''Không chỉ đánh số từ 0 tới n – 1 từ trái qua phải với n là độ dài chuỗi, các kí tự của chuỗi còn được đánh số từ phải qua trái từ -1 đến –n với n là độ dài chuỗi.
Và cũng như trên, ta có thể truy cập bất cứ kí tự nào trong chuỗi bằng những vị trí này '''
print(s8[-2])
#lấy độ dài của chuỗi
print(len(s8))

#cắt chuối

print(s8[1:4])
print(s8[-6:-1])
#khi không biết vị trí cắt dùng None để tự động lấy hết chuỗi
print(s8[2:None])
print(s8[2:]) #nếu bỏ trống thì có thể tự hiểu là None
#nếu bỏ None ở đầu sẽ hiểu là vị trí bắt đầu
print(s8[:6])
#cắt chuỗi từ phải qua trái thì phải dùng cú pháp khác <chuỗi>[vị trí bắt đầu : vị trí dừng : bước]
print(s8[2:7:1])

#ép kiểu dữ liệu
s9 = "69"
s11 = 69
s10 = int(s9) #ép thành kiểu số nguyên
s12 = str(s11) #ép thành kiểu chuỗi
print(type(s10))
print(type(s12)) 
#nếu số thực dùng ép kiểu float

#thay đổi nội dung chuỗi
s13 = "V" + s8[1:None]
print(s13)