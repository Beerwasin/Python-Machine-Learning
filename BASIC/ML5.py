import numpy as np
import matplotlib.pyplot as plt

rng=np.random
x=rng.rand(50)*10   #randสุ่มตัวเลขค่าบวก

y=2*x+rng.randn(50)    #randnสุ่มตัวเลขค่าลบ

plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#y=ax+c