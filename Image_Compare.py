import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# image = plt.imread('OrangeTiger.jpg')
# plt.imshow(image)
# plt.show()

#from PIL import Image

# Открываем изображение
picture = Image.open("OrangeTiger.jpg")

# Получаем rgb составляющую первого пикселя
#r,g,b = picture.getpixel( (0,0) )

# Выводим rgb составляющие
#print("Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))

# Получаем размер изображения (ширину и высоту)
width, height = picture.size

width2 = int(width/2)
height2 = int(height/2)
print(width2, height2)

x_div = 2
y_div = 2
prod = x_div * y_div

# Process every pixel
# Двойной цикл прохода по пикселям с последующим пребразованием


k1 = 0
#for i in range(prod):
for x in range(width2):
   for y in range(height2):
       current_color = picture.getpixel( (x,y) )

       #picture.putpixel( (x,y), (current_color[0] + 50, current_color[1] + 50, current_color[2] + 50))
       k1 = k1 + current_color[0] + current_color[1] + current_color[2]

print(k1)

k2 = 0
# for i in range(prod):
for x in range(width2+1, width):
    for y in range(height2):
        current_color = picture.getpixel((x, y))

        # picture.putpixel( (x,y), (current_color[0] + 50, current_color[1] + 50, current_color[2] + 50))
        k2 = k2 + current_color[0] + current_color[1] + current_color[2]

print(k2)

k3 = 0
# for i in range(prod):
for x in range(width2):
    for y in range(height2+1, height):
        current_color = picture.getpixel((x, y))

        # picture.putpixel( (x,y), (current_color[0] + 50, current_color[1] + 50, current_color[2] + 50))
        k3 = k3 + current_color[0] + current_color[1] + current_color[2]

print(k3)

k4 = 0
# for i in range(prod):
for x in range(width2+1, width):
    for y in range(height2+1, height):
        current_color = picture.getpixel((x, y))

        # picture.putpixel( (x,y), (current_color[0] + 50, current_color[1] + 50, current_color[2] + 50))
        k4 = k4 + current_color[0] + current_color[1] + current_color[2]

print(k4)

k = [k1, k2, k3, k4]
maximum = max(k)
#for i in range(prod):
print(k)
for i in range(len(k)):
    k[i] = k[i]/maximum
print(k)
m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for x in range(prod):
    for y in range(prod):
        m[x][y] = k[x] - k[y]
        m[x][y] = round(m[x][y], 3)
        
print(m)
#r,g,b = picture.getpixel( (0,0) )
#print("Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))
picture.show()