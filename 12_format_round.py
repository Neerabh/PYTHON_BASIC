#this code is used to limit decimal values upto two digit number
>>> 125650429603636838/(2**53)
13.949999999999999

>>> 234042163/(2**24)
13.949999988079071

>>> a = 13.946
>>> print(a)
13.946
>>> print("%.2f" % a)
13.95
>>> round(a,2)
13.949999999999999
>>> print("%.2f" % round(a, 2))
13.95
>>> print("{:.2f}".format(a))
13.95
>>> print("{:.2f}".format(round(a, 2)))
13.95
>>> print("{:.15f}".format(round(a, 2)))
13.949999999999999