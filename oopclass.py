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
