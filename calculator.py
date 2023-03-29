# a = input()
# n = int(input())
#
# power = 1
# ans = 0
# for i in a[::-1]:
#     if i < "A":
#         ans += int(i) * power
#     else:
#         ans += (ord(i) - ord("A") + 10)*power
#     power *= n
#
# print(ans)


# a = int(input())
# n = int(input())
#
# count = ""
#
# while a > 0:
#     count = str(a % n) + count
#     a //= n
# print(count)


digit = int(input())
digit_bin = bin(digit)
digit_oct = oct(digit)
digit_hex = hex(digit).upper()

print(digit_bin[2:])
print(digit_oct[2:])
print(digit_hex[2:])