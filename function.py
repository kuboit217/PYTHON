#Khai báo hàm (create function)
print("Khai báo hàm (create function)")
#Để khai báo một hàm, ta sử dụng từ khóa “def” với cú pháp như sau
#def <function_name>(parameter_1, parameter_2, .., parameter_n): 
#    function-block
def vietdinh():
    pass
print(vietdinh)
vietdinh()
'''Lệnh pass ở trên là một lệnh “giữ chỗ” (placeholder statement) để giúp cho các block của Python không bị thiếu câu lệnh 
trong trường hợp bạn chưa biết viết gì cho phù hợp.
Bạn có thể thấy, khi in ra hàm kteam, bạn sẽ nhận được một dòng khá tương một một generator expression.'''

#Gọi hàm (call function)
print('Gọi hàm (call function)')
#<function>()
def viet():
    print("Việt Đinh")
viet()

#Đừng viết lại code (DRY - Don’t Repeat Yourself)
print("Đừng viết lại code (DRY - Don’t Repeat Yourself)")
#Giả sử, bạn có một script với nhiệm vụ in ra 8 dòng in ra “Hello Kteam!” và “Free Education”
print('Hello Kteam!') 
print("Free Education") 
print('Hello Kteam!') 
print("Free Education") 
print('Hello Kteam!') 
print("Free Education") 
print('Hello Kteam!') 
print("Free Education")
'''Việc sử dụng vòng lặp để làm chuyện này là khả thi, nhưng có nhiều trường hợp các câu lệnh không nằm liền kề nhau như thế này,
 bạn không thể dùng vòng lặp rút gọn.
Bây giờ, bạn muốn thay đổi dòng “Hello Kteam!” thành “Hi Kteam!”, vậy là bạn phải chỉnh sửa lại 4 dòng lệnh.
Giờ ta đưa vấn đề xa hơn một tí nữa. Nếu nhiệm vụ của bạn không chỉ là print ra tám dòng chữ mà còn phải làm nhiều thứ khác,
 thì có phải bạn đang viết lại rất nhiều code không? Và khi chỉnh sửa mà nếu chỉnh sửa nhiều thì bạn sẽ phải mất rất nhiều công sức.
Để có thể tránh được việc đó, ta hãy sử dụng hàm'''
def hello():
    print('Hello Kteam!') 
    print("Free Education") 
hello()
hello()
hello()

#Parameter và Argument
print("Parameter và Argument")
#def kteam(text): 
#    print(text)
#Và khi gọi hàm có parameter, bạn phải truyền vào argument tương ứng
#kteam('Hello Kteam!') 
#Ở đây, argument chúng ta đưa vào là một chuỗi. Chuỗi này sẽ được đưa vào gán cho parameter tương ứng là text. Và rồi hàm thực hiện việc in text ra.
#Đương nhiên là chúng ta có thể biến hóa nhiều ra nữa
#def kteam(greating, name):
#    print(greating, name + '!')

#Giá trị mặc định của parameter (Default argument)
print("Giá trị mặc định của parameter (Default argument)")
def helooPy(name,greating = "Hi"):
    print(greating, name + "!")
helooPy("Việt")
"""Khi bạn đưa default argument cho các parameter, phải để các parameter có default argument ở sau cùng.
Default argument là một unhashable container"""
'''unhashable container phổ biến mà ta đã từng biết như LIST, DICT, SET. 
Ở đây có một cảnh báo cho bạn việc bạn sử dụng default argument cho parameter là một 
unhashable container đó là giá trị của nó không được làm mới (refresh) sau mỗi lần gọi 
hàm mà không pass argument mới cho parameter đó. Đương nhiên là nếu bạn có pass cho nó một argument mới 
thì container đó vẫn không hề mất giá trị nếu lần sau bạn gọi nó.'''
def add(lst=[]):
    lst.append('V')
    print(lst)
add()
add()
add()
add([1,2,3])

#POSITIONAL VÀ KEYWORD ARGUMENT
print("POSITIONAL VÀ KEYWORD ARGUMENT")
'''Với một hàm thông thường như sau
def kteam(a, b):
    pass
Thì ta có thể pass argument vào cho hàm như sau
kteam(3, 'Free Education')
Trong ví dụ trên, hai giá trị là số 3 và chuỗi ‘Free Education’ gọi là positional argument.
Còn với trường hợp dưới đây
kteam(a=3, b='Free Education')
Thì hai giá trị trên (chính là số 3 và chuỗi ‘Free Education’) là những keyword argument.
Một điều nữa là bạn không được phép để positional theo sau (follow) keyword.
Có nghĩa là bạn có thể pass argument vừa positional và keyword cùng một lúc được, nhưng những positional buộc phải đứng trước keyword'''
#Bắt buộc (force) Positional argument và keyword argument
print("Bắt buộc (force) Positional argument và keyword argument")
#Trong Python, có một số hàm bắt chúng ta buộc phải pass argument một cách rõ ràng rành mạch như hàm sorted.
print(sorted([3, 4, 1], reverse=True))
'''def function (*, key_arg1, key_arg2):
 # function-block
 Khi tạo một hàm mà có một parameter *. Thì Python sẽ hiểu đó không phải là parameter
  mà chính là syntax để rồi nó biến các parameter sau * thành các keyword only argument (chỉ nhận giá trị theo kiểu keyword argument)'''
#ta có thể thay thế dấu * bằng *identifier. Tuy nhiên phổ biến vẫn là *.
def tich(a,*,b,c):
    print(a*b*c)
tich(3,b=4,c=6)

