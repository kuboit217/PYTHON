#while và cách hoạt động
print("while và cách hoạt động")
#while expression: 
#   # while-block
#Lưu ý: Việc chia block như thế này cũng giống như khi bạn sử dụng câu lệnh if
i = 5
while i > 0:
    print("i = ", i)
    i -=1
#Sử dụng vòng lặp để xử lí chuỗi, list, tuple
print("Sử dụng vòng lặp để xử lí chuỗi, list, tuple")
lst = "viet dinh"
i =  0
lens = len(lst)
while i < lens:
    print("vị trí ",i, ' = ', lst[i])
    i+=1

#Câu lệnh break và continue
print("Câu lệnh break và continue")
#Lưu ý: Hai câu lệnh này chỉ có thể dùng trong các vòng lặp
#Câu lệnh break
print("Câu lệnh break")
'''Câu lệnh break dùng để kết thúc vòng lặp. 
Cứ nó nằm trong block của vòng lặp nào thì vòng lặp đó sẽ kết thúc khi chạy câu lệnh này.
Trong trường hợp vòng lặp a chứa vòng lặp b. Trong vòng lặp b chạy câu lệnh break
 thì chỉ vòng lặp b kết thúc, còn vòng lặp a thì không.'''
lst = []
num = 1

while True: #5 > len(lst):
    if num % 2 ==0:
        lst.append(num)    
    if len(lst) == 5:
        break
    num += 1
print(lst)

#Câu lệnh continue
print("Câu lệnh continue")
#while expression: 
#   #while-block-1 
#   continue
#   #while-block-2 
'''Khi thực hiện xong while-block-1, câu lệnh continue sẽ tiếp tục vòng lặp, 
không quan tâm những câu lệnh ở dưới continue và như vậy nó đã bỏ qua while-block-2.'''

a = 1
while a < 10:
    if a % 2 == 0:
        a += 1
        continue
    print(a)
    a += 1

#Cấu trúc vòng lặp while-else và cách hoạt động
print("Cấu trúc vòng lặp while-else và cách hoạt động")
#while expression: 
#   # while-block 
#else:
#   else-block
