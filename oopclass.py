''' Nói đơn giản nó giống như là một bản mẫu, một khuôn mẫu. Ở đó ta khai báo các thuộc tính (attribute) 
và phương thức (method) nhằm miêu tả để từ đó ta tạo ra được những object (đối tượng)
Lưu ý:  đôi khi object người ta cũng có thể ghi là instance, tuy nó không sát nghĩa cho lắm. Bạn không cần bận tâm lắm đâu vì vào ví dụ 
ta sẽ hiểu thêm, còn nếu bạn muốn hiểu kĩ thì hãy nghiền ngẫm câu tiếng Anh sau:
'' “Objects are instances of types. 42 is an instance of the type int is equivalent to 42 is an int object”'''
'''

    class <tên_lớp>:

        # code
'''
class SieuNhan:
    pass

sieu_nhan_A = SieuNhan() # sieu_nhan_A chính là một object thuộc lớp SieuNhan
print(sieu_nhan_A)
'''__main__.SieuNhan nghĩa là đây là đối tượng thuộc lớp SieuNhan ở hàm main (có nghĩa là ở file ta đang chạy thực thi) 
kèm theo cái nơi cư trú của nó – thứ mà ta không cần bận tâm lắm lúc này.'''

#Thuộc tính là gì?
print("Thuộc tính là gì?")
'''Siêu nhân (SN) của  ta chưa có thuộc tính gì, ta cần phải giúp SN có thêm một vài thuộc tính. Khi khai báo thuộc tính cho một đối tượng, 
bạn phải nghĩa ra những thuộc tính để mà giúp ta có thể phân biệt nó với những đối tượng khác cùng lớp, ví dụ như giữa 2 thằng con trai đừng lấy
 giới tính ra để phân biệt mà nên dùng hơn là sử dụng tên.

Vậy nghĩ tới siêu nhân, ta nghĩ tới cái gì? Tên, vũ khí, màu sắc,…

Bạn đọc xem đoạn code ví dụ dưới đây để biết khai báo thuộc tính ĐƠN GIẢN và cách lấy thuộc tính'''

class SieuNhan:
    pass

sieu_nhan_A = SieuNhan()

sieu_nhan_A.ten = "Sieu nhan do"
sieu_nhan_A.vu_khi = "Kiem"
sieu_nhan_A.mau_sac = "Do"

print("Ten cua sieu nhan la:",sieu_nhan_A.ten)
print("Sieu nhan mau:", sieu_nhan_A.mau_sac)
print("Su dung vu khi:", sieu_nhan_A.vu_khi)

'''Lưu ý là thuộc tính nào có mới lấy ra được nhé, chứ cái class của chúng ta không tự động sinh ra thuộc tính đâu'''

#Hàm constructor (initialize method)
print("Hàm constructor (initialize method)")
'''
class SieuNhan:
    def __init__(self):
        pass
1
2
3
4

    Lưu ý: 2 dấu gạch “_” bắt đầu và kết thúc
'''
'''Giải thích một vài điều, đây là tên hàm được quy ước, nếu bạn đặt tên hàm như vậy, bạn mặc định nói với chương trình rằng đây 
là constructor (nó là gì thì bạn từ từ sẽ biết). Trong Python, một số hàm trong lớp sẽ được tự động gọi khi ta khai báo một đối tượng và constructor 
là một trong số những hàm đó.

Từ khóa self hay cụ thể ở đây là parameter self là một quy ước (lưu ý là hoàn toàn sẽ không bị bắt lỗi cú pháp nếu dùng từ khóa khác), 
bạn có thể dùng một từ khóa khác. Tuy nhiên từ trước tới giờ mình chưa thấy ai dùng một tứ khóa khác ngoài self. Nếu bạn không muốn gây
 hiểu lầm cho người khác thậm chí khiến người khác nghĩ là bạn viết code sai thì bạn nên sử dụng từ khóa self.

Vậy, từ khóa self là gì? Không ngẫu nhiên mà người ta lại lấy từ self. Ý nghĩa của nó là chính đối tượng đó. 
Hơi khó hiểu nhỉ? Coi ví dụ đã, bạn sẽ dần tự hiểu ra từ khóa này.'''
class sieunhan():
    """
    docstring
    """
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)

print("ten la:",sieu_nhan_A.ten)
#Phương thức là gì?
print("Phương thức là gì?")
class sieunhan():
    """
    docstring
    """
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
    def xinchao(self):
        return "Ta là: " + self.ten

sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)

print("ten la:",sieu_nhan_A.ten)
print(sieunhan.xinchao(sieu_nhan_A))
print(sieu_nhan_A.xinchao())

#Khai báo và sử dụng
print("Khai báo và sử dụng")
class sieunhan():
    """
    class siêu nhân
    """    
    suc_manh = 50
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
    def xinchao(self):
        return "Ta là: " + self.ten

sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)
print(sieu_nhan_A.suc_manh)
''' ta đã khai báo một thuộc tính suc_manh ở ngay hẳn trong lớp SieuNhan, 
và dĩ nhiên thuộc tính này không cần phải khai báo gián tiếp qua hàm constructor.

Lớp SieuNhan dĩ nhiên là có thuộc tính suc_manh = 50. Và vì sieu_nhan_A là một đối tượng thuộc lớp SieuNhan, 
nên những thuộc tính ở lớp SieuNhan mặc định sẽ được tự động gán cho đối tượng này, vì thế đối tượng này cũng có thuộc tính 
và cũng như là giá trị như ta khai báo trong “khuôn mẫu”'''

#Cập nhật giá trị thuộc tính thông qua lớp
print("Cập nhật giá trị thuộc tính thông qua lớp")
class sieunhan():
    """
    class siêu nhân
    """    
    so_thu_tu = 1
    suc_manh = 50
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
        self.stt = sieunhan.so_thu_tu
        sieunhan.so_thu_tu += 1
        
    def xinchao(self):
        return "Ta là: " + self.ten

sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)

sieu_nhan_B = sieunhan("Bool","do",1)
print(sieu_nhan_B.__dict__)

print(sieu_nhan_A.suc_manh)
sieunhan.suc_manh = 40
print(sieu_nhan_A.suc_manh)

print(sieu_nhan_A.stt)
print(sieu_nhan_B.stt)

'''Thuộc tính so_thu_tu được thay đổi qua mỗi lần tạo đối tượng mới vì mỗi lần tạo đối tượng mới là ta lại gọi hàm constructor,
 do đó gián tiếp thay đổi giá trị so_thu_tu của lớp.

Ta gán giá trị này cho một thuộc tính của đối tượng đó ngay trong hàm constructor chứ  không để cho lớp giữ.
 Vì nếu đễ cho lớp giữ thì như bạn đã biết, nó sẽ thay đổi chứ không hề giữ nguyên sau các lần tạo đối tượng mới.'''

 #Cập nhật giá trị thuộc tính thông qua đối tượng
print("Cập nhật giá trị thuộc tính thông qua đối tượng")
class sieunhan():
    """
    class siêu nhân
    """    
    so_thu_tu = 1
    suc_manh = 50
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
        self.stt = sieunhan.so_thu_tu
        sieunhan.so_thu_tu += 1
        
    def xinchao(self):
        return "Ta là: " + self.ten

sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)
print(sieu_nhan_A.suc_manh)



sieu_nhan_B = sieunhan("Bool","do",1)
print(sieu_nhan_B.__dict__)

sieu_nhan_B.suc_manh = 10

print(sieu_nhan_B.suc_manh)

#Sử dụng thuộc tính trong các phương thức
print("Sử dụng thuộc tính trong các phương thức")
'''Và đương nhiên rồi, như đã nói thì khi bạn khai báo thuộc tính của một đối tượng ở ngay trong “khuôn mẫu” 
luôn thì nó cũng chỉ vẫn là thuộc tính, vì thế bạn vẫn có thể sử dụng nó ở trong các phương thức một cách bình thường 
như những thuộc tính được khởi tạo ngay trong hàm constructor'''
class sieunhan():
    """
    class siêu nhân
    """    
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
        
    def xinchao(self):
        return "Ta là: " + self.ten

sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)

print(sieu_nhan_A.xinchao())

#Các phương thức lớp trong lập trình hướng đối tượng với Python 
print("Các phương thức lớp trong lập trình hướng đối tượng với Python ")
'''Thông thường parameter được nhận nhiệm vụ nhân argument đó ta sẽ đặt là self. 
Những phương thức mà có mặc định parameter self người ta gọi đó là những regular method (phương thức thường).'''

#Class method
'''Như bạn biết thì khi làm như vậy, thuộc tính ở lớp cũng như tất cả các đối tượng thuộc lớp đó sẽ được cập nhật lại với giá trị mới.

Tuy nhiên, cách này thường không đường sử dụng, mà thay vào đó họ sẽ sử dụng class method. Sử dụng làm sao thì mời bạn đọc đến với ví dụ sau:'''

print("Class method")

class sieunhan():
    """
    class siêu nhân
    """    
    suc_manh = 50
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi

    @classmethod   
    def cap_nhat_suc_manh(cls,smanh):
        cls.suc_manh = smanh

    def xinchao(self):
        return "Ta là: " + self.ten

sieu_nhan_A = sieunhan("viet","do",29)
print(sieu_nhan_A.__dict__)

print(sieu_nhan_A.suc_manh)

sieu_nhan_A.cap_nhat_suc_manh(10)

print(sieu_nhan_A.suc_manh)

print(sieu_nhan_A.xinchao())

'''Để Python biết được phương thức nào là class method thì bạn thên @classmethod ngay trên dòng khai báo hàm. 
Và như đã nói, mặc định sẽ luôn có một argument được gửi vào đó chính là lớp gọi phương thức đó.

Và dĩ nhiên cũng có thể là lớp của đối tượng gọi phương thức đó
Tuy nhiên, đây không phải là ứng dụng chính của class method. Class method thường được dùng để tạo đối tượng.

Đặt vấn đề, ta muốn khởi tạo một siêu nhân, tuy nhiên một số siêu nhân lại có các thông tin không được tường minh 
rõ ràng mà lại được lưu dưới dạng một list, hay một chuỗi ta có thể xử lí để lấy các thông tin. Và như vậy, 
bạn thấy rằng ta cần phải có một bước tiền xử lí trước khi ra được các thông tin của một siêu nhân sau đó mới tạo được đối tượng

Giả sử ta phải xử lí các thông tin của siêu nhân là một chuỗi. Các thông tin được nối với nhau bằng một kí tư “-“.'''

class sieunhan():
    """
    class siêu nhân
    """    
    suc_manh = 50
    def __init__(self,ten,mausac,tuoi):
        self.ten = ten
        self.mausac = mausac
        self.tuoi = tuoi
    @classmethod
    def from_string(cls,s):
        str = s.split("-")
        new_str = [st.strip() for st in str]
        ten,mausac,tuoi = new_str
        return cls(ten,mausac,tuoi)
str = "Viet - Dinh - Lang"
sieu_nhan_A = sieunhan.from_string(str)
print(sieu_nhan_A.__dict__)
'''đối tượng sieu_nhan_A giờ đây không còn được khởi tạo theo cách thông thường mà giờ đây lớp SieuNhan qua một bức xử lí các thông tin, 
sau đó khởi tạo một đói tượng ngay trong phương thức, rồi mới trả về lại cho sieu_nhan_A.
'''

#Static method
print("Static method")
'''Regular method được ngầm gửi vào argument là chính đối tượng gọi phương thức và ta sử dụng parameter self để xử lí những vấn đề khác, 
class method được ngầm gửi vào argument là chính class gọi phương thức và ta sử dụng parameter cls để xử lí những vấn đề 
khác thì static method chẳng ngầm gửi cái gì vào cả, nó như một hàm bình thường.

Câu hỏi ở đây là, ta chẳng cần tạo static method mà tạo luôn hàm ở ngoài lớp được không? Chẳng vấn đề gì. 
Tuy nhiên static method vẫn tồn tại vì đôi lúc ta cần sự khoa học, logic, một số phương thức chẳng có sử dụng tí
 gì tới những thông tin của đối tượng thuộc lớp đó tuy nhiên nó vẫn có gì đó liên quan nên vẫn được đặt ở trong lớp đó.'''

class vietdinh():
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    @staticmethod
    def chao():
        print(" 1 2 3 xin chào")

viet_dinh = vietdinh("Việt", 30)
print(viet_dinh.__dict__)
print(viet_dinh.chao())

'''Nếu bạn vẫn phân vân khi nào dùng regular method, class method, static method thì bạn chỉ cần nhớ thế này:

    Nếu bạn dựng một phương thức cần sử dụng đối tượng đó thì dùng regular method
    Nếu bạn cần dùng class thì dùng class method
    Trường hợp còn lại (tức là không dùng gì) thì dùng static method
'''
#Tạo lớp kế thừa trong lập trình hướng đối tượng với Python 
print("Tạo lớp kế thừa trong lập trình hướng đối tượng với Python ")

#Tạo lớp kế thừa
print("Tạo lớp kế thừa")

class vietdinh():
    pass
class kubool(vietdinh):
    pass
boolkun = kubool()
print(boolkun)

#Kế thừa thuộc tính
print("Kế thừa thuộc tính")

print("Tạo lớp kế thừa")

class vietdinh():
    suc_manh = 50
class kubool(vietdinh):
    pass
boolkun = kubool()
print("sức mạnh của thằng bool là:",boolkun.suc_manh)

#Giả sử như bạn không muốn thừa hưởng giá trị từ lớp ta kế thừa thì phải làm sao? Đơn giản mà, ta viết lại thôi
print("Kế thừa thuộc tính")

print("Tạo lớp kế thừa")

class vietdinh():
    suc_manh = 50
class kubool(vietdinh):
    suc_manh = 100
boolkun = kubool()
print("sức mạnh của thằng bool là:",boolkun.suc_manh)

#Kế thừa hàm constructor
print("Kế thừa hàm constructor")
'''Ta vừa mới thử thừa kế các thuộc tính ở lớp ta thừa kế (lớp cha), giờ ta thử thừa kế hàm constructor. 
Nếu lớp bạn thừa kế có hàm constructor thì khi bạn thừa kế lớp đó bạn nghiễm nhiên đã có một hàm constructor, và dùng như dùng ở lớp kế thừa. Mời bạn đọc xem ví dụ:'''
class vietdinh():
    suc_manh = 50
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi

class kubool(vietdinh):
    suc_manh = 100
boolkun = kubool("Bool",1)
print(boolkun.__dict__)

'''Vậy câu hỏi đặt ra là ta muốn thêm một số thuộc tính nữa cho lớp siêu nhân gao thì sao? 
Giả sử ta cũng muốn thêm một thuộc tính nữa là sư thú mà siêu nhân gao đó có khi khởi tạo. Và muốn thay đổi thì ta viết lại thôi.'''
class vietdinh():
    suc_manh = 50
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi

class kubool(vietdinh):
    suc_manh = 100
    def __init__(self,ten,tuoi,noisinh):
        self.ten = ten
        self.tuoi = tuoi
        self.noisinh = noisinh

boolkun = kubool("Bool",1,"Phú Yên")
print(boolkun.__dict__)

'''Tại sao ta phải ghi lại gần như là hết cả hàm constructor như lớp cha. Có cách nào nhanh gọn giúp ta đỡ việc copy 
paste lại phương thức từ hàm constructor lớp cha mà chỉ cần thêm những thuộc tính mới thôi không? Có đấy. 
Ví dụ sau đây sẽ dùng phương pháp đó và đây là cách người ta hay dùng chứ không phải cách bên trên.'''

class vietdinh():
    suc_manh = 50
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi

class kubool(vietdinh):
    suc_manh = 100
    def __init__(self,ten,tuoi,noisinh):
        super().__init__(ten,tuoi)
        self.noisinh = noisinh

boolkun = kubool("Bool",1,"Phú Yên")
print(boolkun.__dict__)

#Kế thừa phương thức
print("Kế thừa phương thức")

class vietdinh():
    suc_manh = 50
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def xinchao(self):
        print("xin chào: "+self.ten)

class kubool(vietdinh):
    suc_manh = 100
    def __init__(self,ten,tuoi,noisinh):
        super().__init__(ten,tuoi)
        self.noisinh = noisinh

boolkun = kubool("Bool",1,"Phú Yên")
print(boolkun.__dict__)
boolkun.xinchao()