class facto:
    no = 0
    def __init__(self):
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        facto.no += 1
        self.i *= facto.no
        return self.i


f = facto()
for fo in f:
    if fo > 10000:
        break
    print(fo)