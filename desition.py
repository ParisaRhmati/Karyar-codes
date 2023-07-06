def flip_bit(bit):
    if bit == "0":
        return "1"
    else:
        return "0"


def build_string(n):
    string = "1"  # رشته اولیه
    for _ in range(n - 1):
        reversed_string = string[::-1]  # معکوس کردن رشته فعلی
        complemented_string = "".join(
            flip_bit(bit) for bit in reversed_string)  # تبدیل هر بیت به عکس آن
        string += complemented_string  # اضافه کردن رشته تبدیل شده به انتهای رشته فعلی
    return string


def print_substring(string, l, r):
    substring = string[l - 1:r]  # برش رشته در بازه مورد نظر
    print(substring, end="")


l, r = map(int, input().split())  # دریافت ورودی از کاربر
string = build_string(r)  # ساخت رشته با توجه به اندازه r
print_substring(string, l, r)  # نمایش بازه مورد نظر
