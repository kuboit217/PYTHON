'''Dict(Dictionary) cũng là một container như LIST, TUPLE. 
Có điều khác biệt là những container như List, Tuple có các index để phân biệt các phần tử thì Dict dùng các key để phân biệt.
Một Dict gồm các yếu tố sau:
 Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
 Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
 Các phần tử của Dict phải là một cặp key-value
 Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
 Các key buộc phải là một hash object'''


#Cách khởi tạo Dict
print("Cách khởi tạo Dict")
#Sử dụng cặp dấu ngoặc {} và đặt giá trị bên trong
#{<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>}
dic = {'Name': 'Lang Việt', 'Họ':'Đinh'}
print(dic)
print(type(dic))

empty_dict = {} # khởi tạo dict rỗng
print(empty_dict)
print(type(empty_dict))

#Sử dụng Dict Comprehension
print("Sử dụng Dict Comprehension")
dic = { key: value for key, value in [('name','Họ'),('Lang Việt', 'Đinh')]}
print(dic)

#Sử dụng constructor Dict
print('Sử dụng constructor Dict')

#Với dict, ta có 4 cách để khởi tạo một Dict bằng constructor
#Khởi tạo một Dict rỗng
print("Khởi tạo một Dict rỗng")
dic = dict()
print(dic)

#Khởi tạo một dict từ một mapping object
print("Khởi tạo một dict từ một mapping object")
#dict(mapping)
'''Mapping object cũng gần giống so với dict object.
 Một object là Mapping object khi có đủ hai phương thức keys và __getitem__.
 Dict object cũng là một mapping object. Tuy nhiên, không phải mapping object nào cũng là dict 
object vì dict object không chỉ có hai phương thức keys và __getitem__ và còn nhiều phương thức khác.'''

class Map_Class: 
    def keys(self): 
        return [1, 2, 3] 
    def __getitem__(self, key): 
        return key * 2 
map_obj = Map_Class() 
dic = dict(map_obj)
print(dic)

#Khởi tạo bằng iterable
print("Khởi tạo bằng iterable")
#dict(iterable)
'''iterable này đặc biệt hơn hơn các iterable mà bạn dùng để khởi tạo List hay Tuple, 
đó là các phần tử trong iterable phải có 2 value đó chính là cặp key-value.
Bạn có thể dùng List, Tuple hoặc bất cứ container nào (trừ mapping object) để chứa cặp key-value.'''
iter_ = [('name','Việt'),('Tuổi',29)]
dic = dict(iter_)
print(dic)

#Khởi tạo bằng keyword arguments
print("Khởi tạo bằng keyword arguments")
#dict(**kwargs)
#Cứ hiểu đơn giản là giống như việc bạn khởi tạo biến và giá trị rồi đưa cho dict đó giữ giùm.
# Một lưu ý là những biến này không bị ảnh hưởng hoặc ảnh hưởng gì đến các biến bên ngoài
name = "Việt"
tuoi = 29
dic = dict(name="Việt", tuoi=29)
print(dic)
print(name)
print(tuoi)

#Sử dụng Phương thức fromkeys
print("Sử dụng Phương thức fromkeys")
#dict.fromkeys(iterable, value)
#Cách này cho phép ta khởi tạo một dict với các keys nằm trong một iterable. 
# Các giá trị này đều sẽ nhận được một giá trị với mặc định là None
iter_ = ('name','tuoi')
dic_none = dict.fromkeys(iter_)
print(dic_none)
dic_none = dict.fromkeys(iter_,"value")
print(dic_none)

#Lấy value trong Dict bằng key
print("Lấy value trong Dict bằng key")
#Your_dict[key]

print(dic['name'])

#Thay đổi nội dung Dict trong Python
print("Thay đổi nội dung Dict trong Python")
dic['name'] = "Lang Việt"
print(dic['name'])
print(dic)

#Thêm thủ công một phần tử vào dict
print("Thêm thủ công một phần tử vào dict")
#Cách này khá giống với cách bạn thay đổi nội dung của Dict. Khác ở chỗ, bây giờ bạn sẽ sử dụng một key chưa hề có trong dict.
dic['ho'] = "Đinh"
print(dic)

#Các phương thức tiện ích
print("Các phương thức tiện ích")

#Phương thức copy
print('Phương thức copy')
#<Dict>.copy()
#Giống với phương thức copy trong LIST. Để làm gì thì chắc các bạn cũng có thể suy nghĩ ra.
dic_copy = dic.copy()
print(dic)
print(dic_copy)

#Phương thức clear
print("Phương thức clear")
#<Dict>.clear()
#Loại bỏ tất cả những phần tử có trong Dict
dic_copy.clear()
print(dic)
print(dic_copy)

#Các phương thức xử lí
print("Các phương thức xử lí")

#Phương thức get
print("Phương thức get")
#<Dict>.get(key [,default])
#Trả về giá trị của khóa key. Nếu key không có trong Dict thì trả về giá trị default. Default có giá trị mặc định là None nếu chúng ta không truyền vào.
print(dic.get("name"))
print(dic.get('Tenlot'))
print(dic.get('Tenlot','Lang'))
print(dic)

#Phương thức items
print("Phương thức items")
#<Dict>.items()
#Trả về một giá trị thuộc lớp dict_items. Các giá trị của dict_items sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.Dict_items là một iterable.
print(dic.items())
print(type(dic.items()))
list_items = list(dic.items())
print(list_items)
print(list_items[0])
print(list_items[0][1])

#Phương thức keys
print("Phương thức keys")
#<Dict>.keys()
#Trả về một giá trị thuộc lớp dict_keys. Các giá trị của dict_keys sẽ là các key trong Dict.Dict_keys là một iterable.
print(dic.keys())
print(type(dic.keys()))

#Phương thức values
print("Phương thức values")
#<Dict>.values()
#Trả về một giá trị thuộc lớp dict_values. Các giá trị của dict_values sẽ là các value trong Dict. Dict_values là một iterable
print(dic.values())
print(type(dic.values()))
list_values = list(dic.values())
print(list_values)

#Phương thức pop
print("Phương thức pop")
#<Dict>.pop(key [,default])
#Bỏ đi phần tử có key và trả về value của key đó. Trường hợp key không có trong dict.
#Báo lỗi KeyError nếu default là None (ta không thêm vào).
# Trả về default nếu ta thêm default vào

print(dic.pop('ho'))
print(dic)
print(dic.pop("aaaa",'aaa'))
print(dic)

#Phương thức popitem
print("Phương thức popitem")
#<Dict>.popitem()
#Trả về một 2-tuple với key và value tương ứng bất kì (vấn đề này liên quan đến giá trị của hash của key. 
# Do đó bạn cũng hiểu vì sao key buộc phải là một hash object) trong Dict. Và cặp key-value sẽ bị loại bỏ ra khỏi Dict.
# Nếu Dict là một empty Dict. Sẽ có lỗi KeyError

print(dic.popitem())
print(dic)

#Phương thức setdefault
print("Phương thức setdefault")
#<Dict>.setdefault(key [,default])
#Trả về giá trị của key trong Dict. Trường hợp key không có trong Dict thì sẽ trả về giá trị default. 
# Thêm nữa, một cặp key-value mới sẽ được thêm vào Dict với key bằng key và value bằng default.
# Default mặc định là None
print(dic.setdefault("name"))
print(dic)
print(dic.setdefault("tuoi",29))
print(dic)

#Phương thức update
print("Phương thức update")
#<D>.update([E, ]**F)
