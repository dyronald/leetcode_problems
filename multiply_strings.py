class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_n = self._to_num(num1)
        answer = []
        offset = 0

        for n in num1_n:
            num2_n = self._to_num(num2)
            sub_ans = self._sub_mult(n, num2_n)
            self._add(answer, sub_ans, offset)
            offset += 1

        return ''.join(str(a) for a in reversed(answer)).lstrip('0') or '0'

    def _add(self, accumulator, sub_ans, offset):
        carry = 0

        i = offset
        for sa_digit in sub_ans:
            if i >= len(accumulator):
                accumulator.append(0)
            acc_digit = accumulator[i]

            sub_sum = acc_digit + sa_digit + carry
            carry = sub_sum // 10
            accumulator[i] = sub_sum % 10
            i += 1

        accumulator.append(carry)

    def _sub_mult(self, n, num2_n):
        carry = 0
        for n2 in num2_n:
            step_prod = (n * n2) + carry
            carry = step_prod // 10
            yield step_prod % 10
        yield carry
            
    def _to_num(self, num):
        for n in reversed(num):
            yield int(n)
