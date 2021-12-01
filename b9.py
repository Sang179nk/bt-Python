"""
Viết chương trình phân tích số nguyên n thành các thừa số nguyên tố trong Python.
Ví dụ: 100 = 2x2x5x5.
"""


def phanTichSoNguyen(n):
    i = 2;
    listNumbers = [];
    # phân tích
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            listNumbers.append(i);
        else:
            i = i + 1;
    # nếu listNumbers trống thì add n vào listNumbers
    if (len(listNumbers) == 0):
        listNumbers.append(n);
    return listNumbers;


n = int(input("Nhập số nguyên dương n = "));
# phân tích số nguyên dương n
listNumbers = phanTichSoNguyen(n);
size = len(listNumbers);
sb = "";
for i in range(0, size - 1):
    sb = sb + str(listNumbers[i]) + " x ";
sb = sb + str(listNumbers[size - 1]);
# in kết quả ra màn hình
print("Kết quả:", n, "=", sb);