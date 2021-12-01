"""
Viết chương trình liệt kê tất cả số nguyên tố có 5 chữ số trong Python.
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


print("Liệt kê tất cả số nguyên tố có 5 chữ số:");
dem = 0;
for i in range(10001, 99999):
    if (isPrimeNumber(i)):
        print(i);
        dem = dem + 1;
print("Tổng các số nguyên tố có 5 chữ số là:", dem);