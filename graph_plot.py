import matplotlib.pyplot as plt
  
x = []
y = []
x1 = []
y1 = []

x2 = []
y2 = []
mod=1000000007
file1 = open('output/output_graph/twitter_combined_WC_discountdegree_15_50_1487723611282_1682961553699.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    count += 1
    line = line.strip()
    line = line[0:len(line)-2]
    lines = [i for i in line.split(", ")]
    if len(lines) == 1:
        continue
    

    x2.append(count)
    y2.append(lines[0])

    for i in range(len(lines)):
        x.append(count)
        y.append(int(lines[i])%mod)
    x1.append(x)
    #y=y%mod
    y1.append(y)

y1.sort()
plt.scatter(x1, y1)
plt.show()


y2.sort()
plt.plot(x2, y2)
plt.show()
