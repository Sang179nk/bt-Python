"""
In một bảng số thỏa mãn điều kiện:

Bảng số gồm 10 hàng và 10 cột
Các giá trị trong Pythonột là liên tiếp nhau
Các giá trị trong hàng hơn kém nhau 10
"""
print("In bang so:")
for i in range(0, 10):
    for j in range(i+1, 101, 10):
        print("{:<3}".format(j), end=" ")
    print()