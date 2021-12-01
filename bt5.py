"""
bảng cửu chương rút gọn
"""
start = 2
end = 11

print("In bang cuu chuong rut gon:");
for i in range(start, end):
    count = i;
    for j in range(1, 11):
        print("{:<3}".format(count * j), end=" ")
    print("")