'''Iteration là một khái niệm chung cho việc lấy từng phần tử một của một đối
tượng nào đó, bất cứ khi nào bạn sử dụng vòng lặp hay kĩ thuật nào đó để có
được giá trị một nhóm phần tử thì đó chính là Iteration.
Ví dụ: như bạn ăn một snack, bạn sẽ lấy từng miếng trong bọc snack ra ăn
cho tới khi hết thì thôi. Bạn có thể coi việc lấy bánh là một vòng lặp. Đương
nhiên bạn cũng có thể chọn không lấy hết số bánh ra.'''

'''Iterable object là một object có phương thức __iter__ trả về một iterator, hoặc
là một object có phương thức __getitem__ cho phép bạn lấy bất cứ phần tử
nào của nó bằng indexing ví dụ như Chuỗi, List, Tuple.

Iterator object đơn giản chỉ là một đối tượng mà cho phép ta lấy từng giá trị
một của nó. Có nghĩa là bạn không thể lấy bất kì giá trị nào như ta hay làm với
List hay Chuỗi.
Iterator không có khả năng tái sử dụng trừ một số iterator có phương thức hỗ
trợ như file object sẽ có phương thức seek.
Iterator sử dụng hàm next để lấy từng giá trị một. Và sẽ có lỗi StopIteration
khi bạn sử dụng hàm next lên đối tượng đó trong khi nó hết giá trị đưa ra cho
bạn.
Các iterable object chưa phải là iterator. Khi sử dụng hàm iter sẽ trả về một
iterator. Đây cũng chính là cách các vòng lặp hoạt động.'''

data = [x for x in range(3)] # thuộc lòng 3 giá trị của comprehension này
print(data)
print(data[0])

itor = (i for i in range(5)) # sử dụng () cho ra một generator expression – một iterator
print(itor)
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor))
print(type(itor))
#print(next(itor)) lỗi vì hết interator

lst = [5,6,"Viet",[0,2,4]]
itor = iter(lst)
print(itor)
print(type(itor))
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor)[-1])
#Bạn cũng lưu ý, iterator này cũng dính một vấn đề như List, Dict đó chính là chỉnh một, thay đổi hai.

#Một số hàm hỗ trợ cho iterable object trong Python

#Hàm tính tổng – sum
print("Hàm tính tổng – sum")
#sum(iterable, start=0)
#Trả về tổng các giá trị của iterable và iterable này chỉ chứa các giá trị là số. Còn start chính là giá trị ban đầu. Có nghĩa là sẽ cộng từ start lên.
# Mặc định là 0
itor = (i for i in range(4))
print(type(itor))
print(sum(itor))
print(sum(itor),3)

#Hàm tìm giá trị lớn nhất – max
print("Hàm tìm giá trị lớn nhất – max")
#max(iterable, *[, default=obj, key=func])
#Nhận vào một iterable.Tìm giá trị lớn nhất bằng key (mặc định là sử dụng operator >). Default là giá trị muốn nhận về trong trường hợp không lấy được bất kì giá trị nào trong iterable.
# Dấu * chính là kí hiệu yêu cầu keyword-only argument. Bạn sẽ hiểu thêm khi Kteam giới thiệu parameter trong function.
# hoặc max(arg1, arg2, *args, *[, key=func])
tup = (3,5,10)
itor = iter(tup)
print(max(itor))

#Hàm tìm giá trị nhỏ nhất – min
print("Hàm tìm giá trị nhỏ nhất – min")
#min(iterable, *[, default=obj, key=func])
#min(arg1, arg2, *args, *[, key=func])
#giống như hàm max. Khác ở chỗ đây là tìm giá trị nhỏ nhất
tup = (5,36,49)
itor = iter(tup)
print(min(itor))

#Hàm sắp xếp – sorted
print("Hàm sắp xếp – sorted")
#sorted(iterable, /, *, key=None, reverse=False)
#Giống với phương thức sort của List object.
lst = [5,3,65,2]
itor = iter(lst)
print(lst)
print(sorted(itor, reverse=True))