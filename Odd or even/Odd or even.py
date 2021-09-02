# 寫一個程式，當使用者輸入一個介於一定範圍（例如 1 到 1000）的數字，它能夠辨別奇偶，並輸出檢驗結果給使用者。
#
# 範例：
#
# 畫面：輸入一個數字
# 輸入：25
# 輸出：奇數

def 判斷是否為奇數偶數(number):
    if (number % 2) == 0:
        print("{0} is Even".format(number))
    else:
        print("{0} is Odd".format(number))

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    判斷是否為奇數偶數(number=number)
