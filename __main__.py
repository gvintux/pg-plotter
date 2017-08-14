from matplotlib import pyplot as plt
import sys

file_path1, file_path2, file_path3 = sys.argv[1:]
file_1 = open(file_path1, 'r')
file_2 = open(file_path2, 'r')
file_3 = open(file_path3, 'r')


x1 = list()
y1 = list()
w1 = list()
x2 = list()
y2 = list()
w2 = list()

x3 = list()
y3 = list()
w3 = list()


line1 = file_1.readline()
line2 = file_2.readline()
line3 = file_3.readline()


while len(line1) > 0:
    x0, y0, w0 = line1.split(",", 3)
    x1.append(x0)
    y1.append(y0)
    w1.append(w0)

    x0, y0, w0 = line2.split(",", 3)
    x2.append(x0)
    y2.append(y0)
    w2.append(w0)
    x0, y0, w0 = line3.split(",", 3)
    x3.append(x0)
    y3.append(y0)
    w3.append(w0)

    line1 = file_1.readline()
    line2 = file_2.readline()

# line1, = plt.plot(x1[0:30], w1[10:40])
# line1.set_antialiased(True)
# line2, = plt.plot(x1[0:30], w2[5:35])

x = x1[0:30]
w1 = w1[10:40]
w2 = w2[5:35]

abs_diff = list()

for i in range(0, len(x)):
    abs_diff.append(abs(float(w2[i]) / float(w1[i])))

plt.plot(x[18:], abs_diff[18:])

# line2.set_antialiased(True)

plt.autoscale(True)
plt.grid(True)
plt.show()