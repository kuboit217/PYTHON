#Mở File trong Python
print("Mở File trong Python")

#Hàm open
print("Hàm open")
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#Ở mức độ cơ bản, chúng ta sẽ chỉ quan tâm đến 2 parameter: file và mode.
#Nếu các bạn muốn tìm hiểu rõ hơn về các parameter khác. Hãy dùng lệnh:
#help(open)
file_obj = open("file.txt")
print(file_obj)
#r mở để dọc đây là mode mặc đinh
#r+ mở để đọc và ghi
#w mở để ghi. trước đó nó sẽ xóa hết nội dung hiện có. Nếu file không tôn tài, sẽ tạo ra một file với tên là tên file truyền vào.
#w+ mở để ghi và đọc. trước đó cũng sẽ xóa hết nội dung hiện có. nếu file không tồn tại, sẽ tạo ra một file với tên là file truyền vào.
#a mở để ghi. nếu file không tồn tại, sẽ tạo ra mootj file với tên là file truyền vào.
#a+ mở để ghi và đọc. nếu file không tồn tài sẽ tạo ra một file với tên là file truyền vào.

#Đóng File trong Python
print("Đóng File trong Python")
#<File>.close()

#Đọc File trong Python
print("Đọc File trong Python")
#<File>.read(size=-1)
'''Nếu size bị bỏ trống hoặc là một số âm. Nó sẽ đọc hết nội dung của file đồng thời đưa con trỏ file tới cuối file. 
Nếu không nó sẽ đọc tới n kí tự (với n = size) hoặc cho tới khi nội dung của file đã đọc xong.
 Sau khi đọc được nội dung, nó sẽ trả về dưới một dạng chuỗi.
Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng 0'''
print(file_obj.read(30))
file_obj.close()

#Phương thức readline
print("Phương thức readline")
#<File>.readline(size=-1)
'''Với parameter size thì hoàn toàn tương tự như phương thức read.
 Khác biệt ở chỗ, phương thức readline chỉ đọc một dòng có nghĩa là đọc tới khi nào gặp newline hoặc hết file thì ngừng.
 Con trỏ file cũng sẽ đi từ dòng này qua dòng khác.
 Kết quả đọc được trả về dưới dạng một chuỗi.
 Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng'''
file_obj = open("file.txt")
print(file_obj.readline(10))
print(file_obj.readline(10))
print(file_obj.readline(10))
file_obj.close()


#Phương thức readlines
print("Phương thức readlines")
#<File>.readlines(hint=-1)
'''Phương thức này sẽ đọc toàn bộ file, sau đó cho chúng vào một list. Với các phần tử trong list là mỗi dòng của file.
 Con trỏ file sẽ được đưa tới cuối file. Khi đó, nếu bạn tiếp tục dùng readlines. Bạn sẽ nhận được một list rỗng.'''
file_obj = open("file.txt")
print(file_obj.readlines())
print(file_obj.readlines(11))
file_obj.close()

#Đọc file bằng constructor nhận iterable
print("Đọc file bằng constructor nhận iterable")
'''Như đã nói, file object nhận được từ hàm open cũng là một iterable.
Thế nên, ta có thể sử dụng constructor list'''
file_obj = open("file.txt")
list_contents = list(file_obj.readlines())
print(list_contents)
file_obj.close()
file_obj = open("file.txt")
tup_contents = tuple(file_obj.readlines())
print(tup_contents)
file_obj.close()

#Ghi File trong Python
print("Ghi File trong Python")
#Phương thức write
print("Phương thức write")
#<File>.write(text)
#Phương thức này sẽ trả về số kí tự mà chúng ta ghi vào.
file_obj = open("file.txt", "w")
print(file_obj.write("Hello \n"))
file_obj.close()
file_obj = open("file.txt", "w") #nội dung file ban đầu của bạn sẽ bị mất đi. Đó là lí do chúng ta cần mới mode a.
print(file_obj.write("Viet Dinh \n"))
file_obj.close()

#sử dụng mode a
file_obj = open("file.txt" , "a")
print(file_obj.write("Dinh lang viet \n"))
file_obj.close()
file_obj = open("file.txt" , "a")
print(file_obj.write("co len nao \n"))
file_obj.close()

#Kiểm soát con trỏ file
print("Kiểm soát con trỏ file")

#Phương thức seek
print("Phương thức seek")
#<File>.seek(offset, whence=0)
'''Phương thức này giúp ta di chuyển con trỏ từ vị trí đầu file qua offset kí tự. Và parameter offset phải là một số tự nhiên.
 Nhờ phương thức này, ta có thể ghi nội dung từ bất cứ đâu trong file.
 Và từ đó ta có thể đọc lại file sau khi ta đưa con trỏ file xuống cuối file.'''
file_obj = open("file.txt")
print(file_obj.read())
file_obj.seek(5)
print(file_obj.read())
file_obj.close()

#Câu lệnh with
print("Câu lệnh with")
#with expression [as variable]: with-block
'''Nhớ rằng with-block nằm thụt vào so với dòng with expression (theo chuẩn PEP8 là 4 space và là dùng space không dùng tab)
Câu lệnh này liên quan đến phương thức __enter__ và __exit__ của đối tượng. Do đó, ở đây Kteam sẽ nói cơ bản khi sử dụng file.
Đặc điểm của câu lệnh with khi sử dụng với file là. Khi kết thúc with-block. File sẽ được đóng.'''
with open("file.txt") as file_obj:
    data = file_obj.readlines()
print(data)
    

