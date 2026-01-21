# 11-mashq
def yaqin_juft(n):
    return n if n % 2 == 0 else n - 1
# 12-mashq
def uzunlik_lugat(sozlar):
    return {soz: len(soz) for soz in sozlar}
# 13-mashq
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# 14-mashq
def faqat_sonlar(royxat):
    return [x for x in royxat if isinstance(x, (int, float))]
# 15-mashq
def umumiy_harflar(a, b):
    return list(set(a.lower()) & set(b.lower()))
