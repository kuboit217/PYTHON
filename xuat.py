#Tìm hiểu cách sử dụng hàm print thông qua các parameter
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#*objects
print("objects")
#* chính là packing argument. Ở đây hiểu nôm na sẽ là nó sẽ gom lại các argument của bạn lại thành một Tuple.
packing = 1, 2, 3, 4 # giống như gọi hàm function(1, 2, 3, 4)
print(packing)
#Khi bạn truyền các argument vào hàm (giá trị 1, giá trị 2, giá trị 3,…) thì nó sẽ gói lại thành một Tuple giống như trên.
'''Nhờ như vậy, bạn có thể truyền argument vào hàm print với số lượng bất kì. Điều này giúp bạn không phải ép kiểu dữ liệu, 
để rồi nối chúng lại với nhau thành một giá trị rồi mới truyền cho hàm print.'''

#sep (separate – chia ra, phân ra)
print("sep (separate – chia ra, phân ra)")
'''Giá trị mặc định của parameter này là một khoảng trắng. Khi các argument bạn ném vào cho hàm print để hàm print in ra nội dung, như đã biết là nó sẽ được gói vào một Tuple. 
Các giá trị trong Tuple sẽ được nối với nhau bằng parameter sep.
Lưu ý: Khi truyền giá trị vào cho parameter theo cách keyword argument thì sẽ không bị packing. Nghĩa là sẽ không bị gói vào trong giá trị của parameter object.'''

print('việt','đinh') # sep mặc định là một khoảng trắng
print("việt", "đinh" , sep="--") # đổi sep thành --

#end (kết thúc bằng)
print("end (kết thúc bằng)")
from time import sleep # nhập hàm sleep từ thư viện time 
print('start....') 
sleep(3) # dừng chương trình 3 giây 
print('end...')


from time import sleep # nhập hàm sleep từ thư viện time
print('start....', end='') # in ra nội dung và kết thúc bới một chuỗi rỗng
sleep(3) # dừng chương trình 3 giây
print('end...')
