from matplotlib import pyplot as plt

x = [1,3,5,30,55,100]
x2 = [3,5,10,29,50,120]
y = range(len(x))

plt.title("Matplotlib Graph", {"fontsize":25})
plt.xlabel("x-number", {"fontsize":15})
plt.ylabel("y-number", {"fontsize":15})

plt.plot(x,y, label='graph1')
plt.plot(x2,y, label='graph2')
plt.legend()

"fig = plt.figure()"
"fig.add_subplot(1,1,1)"
plt.savefig('test.png')
plt.show()
