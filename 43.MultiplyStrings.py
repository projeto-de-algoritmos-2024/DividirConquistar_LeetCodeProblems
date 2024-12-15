#Medium (Karatsuba)

class Solution:
    def multiply(self, num1, num2):
        def karatsuba(x, y):
            if x < 10 or y < 10:
                return x * y

            n = max(len(str(x)), len(str(y)))
            m = n // 2

            high1, low1 = divmod(x, 10**m)
            high2, low2 = divmod(y, 10**m)

            z0 = karatsuba(low1, low2)
            z1 = karatsuba((low1 + high1), (low2 + high2))
            z2 = karatsuba(high1, high2)

            return z2 * 10**(2 * m) + (z1 - z2 - z0) * 10**m + z0

        int_num1 = int(num1)
        int_num2 = int(num2)

        product = karatsuba(int_num1, int_num2)

        return str(product)

# Testes
solution = Solution()

num11 = "2"
num21 = "3"
print(solution.multiply(num11, num21))

num12 = "123"
num22 = "456"
print(solution.multiply(num12, num22))