import numpy as np
import matplotlib.pyplot as plt

# Данная реализация программы обрабатывает ошибки, которые могут возникнуть при выполнении функции linear_equalization, и не завершается в случае ошибки. 
# Вместо этого программа продолжает свою работу и выводит на экран только те изображения, для которых эквализация прошла без ошибок.

def linear_equalization(img):
    try:
        if img.ndim != 2:
            raise ValueError('Изображение должно быть 2D')
        if img.dtype != np.uint8:
            raise TypeError('Изображение должно быть uint8')

        # получаем гистограмму изображения
        hist, bins = np.histogram(img.flatten(), 256, [0, 256])
        # вычисляем вероятности появления яркостных значений
        prob = hist / np.sum(hist)
        # получаем функцию преобразования яркости
        cdf = np.cumsum(prob)
        # выполняем эквализацию
        img_eq = np.interp(img.flatten(), bins[:-1], cdf * 255)
        img_eq = img_eq.reshape(img.shape).astype(np.uint8)
        return img_eq
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# загружаем три изображения и применяем эквализацию
img = plt.imread(r'C:\Users\Niemus\YandexDisk\Прочее\VS CODE - PROJECTS\image2.jpg')  
img2 = plt.imread(r'C:\Users\Niemus\YandexDisk\Прочее\VS CODE - PROJECTS\image3.jpg')  
img3 = plt.imread(r'C:\Users\Niemus\YandexDisk\Прочее\VS CODE - PROJECTS\image4.jpg')  

img_gray = np.mean(img, axis=2).astype(np.uint8)
img_eq = linear_equalization(img_gray)

img_gray2 = np.mean(img2, axis=2).astype(np.uint8)
img_eq2 = linear_equalization(img_gray2)

img_gray3 = np.mean(img3, axis=2).astype(np.uint8)
img_eq3 = linear_equalization(img_gray3)

# выводим изображения на экран
if img_eq is not None:
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_gray, cmap='gray')
    axs[0].set_title('Оригинальное изображение')
    axs[1].imshow(img_eq, cmap='gray')
    axs[1].set_title('После эквализации')
    plt.show()

if img_eq2 is not None:
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_gray2, cmap='gray')
    axs[0].set_title('Оригинальное изображение')
    axs[1].imshow(img_eq2, cmap='gray')
    axs[1].set_title('После эквализации')
    plt.show()

if img_eq3 is not None:
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_gray3, cmap='gray')
    axs[0].set_title('Оригинальное изображение')
    axs[1].imshow(img_eq3, cmap='gray')
    axs[1].set_title('После эквализации')
    plt.show()
