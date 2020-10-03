#Các phương thức tiện ích
lst = [1,2,3,4,5,6,7,8,9,10]
print(lst)
#Phương thức count
#<List>.count(sub, [start, [end]])
#Giống với phương thức count của kiểu dữ liệu chuỗi.
# Trả về một số nguyên, chính là số lần xuất hiện của sub trong chuỗi.
# Còn start và end là số kĩ thuật slicing (lưu ý không hề có bước).
count = lst.count(1)
print("Phương thức count")
print(count)

#Phương thức index
#<List>.index(sub[, start[, end]])
#Tương tự phương thức index của kiểu dữ liệu chuỗi.
print("Phương thức index")
index = lst.index(4)
print(index)

#Phương thức copy
#<List>.copy()
#Trả về một List tương tự với List[:]
print("Phương thức copy")
copy = lst.copy()
print(copy)

#Phương thức clear
#<List>.clear()
#Xóa mọi phần tử có trong List.
print("Phương thức clear")
clear = copy.clear()
print(clear)
#Phương thức trên bản chất không như những cách gán với một List rỗng. Giống như dưới đây:copy[]

#Các phương thức cập nhật

#Phương thức append
#<List>.append(x)
#Thêm phần tử x vào cuối List
print("Phương thức append")
append = lst.append(11)
print(lst)

#Phương thức extend
#<List>.extend(iterable)
#Thêm từng phần tử một của iterable vào cuối List.
print("Phương thức extend")
extend = lst.extend([12,13,14])
print(lst)

#Phương thức insert
#<List>.insert (i, x)
#Thêm phần x vào vị trí i ở trong List.
print("Phương thức insert")
insert = lst.insert(1,9)
print(lst)
#Nếu vị trí i lại lớn hơn hoặc bằng số phần tử ở trong List thì kết quả sẽ tương tự như phương thức append.

#Phương thức pop
#<List>.pop([i])
#Bỏ đi phần tử thứ i trong List và trả về giá trị đó.
#  Nếu vị trí i không được cung cấp, phương thức này sẽ tự bỏ đi phần tử cuối cùng của List và trả về giá trị đó.
print("Phương thức pop")
pop = lst.pop(0)
print(lst)
print(pop)

#Phương thức remove
#<List>.remove(x)
#Bỏ đi phần tử đầu tiên trong List có giá trị x. 
# Nếu trong List không có giá trị x sẽ có lỗi được thông báo
print("Phương thức remove")
remove = lst.remove(14)
print(lst)

#Các phương thức xử lí
#Phương thức reverse
#<List>.reverse()
#Đảo ngược các phần tử ở trong List.
print("Phương thức reverse")
reverse = lst.reverse()
print(lst)

#Phương thức sort
#<List>.sort(key=None, reverse=False)
#Sắp xếp các phần tử từ bé đến lớn bằng cách so sánh trực tiếp.
print("Phương thức sort")
sort = lst.sort()
print(lst)
sort = lst.sort(reverse=True) 
print(lst)




