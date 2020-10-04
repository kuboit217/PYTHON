'''Boolean là một kiểu dữ liệu mà các ngôn ngữ lập trình ngày này đều thường xuyên sử dụng. Python cũng không ngoại lệ.
Kiểu dữ liệu này chỉ có hai giá trị:
 Một là True – có nghĩa là đúng
 Nếu không thì là False – có nghĩa là sai.
Bạn cũng đã thấy nó rồi khi sử dụng toán tử in trong các bài kiểu dữ liệu chuỗi, list,…'''

#Boolean trong các toán tử so sánh

#So sánh giữa số với số
print("So sánh giữa số với số")
'''3 > 1 là đúng
 69 < 10 là sai
 241 = 141 + 100 là đúng
 (5 x 0) ≠ 0 là sai.'''
# toán học       Python 
#  >               >
#  <               <
#  =               ==
# >=               > =
# <=                = <
# #                ! =
print(3 > 1)
print(3 <= 1)
print (3 == 2 + 1)
print((5*0) != 0) 

#So sánh giữa hai iterable cùng loại
print("So sánh giữa hai iterable cùng loại")
print("Viet" == "Việt")
print("Việt" == "Việt")

#Lưu ý: Python so sánh các kí tự với nhau bằng cách đưa chúng về dưới dạng số bằng hàm ord.
# Bạn có thể tham khảo giá trị của nó trong ASCII Table.

#Toán tử is
print("Toán tử is")
#Từ is trong tiếng Việt (ở ngữ cảnh này – ngôn ngữ lập trình Python) có nghĩa là “là”. 
# Còn toán tử == có nghĩa là bằng.
lst = [1,2,3]
lst_ = [1,2,3]
_lst = lst
print(lst_ is lst)
print(lst == lst_)
print(_lst is lst)

#Lưu ý toán tử is
#Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự dưới 20 thì các biến có cùng một giá trị sẽ có cùng một giá trị trả về từ hàm id.

#NOT, AND và OR
print("NOT, AND và OR")
#Not là phủ định.
'''Đây là cách bạn có thể đổi giá trị Boolean. Trong một số trường hợp đặc biệt. 
Việc kiểm tra giá trị Boolean đó là False hay là True hơi phức tạp, rườm ra trong khi đó việc kiểm tra
 trị ngược lại thì dễ dàng, đơn giản hơn.'''

#And là và.
#Or là hoặc

#Các giá trị cũng là các Boolean
#1 là True, 0 là False

#Syntaxnic sugar cho việc so sánh trong Python
