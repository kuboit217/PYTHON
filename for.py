#Hạn chế của vòng lặp while
print("Hạn chế của vòng lặp while")
'''Bạn có thể sử dụng vòng lặp while để có thể duyệt một List, chuỗi hoặc là một Tuple. Và thậm chí là một iterator (một object không hỗ trợ indexing) 
khi biết được số phần tử mà iterator đó chứa.'''
'''Nếu bạn không biết trước được số phần tử mà iterator đó có thì cũng không sao. Python vẫn cho phép bạn làm được điều đó bằng try-block'''
length = 3
iter_ = (i for i in range(length))
c = 0
while c < length:
    print((next(iter_)))
    c+= 1

#ví dụ về try
print("Ví dụ về try")
iter_ = (i for i in range(5))
while True:
    try:
        print((next(iter_)))
    except StopIteration:
        break

#Cấu trúc vòng lặp for và cách hoạt động
print("Cấu trúc vòng lặp for và cách hoạt động")
#for variable_1, variable_2, .. variable_n in sequence: 
#   # for-block
'''Sequence ở đây là một iterable object (có thể là iterator hoặc là một dạng object cho phép sử dụng indexing hoặc thậm chí không phải hai kiểu trên).
Lưu ý: Nếu sequence là một iterator object thì việc dùng vòng lặp duyệt qua cũng sẽ tương tự như bạn sử dụng hàm next.
Ở cấu trúc vòng lặp này, bạn có thể for bao nhiêu biến theo sau cũng được. Nhưng phải đảm bảm một điều rằng, nếu bạn for với n biến thì
 mỗi phần tử trong sequence cũng phải bao gồm n (không lớn hơn hoặc nhỏ hơn) giá trị để unpacking (gỡ) đưa cho n biến của bạn.'''
print("unpacking")
h = (1, 2, 3) # khởi tạo Tuple bình thường
print(type(h))
h,k,t = (1,2,3)
print(h , k ,t)

#Sử dụng vòng lặp để xử lí các iterator và Dict
print("Sử dụng vòng lặp để xử lí các iterator và Dict")

iter_ = (value for value in range(4))
for i in iter_:
    print("=>" , i)

'''Tiếp đến chúng ta sẽ dùng vòng lặp này để duyệt một Dict. Nếu như một số ngôn ngữ khác phải có một vòng lặp mới for-reach thì với Python lại không cần.'''
dic_ = {'name':"việt", "tuoi":29}
print(dic_.items())
'''Dict-items không phải là một iterator object. Cũng không phải là một object cho phép bạn indexing. Nhưng nó vẫn là một iterable, nên ta có thể dùng
một constructor nào đó để biến đổi nó về một thứ dễ xem xét hơn. Chẳng hạn thế này.'''
lst_ = list(dic_.items())
print(lst_)
#Từ đó, ta có thể dễ dàng suy ra cách để có thể có được một vòng lặp duyệt một Dict. Và đây là ví dụ:
for key, value in dic_.items():
    print(key ,"=>", value)

#Câu lệnh break, continue
print("Câu lệnh break, continue")
'''Những câu lệnh này có chức năng hoàn toàn tương tự như trong vòng lặp while.
Ví dụ về câu lệnh break trong vòng lặp for'''
ch = "Việt Đinh"
for i in ch:
    if i ==" ":
        break
    else:
        print(i)
#chỉ in được việt do có khoảng trống sẽ thoát ra vòng lặp
ch = "Việt Đinh"
for i in ch:
    if i ==" ":
        continue
    else:
        print(i)
#sẽ in ra hết nhưng sẽ bỏ khoảng trống đi vì có continue

#Cấu trúc vòng lặp for-else và cách hoạt động
print("Cấu trúc vòng lặp for-else và cách hoạt động")
#for variable_1, variable_2, .. variable_n in sequence: 
#   # for-block 
# else: 
#   # else-block
'''Cũng sẽ tương tự như while-else, vòng lặp hoạt động bình thường. Khi vòng lặp kết thúc, khối else-block sẽ được thực hiện. 
Và đương nhiên nếu trong quá trình thực hiện for-block mà xuất hiện câu lệnh break thì vòng lặp sẽ kết thúc mà bỏ qua else-block'''
#For-else bình thường:
print("For-else bình thường:")
for i in (1,2,3):
    print(i)
else:
    print("Xong")

#For-else có break:
print("For-else có break:")
for i in (1,3,4):
    if i % 2 == 0:
        break
    else: print(i)
