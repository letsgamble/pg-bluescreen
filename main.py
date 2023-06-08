import cv2
import numpy as np


def apply_blue_screen(image_path, background_path):
    """
    Funkcja do nakładania obrazu na tło z zastosowaniem techniki blue screen.

    Parametry:
    image_path (str): Ścieżka do obrazu z blue screen.
    background_path (str): Ścieżka do obrazu tła.

    Zwraca:
    final_image: Obraz wynikowy po zastosowaniu efektu blue screen.
    """
    # Wczytaj obraz i tło
    image = cv2.imread(image_path)
    background = cv2.imread(background_path)

    # Upewnij się, że oba obrazy mają ten sam rozmiar
    background = cv2.resize(background, (image.shape[1], image.shape[0]))

    # Zdefiniuj zakres koloru blue screen
    lower_blue = np.array([0,0,100])
    upper_blue = np.array([100,100,255])

    # Utwórz maskę
    mask = cv2.inRange(image, lower_blue, upper_blue)

    # Wykonaj operację bitwise, aby usunąć blue screen
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Zmień tło, które nie jest blue screenem
    masked_background = cv2.bitwise_and(background, background, mask=cv2.bitwise_not(mask))

    # Połącz obie warstwy
    final_image = cv2.add(masked_image, masked_background)

    # Zwróć wynik
    return final_image


# Przykładowe użycie
final_image = apply_blue_screen('actor.jpg', 'background.jpg')

# Zapisz obraz wynikowy
cv2.imwrite('final_image.jpg', final_image)
