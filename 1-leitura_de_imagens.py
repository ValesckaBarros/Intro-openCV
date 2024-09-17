import cv2
from matplotlib import pyplot as plt

# Leitura da imagem
imagem = cv2.imread('dog.jpg')

# Exibir a imagem com OpenCV
cv2.imshow('Imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exibir a imagem com Matplotlib (em RGB)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
plt.imshow(imagem_rgb)
plt.axis('off')
plt.show()
