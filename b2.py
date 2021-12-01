"""
Viết một chương trình tính giai thừa của một số nguyên dương n.
Với n được nhập từ bàn phím.
 Ví dụ, n = 8 thì kết quả đầu ra phải là 1*2*3*4*5*6*7*8 = 40320.

"""
n = int(input("Nhập số cần tính giai thừa: "))


def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)


print(giaiThua(n))
