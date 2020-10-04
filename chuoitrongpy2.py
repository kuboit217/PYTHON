#định dạng bằng toán tử %
#<chuỗi> % (giá trị thứ 1, giá trị thứ 2, .., giá trị thứ n – 1, giá trị 
s = "Tôi là %s và tôi là %s"
inS = s %("việt","chán nản")
print(inS)

#định dạng bằng chuỗi f
ten = 'Việt'
tuoi = 12
s1 = f"Khi tôi sinh ra {ten}, và tôi sẽ {tuoi}"
print(s1)

#định dạng bằng format
s2 = "{},{},{}".format(1,2,3)
print(s2)
s3 = "a: {1}, b: {2}, c: {0}".format("one", "two", "three")
print(s3)

#cắn lề trong Python 
#>>> ‘{:^10}’.format(‘aaaa’) # căn giữa ' aaaa ' 
# >>> '{:<10}'.format('aaaa') # căn lề trái 'aaaa ' 
# >>> '{:>10}'.format('aaaa') # căn lề phải ' aaaa' 
# >>> '{:*>10}'.format('aaaa') # căn lề trái, thay thế khoảng trắng bằng kí tự * '******aaaa' 
# >>> '{:*<10}'.format('aaaa') # căn lề phải, thay thế khoảng trắng bằng kí tự * 'aaaa******' 
# >>> '{:*^10}'.format('aaaa') # căn giữa, thay thế khoảng trắng bằng kí tự * '***aaaa***'
# phần định dạng 
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '') 
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh') 
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese') 
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada') 
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '') 
# phần xuất kết quả 
print(row_1) 
print(row_2) 
print(row_3) 
print(row_4) 
print(row_5)

#các phương thức biến đổi trong chuỗi
#capitalize Viết hóa chữ cài đầu tiên trong chuỗi, các kỹ tự còn lại sẽ là chữ thường
char = "Đinh Lang Việt"
capT = char.capitalize()
print(capT)

#upper Trả về một chuỗi với tất cả các kí tự được chuyển thành các kí tự viết hoa
upper = char.upper()
print(upper)

#lower Trả về một chuỗi với tất cả các kí tự được chuyển thành các kí tự viết thường
lower = char.lower()
print(lower)

#swapcase Trả về một chuỗi với các kí tự viết hoa được chuyển thành viết thường, các kí tự viết thường được chuyển thành viết hoa
swapCase = char.swapcase()
print(swapCase)

#title Trả về một chuỗi với định dạng tiêu đề, có nghĩa là các từ sẽ được viết hoa chữ cái đầu tiên, còn lại là viết thường
title = char.title()
print(title)

#Các phương thức định dạng
#center Trả về một chuỗi được căn giữa với chiều rộng width.
#center(width, [fillchar])
center = char.center(50,"*")
print(center)

#rjust Căn lề phải
#rjust(width, [fillchar])
rjust = char.rjust(50,'*')
print(rjust)

#ljust căn lề trái
#ljust(width, [fillchar])
ljust = char.ljust(50,"*")
print(ljust)

#Các phương thức xử lí
#Đây là phương thức dùng để encode một chuỗi với phương thức mã hóa mặc định là utf-8.
#encode(encoding=’utf-8’, errors=’strict’)
encode = char.encode(encoding="utf-8", errors="strict")
print(encode)

#Phương thức join
#join(<iterable>)
#Trả về một chuỗi bằng cách nối các phần tử trong iterable bằng kí tự nối.
join = char.join(("1","2","3"))
print(join)

#Phương thức replace
#replace(old, new, [count])
#Trả về một chuỗi với các chuỗi old nằm trong chuỗi ban đầu được thay thế bằng chuỗi new. 
# Nếu count khác None (có nghĩa là ta cho thêm count) thì ta sẽ thay thế old bằng new với số lượng count từ trái qua phải.
replace = char.replace("Lang Việt","Ngọc Thiên")
print(replace)

#Phương thức strip
#<chuỗi>.strip([chars])
#Trả về một chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi các kí tự chars. 
# Nếu chars bị bỏ trống thì mặc định các kí tự bị bỏ đi là dấu khoảng trắng và các escape sequence.
strip = char.strip("Đinh")
print(strip)

#Phương thức rstrip
#<chuỗi>.rstrip()
#Cách hoạt động hoàn toàn như phương thức strip, nhưng khác là chỉ bỏ đi ở phần đuôi (từ phải sang trái)
#Phương thức lstrip
#<chuỗi>.lstrip()
#Cách hoạt động tương tự phương thức rstrip, khác ở chỗ rstrip lo phần đuôi, còn lstrip lo phần đầu (từ trái sang phải)

#Phương thức split
#<chuỗi>.split(sep=None, maxsplit=-1)
#Trả về một list (kiểu dữ liệu sẽ được Kteam giới thiệu ở bài KIỂU DỮ LIỆU LIST) bằng cách chia các phần tử bằng kí tự sep.
split = char.split(" ")
print(split)

#Phương thức rsplit
#<chuỗi>.split(sep=None, maxsplit=-1)
#cũng hoàn toàn như phương thức split, có điều là việc tách từ bên phải sang trái
rsplit = char.rsplit(" ", 1)
print(rsplit)

#Phương thức partition
#<chuỗi>.partition(sep)
#Trả về một tuple với 3 phần tử. Các phần tử đó lần lượt là chuỗi trước chuỗi sep, sep và chuỗi sau sep.
partition = char.partition("L")
print(partition)

#Phương thức rpartition
#<chuỗi>.rpartition(sep)
#Cách phân chia giống như phương thức partition nhưng lại chia từ phải qua trái. 
# Và với sep không có trong chuỗi thì sẽ trả về 2 giá trị đầu tiên là chuỗi rỗng và cuối cùng là chuỗi ban đầu

rpartition = char.rpartition("a")
print(rpartition)

#Phương thức count
#<chuỗi>.count(sub, [start, [end]])
#Trả về một số nguyên, chính là số lần xuất hiện của sub trong chuỗi. Còn start và end là số kĩ thuật slicing (lưu ý không hề có bước).
count = char.count('i',1,10)
print(count)


#Phương thức startswith
#<chuỗi>.startswith(prefix[, start[, end]])
#Trả về giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix. Ngược lại là False.
startswith = char.startswith('Đ',1)
print(startswith)

#Phương thức endswith
#<chuỗi>.endswith(prefix[, start[, end]])
#Trả về giá trị True nếu chuỗi đó kết thúc bằng chuỗi prefix. Ngược lại là Flase.
endSwith = char.endswith("t")
print(endSwith)

#Phương thức find
#<chuỗi>.find(sub[, start[, end]])
#Trả về một số nguyên, là vị trí đầu tiên của sub khi dò từ trái sang phải trong chuỗi. 
# Nếu sub không có trong chuỗi, kết quả sẽ là -1. 
# Vẫn như các phương thức khác, start end đại diện cho slicing và ta sẽ tìm trong chuỗi slicing này.
find = char.find("V")
print(find)

#Phương thức rfind
#<chuỗi>.rfind(sub[, start[, end]])
#Tương tự phương thức find nhưng tìm từ phải sang trái
rFind = char.rfind("L")
print(rFind)

#Phương thức index
#<chuỗi>.index(sub[, start[, end]])
#Tương tự phương thức find. Nhưng khác biệt là sẽ có lỗi ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu
index = char.index("V")
print(index)

#Phương thức rindex
#<chuỗi>.rindex(sub[, start[, end]])
#Tương tự phương thức rindex. Và cũng khác ở điểm l
rIndex = char.rindex("V",4)
print(rIndex)

#Các phương thức xác thực
#Phương thức islower
#<chuỗi>.islower()
#Trả về True nếu tất cả các kí tự trong chuỗi đều là viết thường. Ngược lại là False
isLower = char.islower()
print(isLower)

#Phương thức isupper
#<chuỗi>.isupper()
#Trả về True nếu tất cả các kí tự trong chuỗi đều là viết hoa. Ngược lại là False
isUpper = char.isupper()
print(isUpper)

#Phương thức istitle
#<chuỗi>.istitle()
#Trả về True nếu chuỗi đó là một dạng title. Ngược lại là False
isTitle = char.istitle()
print(isTitle)

#Phương thức isdigit
#<chuỗi>.isdigit()
#Trả về True nếu tất cả các kí tự trong chuỗi đều là những con số từ 0 đến 9
isDigit = char.isdigit()
print(isDigit)

#Phương thức isspace
#<chuỗi>.isspace()
#Trả về True nếu tất cả các kí tự trong chuỗi đều là kí tự khoảng trắng
isSpace = char.isspace()
print(isSpace)

