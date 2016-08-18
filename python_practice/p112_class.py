class Bank:
    def __init__(self, name, pList):
        self.name = name
        self.proList = pList

    def accountTotal(self):
        return {"name": self.name, "Total":sum(self.proList)}

    def addProperty(self, n):
        self.proList.append(n)

    def __str__(self):
        return "Total: {0}".format(sum(self.proList))