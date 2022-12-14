import numpy
import matplotlib.pyplot as mpl

n = 5
x = numpy.linspace(-1, 1, n)


def funkcja(x):
    wynik_funkcji = 1 / (1 + 25 * (x * x))
    return wynik_funkcji


y = funkcja(x)

xx = numpy.linspace(-1, 1, 10000)

yy = numpy.polyval(numpy.polyfit(x, y, len(x) - 1), xx)

er = numpy.abs(yy - funkcja(xx))

erer = max(er)
print(erer)
mpl.plot(xx, funkcja(xx), label="func")
mpl.plot(xx, yy, label='interpol func')
mpl.plot(xx, er, label='error')
mpl.legend()
mpl.show()