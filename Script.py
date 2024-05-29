import cv2
import numpy as np
import os

def apply_filter(image_path, choice):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Erro ao carregar a imagem no caminho: {image_path}")
        return None

    if choice == 1:
        # Filtro de Média (Blur)
        filtered_image = cv2.blur(image, (5, 5))
    elif choice == 2:
        # Filtro Gaussiano
        filtered_image = cv2.GaussianBlur(image, (5, 5), 0)
    elif choice == 3:
        # Filtro de Mediana
        filtered_image = cv2.medianBlur(image, 5)
    elif choice == 4:
        # Filtro Laplaciano
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered_image = cv2.Laplacian(gray, cv2.CV_64F)
    elif choice == 5:
        # Filtro Sobel
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        filtered_image = cv2.magnitude(sobelx, sobely)
    elif choice == 6:
        # Filtro Canny
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered_image = cv2.Canny(gray, 100, 200)
    elif choice == 7:
        # Ajuste de Brilho
        brightness = 50
        filtered_image = cv2.convertScaleAbs(image, alpha=1, beta=brightness)
    elif choice == 8:
        # Granulação
        noise = np.random.normal(0, 25, image.shape)
        filtered_image = cv2.add(image, noise.astype(np.uint8))
    elif choice == 9:
        # Suavização
        filtered_image = cv2.bilateralFilter(image, 9, 75, 75)
    else:
        print("Escolha inválida.")
        return None

    return filtered_image

def main():
    image_path = "./fotoTeste.jpg"
    print("Escolha um filtro para aplicar à imagem:")
    print("1. Filtro de Média (Blur)")
    print("2. Filtro Gaussiano")
    print("3. Filtro de Mediana")
    print("4. Filtro Laplaciano")
    print("5. Filtro Sobel")
    print("6. Filtro Canny")
    print("7. Brilho")
    print("8. Granulação")
    print("9. Suavização")

    choice = int(input("Digite o número do filtro desejado: "))
    filtered_image = apply_filter(image_path, choice)

    if filtered_image is not None:
        cv2.imshow('Imagem Filtrada', filtered_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        base_name = "fotoResultado"
        ext = ".jpg"
        save_dir = os.path.dirname(image_path)
        save_path = os.path.join(save_dir, base_name + ext)
        counter = 1

        while os.path.exists(save_path):
            save_path = os.path.join(save_dir, f"{base_name}({counter}){ext}")
            counter += 1

        cv2.imwrite(save_path, filtered_image)
        print(f"Imagem salva como: {save_path}")

if __name__ == "__main__":
    main()
