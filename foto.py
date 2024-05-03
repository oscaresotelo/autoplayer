# import base64
# from PIL import Image

# # Código para ejecutar la aplicación deseada
# executable_code = '''
# import os
# os.system("notepad.exe")
# '''

# # Codifica el código ejecutable en base64
# encoded_code = base64.b64encode(executable_code.encode()).decode()

# # Obtén los bits del código ejecutable
# bits = [int(bit) for bit in ''.join(format(ord(c), '08b') for c in encoded_code)]

# # Abre la imagen
# image = Image.open('lobo.png')

# # Convierte la imagen en modo RGBA
# image_rgba = image.convert('RGBA')

# # Obtiene los píxeles de la imagen
# pixels = list(image_rgba.getdata())

# # Oculta los bits del código ejecutable en los componentes menos significativos de los píxeles
# new_pixels = []
# bit_index = 0
# for pixel in pixels:
#     if bit_index < len(bits):
#         r, g, b, a = pixel
#         new_r = (r & 0xFE) | bits[bit_index]
#         new_g = (g & 0xFE) | bits[bit_index+1]
#         new_b = (b & 0xFE) | bits[bit_index+2]
#         new_pixel = (new_r, new_g, new_b, a)
#         new_pixels.append(new_pixel)
#         bit_index += 3
#     else:
#         new_pixels.append(pixel)

# # Crea una nueva imagen con los píxeles modificados
# new_image = Image.new('RGBA', image.size)
# new_image.putdata(new_pixels)

# # Guarda la nueva imagen con el código ejecutable oculto
# new_image.save('imagen_con_codigo_modificada.png')


import base64
import os
from PIL import Image

# Abre la imagen con el código oculto
image = Image.open('imagen_con_codigo_modificada.png')

# Convierte la imagen en modo RGBA
image_rgba = image.convert('RGBA')

# Obtiene los píxeles de la imagen
pixels = list(image_rgba.getdata())

# Extrae los bits ocultos del código ejecutable
bits = []
for pixel in pixels:
    r, g, b, _ = pixel
    bits.extend([r & 1, g & 1, b & 1])

# Convierte los bits en una cadena binaria
binary_data = ''.join(map(str, bits))

# Decodifica los datos binarios base64 sin decodificar a UTF-8
encoded_code = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
executable_code = base64.b64decode(encoded_code.encode())

# Ejecuta el código oculto para abrir el Notepad
exec(executable_code)
