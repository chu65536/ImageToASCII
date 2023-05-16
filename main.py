import numpy as np
from PIL import Image, ImageDraw, ImageFont


img = Image.open('src/rat.jpg').convert('L')
arr = np.array(img)

k = int(max(arr.shape[0], arr.shape[1]) / 1000 * 10)
font_size = 6

gscale = "@%#*+=-:. "
gscale = gscale[::-1]

scale_arr = np.zeros(((arr.shape[0] + k - 1) // k, (arr.shape[1] + k - 1) // k))
print()
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if (i % k == 0) and (j % k == 0): 
            scale_arr[i // k, j // k] = arr[i, j] // (255 // len(gscale) + 1)

ascii_img = Image.new('RGB', (scale_arr.shape[1] * font_size, scale_arr.shape[0] * font_size), color = (0, 0, 0))
draw = ImageDraw.Draw(ascii_img)
myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 10)
for i in range(scale_arr.shape[0]):
    str = ''
    for num in scale_arr[i]:
        str += gscale[int(num)]
    draw.text((0, i*font_size), str, fill=(255,255,255),  align='center')

ascii_img.show()

