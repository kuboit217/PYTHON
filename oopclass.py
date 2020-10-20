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