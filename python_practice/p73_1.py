with open("nine.txt", "w") as f:
    for i in range(1,10):
        for j in range(1, 10):
            f.write("{0}*{1}={2}\n".format(i, j, i*j))
        f.write("\n")