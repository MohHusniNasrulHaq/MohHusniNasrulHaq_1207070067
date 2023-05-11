import numpy as np #mengimport/memanggil library numpy
import imageio #mengimport library imageio
import matplotlib.pyplot as plt #mengimport library matplotlib

img = imageio.imread("gedung-dpr.jpg") #membaca gambar yang diupload 

img_height = img.shape[0] #mendapatkan dimensi ketinggian dalam gambar yang dimasukan
img_width = img.shape[1] #mendapatkan dimensi lebar dalam gambar yang dimasukan
img_channel = img.shape[2] #mendapatkan atau mengakses warna
img_type = img.dtype #mendapatkan tipe atau membaca dari image yang diinputkan

img_flip_horizontal = np.zeros(img.shape, img_type) #membuat variable horizontal untuk mengubah semua elemen array menjadi 0 tanpa terkecuali
img_flip_vertical = np.zeros(img.shape, img_type) #membuat variable vertikal untuk mengubah semua elemen array menjadi 0 tanpa terkecuali

for y in range(0, img_height):#variabel y dalam rentang 0 dalam dimensi ketinggian di gambar 
    for x in range(0, img_width): #variabel x dalam rentang 0 dalam dimensi lebar di gambar 
        for c in range(0, img_channel): #variabel c dalam rentang 0 dalam dimensi ketinggian di gambar 
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c] #membalik gambar menjadi horizontal

for y in range(0, img_height):#variabel y dalam rentang 0 dalam dimensi ketinggian di gambar 
    for x in range(0, img_width):#variabel x dalam rentang 0 dalam dimensi lebar di gambar 
        for c in range(0, img_channel):#variabel c dalam rentang 0 dalam dimensi ketinggian di gambar 
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c] #membalik gambar menjadi vertikal

plt.imshow(img_flip_horizontal) #memanggil gambar yang sudah diinputkan dengan gambar horizontal
plt.title("Flip Horizontal")  #memberikan judul hasil plot di grafik
plt.show() #menampilkan gambar
plt.imshow(img_flip_vertical) #menampilkan gambar yang sidah diinputkan dengan gambar vertikal
plt.title("Flip Vertical") #memberi judul
plt.show() # menampilkan gambar dengan fungsi plot
