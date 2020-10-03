'''LIST là một container được sử dụng rất nhiều trong các chương trình Python. Một List gồm các yếu tố sau:
 Được giới hạn bởi cặp ngoặc [ ], tất cả những gì nằm trong đó là những phần tử của List.
 Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
 List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó! (một trường hợp hay ho Kteam sẽ giới thiệu ở phần khác).'''

#Cách khởi tạo List
#Sử dụng cặp dấu ngoặc [] đặt giá trị bên trong
#[<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>]
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list1)
list2 = [[1,2],[3,4]]
print(list2)
print(list2[0][1])

#Sử dụng List Comprehension
#[Comprehension]
list3 = [i for i in range(10)]
print(list3)
list4 = [[i,i*1,i*2,i*3] for i in range(1,5)]
print(list4)
#List comprehension là một cách khởi tạo một List rất thú vị trong Python. 
# Do đó, rất khó để có thể nói hết các trường hợp. 
# Vì vậy, hãy tạm gác lại kiến thức này, bạn không cần phải cố gắng hiểu nó khi chúng ta chưa gặp gỡ các vòng lặp.

#Sử dụng constructor List
#list (iterable)
#iterable là một đối tượng nói chung của các container. 
# Khái niệm này sẽ được Kteam giới thiệu ở bài sau. Đối với bạn khi theo dõi khóa học này của Kteam, 
# bạn đã được biết hai iterable đó chính là chuỗi, và List.
list5 = list("Đinh Lang Việt") #phải bắt đầu bằng chuỗi
print(list5)

#Một số toán tử với List trong Python
#Toán tử +
list6 = [1,2]
list7 = ["viet","dinh"]
list7 += ["Lang"]
print(list6+list7)
print(list7)
#List cộng chuỗi cho phép, chuỗi cộng List thì không

#Toán tử *
list8 = ["Lang","Viet"]
list8 *= 2
print(list8)

#Toán tử in
true = 'Lang' in list8
print(true)

#Indexing và cắt List trong Python
lst = [1, 2, 'a', 'b', [3, 4]]
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[1:3])
print(lst[:3])
print(lst[2:])
print(lst[::-1])

#Thay đổi nội dung List trong Python
lst[0] = "one"
print(lst)

#Ma trận
lst = [[1, 2, 3], [4, 5, 6]]
print(lst)
print(lst[0])
print(lst[-1])
#Hai giá trị đó cũng là một List. 
# Và lẽ dĩ nhiên, bạn có quyền truy cập đến các phần tử con của phần tử nằm trong List bạn vừa khởi tạo. Thậm chí là cắt List!
print(lst[0][1])
print(lst[1][1])
print(lst[1][:])

#Vấn đề cần lưu tâm khi sử dụng List
#Không được phép gán List này qua List kia nếu không có chủ đích
#Chỉnh một, nhưng đổi tới hai. Lí do là vì khi bạn gán giá trị List trực tiếp như thế, bạn đang đưa hai List đó trỏ cùng vào một nơi.
#Do đó, trước khi gán, bạn phải copy giá trị của List
lst=[1,2,3]
lst1 = list(lst)#cách 1
lst2 = lst[:] #cách 2
print(lst)
print(lst1) 
print(lst2)
lst1[0] = "one"
print(lst)
print(lst1) # Giá trị của list copy sẽ không thay đổi.
print(lst2)

#nó chỉ sao chép các phần tử của List. Không hề sao chép các phần tử con của các phần tử nằm trong List. 
# Do đó, nếu bạn thay đổi các phần tử trong List thì không sao, 
# tuy nhiên nếu thay đổi phần tử con của các phần tử trong List, thì vấn đề lại xuất hiện.
