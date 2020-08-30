from scipy.io import loadmat
import matplotlib.pyplot as plt 

mnist_raw=loadmat("mnist-original.mat")

mnist={
    "data":mnist_raw["data"].T,        #ข้อมูลลายมือชุดเรียนรู้เลข 1-9
    "target":mnist_raw["label"][0]     #ตัวเลขเฉลยว่าเลขที่เขียนคือ 1-9
}
x,y=mnist["data"],mnist["target"]

number=x[15000]
number_image=number.reshape(28,28)       #reshapeขนาดรูป 28x28

print(y[15000])

plt.imshow(
    number_image,
    cmap=plt.cm.binary,
    interpolation="nearest"
)
plt.show()

print(x.shape)





#print(mnist_raw.keys())    #ใช้เช็คKeysคำสั่ง
