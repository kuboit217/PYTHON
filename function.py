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

#Unpacking arguments với *
print("Unpacking arguments với *")

def kteam(k, t, e, r): 
    print(k) 
    print(t, e) 
    print('end', r)
'''Bạn thấy đấy! Hàm này gồm 4 parameter và không có default argument. Vậy nên khi gọi hàm này, bạn buộc phải đưa vào 4 argument.
Nhưng bạn có một vấn đề, 4 argument cần truyền vào khi gọi hàm này lại nằm trong một List
lst = ['123', 'Kteam', 69.96, 'Henry']
Chả sao cả, bạn có thể lấy từng phần tử (element) trong list ra một cách dễ dàng, sau đó bạn có thể gọi hàm kteam như thế này'''
#lst = ['123', 'Kteam', 69.96, 'Henry']
#kteam(lst[0], lst[1], lst[2], lst[3])
'''Phức tạp vấn đề lên một chút nào! Sẽ ra sao nếu bạn có 50 parameter và phải gõ hết 50 indexing để truyền vào cho hàm khi gọi nó?
Lập trình viên lười lắm, họ không làm chuyện đó đâu. Vậy nên, Python cho phép làm điều đó đơn giản chỉ bằng một dấu *'''
lst = ['123', 'Kteam', 69.96, 'Henry']
kteam(*lst)
'''Khi bạn sử dụng *, bạn không chỉ có thể unpack được các List mà bên cạnh đó bạn có thể unpack các container 
khác như Tuple, Chuỗi, Generator, Set, Dict (chỉ lấy được key).
Pass argument bằng cách unpacking argument như thế này là đang truyền vào dưới dạng positional argument. 
Hãy cẩn thận sử dụng kĩ thuật này với những hàm có parameter dạng keyword-only argument.
>>> def a(*, s, d): ... print(s, d) ... >>> a(*('a', 'b')) Traceback (most recent call last): File "<stdin>", 
line 1, in <module> TypeError: a() takes 0 positional arguments but 2 were given
Trong trường hợp container của bạn unpack các giá trị có trong container nhưng vẫn chưa đủ yêu cầu của hàm, thì bạn có thể truyền thêm:'''
kteam(* ('a', 'b', 'c'), 'd')

#Packing arguments với *
print('Packing arguments với *')
'''Khi bạn sử dụng packing argument. Đồng nghĩa với việc bạn nhờ một biến đi gói tất cả 
các giá trị truyền vào cho hàm bằng positional argument thành một Tuple. Nếu không có 
gì để gói (bạn không truyền vào bất cứ argument nào) thì bạn sẽ nhận được một tuple rỗng. 
Để giao nhiệm vụ cho một biến làm công việc này, bạn đặt một dấu * trước nó.'''
def kteam(*args):
    print(args)
    print(type(args)) 

kteam('Kteam', 69.96, 'Henry')
'''Bạn không nên nhầm lẫn việc này với việc force keyword-only argument Không 
được phép để 2 parameter cùng làm nhiệm vụ packing argument trong một hàm
Nếu sau một packing parameter còn có những parameter khác, 
khi gọi hàm muốn truyền giá trị vào cho các parameter sau packing parameter bạn cần phải sử dụng keyword argument.
def f(*args, kter): 
    print(kter) 
    f('1', '2') 
Traceback (most recent call last): File "<stdin>", 
line 1, in <module> TypeError: f() missing 1 required keyword-only argument: 'kter' >>> 
f('1', '2', kter='3')'''

#Unpacking arguments với **
print("Unpacking arguments với **")
dic = {'name': 'Kteam', 'member': 69}
def kteam(a,b):
    print(a)
    print(b)
kteam(*dic)
'''Với Dict, thì nó phức tạp hơn một xíu khi mỗi phần tử là một cặp key và value. 
Vậy nên một dấu * là không đủ nội công để unpack hết được các giá trị. Do đó ta phải nhờ đến một cặp **.
Nếu bạn unpacking một Dictionary để truyền argument vào cho hàm khi gọi hàm thì đây chính là dạng keyword argument. 
Vậy nên bạn phải chắc chắn rằng parameter với key là giống nhau.'''
dic = {'name': 'Kteam', 'member': 69}
def kteam(name,member):
    print(name,'=>',name)
    print(member,'=>',member)
kteam(**dic)

#Packing arguments với **
print('Packing arguments với **')
'''Đã có unpacking với ** thì cũng phải có packing. Khác với dấu * là gói những positional argument thì ** lại gói các keyword argument. 
Và đương nhiên, nó sẽ gói trong một Dict. Nếu không truyền gì vào sẽ là một dict rỗng.'''
def kteam(**kwargs):
    print(kwargs)
    print(type(kwargs))
kteam(name="viet", tuoi = 29)

def infor(**kwargs):
    for key,value in kwargs.items():
        print(key , "=>", value)
infor(name = 'Việt', Tuoi = 29)
'''bạn không được phép bỏ các positional parameter sau biến packing mà có ** giống như với *.'''

#Bài 31: KIỂU DỮ LIỆU FUNCTION TRONG PYTHON - BIẾN LOCALS VÀ GLOBALS
print("Bài 31: KIỂU DỮ LIỆU FUNCTION TRONG PYTHON - BIẾN LOCALS VÀ GLOBALS")

#Khai báo biến ở trong hàm
def make_sologan():
    viet = "Việt Đinh"
    print(viet)
make_sologan()
'''biến khai báo ở hàm nào thì chỉ hàm đó mới biết biến đó còn thoát ra ngoài hàm đó thì coi như không có. 
Biến khai báo ở hàm cha có thể sử dụng trong hàm con nhưng biến ở hàm con không thể sử dụng ở hàm cha.
Lưu ý: Biến là đối tượng nên bị ràng buộc bởi điều này. Do đó các HÀM (FUNCTION), LỚP (CLASS) 
cũng chịu sự ràng buộc này tương tự. Khai báo ở hàm nào thì chỉ dùng ở hàm đó.'''
#Thay đổi giá trị argument gián tiếp qua parameter
print("Thay đổi giá trị argument gián tiếp qua parameter")
'''pass by reference. Có nghĩa là bạn đưa bản gốc.
pass by value, đưa giá trị hoặc là “đưa bản sao”.'''
num = 69 
st = 'How Kteam' 
lst = [1, 2, 3] 
tup = tuple('Education') 
def change(parameter): 
    parameter = 'New value' 
    print('Changed successfully!') 
change(num) 
change(st) 
change(lst) 
change(tup) 
print('*' * 10) 
print('{}\n{}\n{}\n{}\n'.format(num, st, lst, tup))

#Sử dụng lệnh global
print("Sử dụng lệnh global")
'''
Nếu như một biến nằm trong một hàm (như biến kteam trong ví dụ cuối ở phần đầu) thì người ta hay gọi đó là local variable (biến chỉ có hiệu lực trong một hàm nhỏ).
Đặt vấn đề là việc khai báo biến ở trong hàm trở nên cần thiết thì sao nhỉ?
Ta được Python hỗ trợ lệnh global.
global <variable>
def make_slogan(): 
    # khởi tạo với global không có giá trị nhé 
    # global kteam # sau khi khởi tạo xong, ta mới gán giá trị 
    # kteam = 'How Kteam' 
    # # nhớ là phải chạy hàm nữa 
make_slogan() 
print(kteam)'''
'''BẠN KHÔNG NÊN SỬ DỤNG GLOBAL trừ khi hết cách. Nó giống như hàm eval vậy. 
Việc sử dụng biến global làm cho chương trình rối, khó kiểm soát cho nên hạn hãy chế tối đa việc sử dụng.'''

#Giới thiệu hàm locals và globals
print("Giới thiệu hàm locals và globals")
'''
Cái tên hàm nói lên tất cả. Hàm locals cho ta biết được những biến local (những biến được khai báo trong hàm)
nằm trong chương trình của chúng ta. Còn globals là hàm giúp chúng ta biết được những biến global trong chương trình.
Kết quả trả ra của hai hàm này là một Dict. Với key là tên biến và value là giá trị của biến.
Với hàm globals() thì với biến globals có giá trị mới được trả về.'''
print(locals())
print(globals())

#Giới thiệu lệnh return
print("Giới thiệu lệnh return")
''''
Đây là lệnh chỉ sử dụng được ở trong hàm (nếu sử dụng ở ngoài hàm sẽ có nhắc lỗi) 
SyntaxError: 'return' outside function
Lệnh return có cú pháp như sau 
return [object]
Ở đây, object là một đối tượng bất kì của một lớp nào đó, có thể là số (number),
chuỗi (string), list, tuple, hàm (sẽ biết rõ hơn khi tìm hiểu decorator), lớp (class) 
hoặc thậm chí là bỏ trống – trường hợp bỏ trống thì object return về được tính là None.
Khi return được gọi, hàm được kết thúc và kết quả được trả ra ngoài. Kết quả trả ra ngoài 
nên được đưa cho một biến nào đó hứng, nếu không thì coi như bạn gọi hàm không để làm gì.
'''
def cal_rec_per(width,height):
    per = (width + height) * 2
    return per # treturn per
width_rec = 10
height_rec = 20
rec_per = cal_rec_per(width_rec,height_rec) # tạo biến hứng return trong hàm.
print(rec_per)
