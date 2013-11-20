import math
import datetime
import fractions
import random

abs  = abs
cos  = math.cos
acos = math.acos
sin  = math.sin
asin = math.asin
tan  = math.tan
atan = math.atan
ln   = math.log
log  = math.log10

gcd = fractions.gcd
lcm = lambda a, b: (a * b) // gcd(a, b)

dayOfWk = lambda year, month, day: (datetime.date(year, month, day).weekday() + 2) % 7

iPart = int
fPart = lambda x: x - int(x)

int = lambda x: iPart(x) if x >= 0 else -1 + iPart(x)

rand = lambda: round(random.random(), 10)

not = lambda x: 0 if x else 1
