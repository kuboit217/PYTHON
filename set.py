'''Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.
Một Set gồm các yếu tố sau:
 Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
 Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
 Set không chứa nhiều hơn 1 phần tử trùng lặp
Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.'''
#Cách khởi tạo Set
#{<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>}
#Lưu ý: Khi khởi tạo bằng cách này, ít nhất phải có một giá trị.
setPy = {1,2,3,4,5}
print(setPy)
print(type(setPy))
setPy = {1, 1, 1} # các giá trị trùng lặp bị loại bỏ
print(setPy)

#Sử dụng Set Comprehension
setPy = {i for i in range(10)}
print(setPy)

#Sử dụng constructor Set
#set(iterable)
#Giống hoàn toàn với việc bạn sử dụng constructor List. Khác biệt duy nhất là constructor Set sẽ tạo ra một Set.
print("Sử dụng constructor Set")
setPy = set("Đinh Lang Việt")
print(setPy)  # set không quan tâm đến vị trí của các phần tử

#Một số toán tử với Set trong Python
print("Một số toán tử với Set trong Python")
#Toán tử in
print('Toán tử in')
#value in <Set>
#Kết quả trả về là True nếu value xuất hiện trong Set. Ngược lại sẽ là False
print("i" in setPy)

#Toán tử -
print("Toán tử -")
#<Set1> - <Set2>
#Kết quả trả về là một Set gồm các phần tử chỉ tồn tại trong Set1 mà không tồn tại trong Set2
set_1 = {1,2,3,4,5,6,7}
set_2 = {1,2,3,4,5}
set_3 = {1,2,3,4,5,6,7,8,9}
print(set_1 - set_2)
print(set_1 - set_3) #trả về set rỗng 

#Toán tử &
print("Toán tử &")
#<Set1> & <Set2
#Kết quả trả về là một Set chứa các phần tử vừa tồn tại trong Set1 vừa tồn tại trong Set2
print(set_1 & set_3)

#Toán tử |
print("Toán tử |")
#<Set1> | <Set2>
#Kết quả trả về là một Set chứa tất cả các phần tử tồn tại trong hai Set
print(set_1 | set_3)

#Toán tử ^
print("Toán tử ^")
#<Set1> ^ <Set2>
#Kết quả trả về là một Set chứa tất cả các phần tử chỉ tồn tại ở một trong hai Set
print(set_1 ^ set_3)

#Indexing và cắt Set trong Python
#việc indexing và cắt set trong Python không được hỗ trợ.

#Các phương thức của Set
#Phương thức clear
print('Phương thức clear')
#<Set>.clear()
#Loại bỏ hết tất cả các phần tử có trong Set
print(set_2.clear())

#Phương thức pop
print("Phương thức pop")
#<Set>.pop()
#Kết quả trả về một giá trị được lấy ra từ Set, đồng thời loại bỏ giá trị đã lấy ra khỏi Set ban đầu
# Nếu là set rỗng, sẽ có lỗi

print(set_3.pop())
print(set_3)

#Phương thức remove
print("Phương thức remove")
#<Set>.remove(value)
#Loại bỏ giá trị value ở trong Set. Nếu như value không ở trong Set, thông báo lên lỗi KeyError.
print(set_3.remove(2))
print(set_3)

#Phương thức discard
print("Phương thức discard")
#<Set>.discard(value)
#Loại bỏ giá trị value ở trong Set. Nếu như value không ở trong Set, thì sẽ bỏ qua.
print(set_3.discard(9))
print(set_3)

#Phương thức copy
print("Phương thức copy")
#<Set>.copy()
#Trả về một bản sao của Set
setCopy = set_3.copy()
print(setCopy)

#Phương thức add
print("Phương thức add")
#Thêm value vào trong set. Nếu như value đã có trong Set thì bỏ qua.
set_3.add(9)
print(set_3)