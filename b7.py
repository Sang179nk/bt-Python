"""
Viết chương trình liệt kê n số nguyên tố đầu tiên trong Python.
Số nguyên dương n được nhập từ bàn phím.
"""
import math

"""
 * check so nguyen to
 * 
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return true la so nguyen so, 
 *         false khong la so nguyen to
"""


def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;

    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;


n = int(input("Nhập số nguyên dương n = "));
print(n, "Số nguyên tố đầu tiên là:");
dem = 0;  # đếm số số nguyên tố
i = 2;  # tìm số nguyên tố bắt dầu từ số 2
sb = "";
while (dem < n):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " ";
        dem = dem + 1;
    i = i + 1;
print(sb);