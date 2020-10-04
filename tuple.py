#Tuple là một container cũng được sử dụng rất nhiều trong các chương trình Python không thua kém gì List.
'''Một Tuple gồm các yếu tố sau:
 Được giới hạn bởi cặp ngoặc (), tất cả những gì nằm trong đó là những phần tử của Tuple.
 Các phần tử của Tuple được phân cách nhau ra bởi dấu phẩy (,).
 Tuple có khả năng chứa mọi giá trị, đối tượng trong Python.'''
tup = (1,2,3,4,5,6,7,8,9,"Việt",["Lang","việt"])
print("Đây là tuple")
print(tup)

#Cách khởi tạo Tuple
#Sử dụng cặp dấu ngoặc () và đặt giá trị bên trong
#(<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>)
#Bạn hãy chú ý khi khởi tạo tuple với một giá trị
tup = (4) #đây là số nguyên nếu 1 giá trị
print(tup)

#Sử dụng Tuple Comprehension
tup = (i for i in range(10))
print(tup)
#Đối tượng được tạo từ Generator Expression cũng là một dạng iterable.

#Sử dụng constructor Tuple
#tuple(iterable)
#Giống hoàn toàn với việc bạn sử dụng constructor List. Khác biệt duy nhất là constructor Tuple sẽ tạo ra một Tuple.
print("Sử dụng constructor Tuple")
tup = ([1,2,3,4])
print(tup)
tup = tuple("Việt Đinh")
print(tup)
generator = (i for i in range(10) if i%2==0)
print(generator) # bạn không cần phải cố gắng hiểu khi chưa rõ comprehension
print(tuple(generator))

#Một số toán tử với Tuple trong Python
#Các toán tử của Tuple giống với toán tử của chuỗi. Nếu bạn đọc kĩ phần này ở bài List thì
# bạn sẽ thấy Kteam đề cập là toán tử của List chỉ là gần giống với toán tử của chuỗi. 
# Lí do vì sao sẽ được giải thích trong bài sự khác biệt các toán tử của hash object (immutable như chuỗi, Tuple) và unhash object (mutable như List

#Toán tử +
print("Toán tử +")
tup = (1,2,3)
tup += ("Việt","Đinh")
print(tup)

#Toán tử *
print("Toán tử *")
tup = (1,2,3)
tup *=2
print(tup)

#Toán tử in
print("Toán tử in")
tup = (1,2,3)
print(1 in tup)

#Indexing và cắt Tuple trong Python
print("Indexing và cắt Tuple trong Python")
#Indexing và cắt Tuple hoàn toàn tương tự như với kiểu dữ liệu List
tup = (1, 2, 'a', 'b', [3, 4])
print(len(tup)) #lấy độ dài phần tử trong Tuple
print("indexing", tup[4])
print("đảo ngược phải sang trái", tup[::-1])

#Thay đổi nội dung Tuple trong Python
print("Thay đổi nội dung Tuple trong Python")
#Tuple và chuỗi đều là một dạng hash object (immutable). Do đó việc bạn muốn thay đổi nội dung của nó trên lí thuyết là không.
#nếu muốn đổi giá trị trong tuple chuyển qua dạng list sẽ đổi bình thường vì list là unhash object
tup = (1,2,3)
print(tup[0] == "1")
tup = ([1,2,3],1,2)
tup[0][2] = "việt"
print(tup)
#Vì thế, một Tuple sẽ được coi là một hash object khi nó chứa các phần tử đều là hash object.

#Các phương thức của Tuple
print("Các phương thức của Tuple")
#Phương thức count
print("Phương thức count")
#<Tuple>.count(value)
print(tup.count(1))

#Phương thức index
print("Phương thức index")
#<Tuple>.index(sub[, start[, end]])
#Tương tự phương thức index của kiểu dữ liệu chuỗi.

print(tup.index(1))

#Khi nào thì chọn Tuple thay cho List?
'''Tuple khác List ở chỗ Tuple không cho phép bạn sửa chữa nội dung, còn List thì có. Vì đặc điểm đó, Tuple mạnh hơn List ở những điểm sau:
 Tốc độ truy xuất của Tuple nhanh hơn so với List
 Dung lượng chiếm trong bộ nhớ của Tuple nhỏ hơn so với List
 Bảo vệ dữ liệu của bạn sẽ không bị thay đổi
 Có thể dùng làm key của Dictonary (một kiểu dữ liệu sẽ được giới thiệu). Điều mà List không thể vì List là unhash object.
Những điểm trên là những điều giúp bạn có thể cân nhắc việc chọn Tuple hay List để lưu dữ dữ liệu dưới một mảng.'''