import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread("arvore.jpg")  
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar detecção de bordas (Canny)
bordas = cv2.Canny(imagem_cinza, 100, 100)

# Exibir as imagens (original e com bordas)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(bordas, cmap="gray")
plt.title("Detecção de Bordas - Canny")
plt.axis("off")

plt.show()
