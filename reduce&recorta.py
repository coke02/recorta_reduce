from PIL import Image
import os

def reduce_image_size(image, base_width=800, quality=85):
    w_percent = (base_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    resized_image = image.resize((base_width, h_size), Image.LANCZOS)
    return resized_image

def trim_white_borders(image):
    gray_image = image.convert('L')
    # Convertir en binario: los valores mayores a 250 (casi blanco) se vuelven blancos (255)
    thresholded = gray_image.point(lambda x: 255 if x > 250 else 0)

    # Definir la caja (bbox) para recortar bordes en blanco
    bbox = (40, 40, image.width - 20, image.height - 230)

    # Recortar la imagen basada en el bbox
    cropped_image = image.crop(bbox)
    return cropped_image

def process_images(input_dir, output_dir, base_width=800, quality=85):
    for root, dirs, files in os.walk(input_dir):
        relative_path = os.path.relpath(root, input_dir)
        current_output_dir = os.path.join(output_dir, relative_path)

        if not os.path.exists(current_output_dir):
            os.makedirs(current_output_dir)

        for file in files:
            if file.lower().endswith('.png'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(current_output_dir, file)

                # Abrir la imagen
                image = Image.open(input_path)

                # Reducir el tamaño de la imagen
                resized_image = reduce_image_size(image, base_width, quality)

                # Recortar bordes blancos
                trimmed_image = trim_white_borders(resized_image)

                # Guardar la imagen recortada y reducida
                trimmed_image.save(output_path, quality=quality)
                print(f"Procesada y guardada en {output_path}")

# Rutas de las carpetas de entrada y salida
dir_raiz = 'D:\\ndviValpo'
"""
# Procesar la carpeta "Salida_Imagenes" con subcarpetas
dir_imagenes_originales = os.path.join(dir_raiz, 'Salida_Imagenes')
dir_imagenes_reducidas = os.path.join(dir_raiz, 'Salida_imagenes_reducidas', 'Salida_Imagenes')
process_images(dir_imagenes_originales, dir_imagenes_reducidas)

# Procesar la carpeta "Salida_Climatología" sin subcarpetas
dir_climatologia_original = os.path.join(dir_raiz, 'Salida_Climatología')
dir_climatologia_reducida = os.path.join(dir_raiz, 'Salida_imagenes_reducidas', 'Salida_Climatología')
process_images(dir_climatologia_original, dir_climatologia_reducida)
"""
# Procesar la carpeta "Salida_Climatología" sin subcarpetas
dir_climatologia_original = os.path.join(dir_raiz, 'Salida _Anomalia')
dir_climatologia_reducida = os.path.join(dir_raiz, 'Salida_imagenes_reducidas', 'Salida_Anomalia')
process_images(dir_climatologia_original, dir_climatologia_reducida)