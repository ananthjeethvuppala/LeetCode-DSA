class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            shift = 0

            while dividend >= (divisor << (shift + 1)):
                shift += 1

            dividend -= divisor << shift
            quotient += 1 << shift

        if negative:
            quotient = -quotient
        
        return quotient