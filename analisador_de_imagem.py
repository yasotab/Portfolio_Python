import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pyttsx3

def load_image(path):
    """
    Carrega a imagem do caminho especificado.
    """
    image = cv2.imread(path)
    return image

def describe_image(image):
    """
    Descreve a imagem carregada.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objects = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if area > 100 and aspect_ratio > 0.5:
            objects += 1
    speak(f"A imagem tem {objects} objetos.")

def understand_image(image):
    """
    Entende o que aparece na imagem.
    """
    objects = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if area > 100 and aspect_ratio > 0.5:
            objects.append((x, y, w, h))
    return objects

def suggest_items(objects):
    """
    Sugere itens relacionados ao usuário com base nos objetos detectados.
    """
    items = []
    for obj in objects:
        x, y, w, h = obj
        if w > 100 and h > 100:
            items.append("Um objeto grande")
        elif w < 50 and h < 50:
            items.append("Um objeto pequeno")
        else:
            items.append("Um objeto médio")
    speak("Os objetos detectados são: " + ", ".join(items))

def speak(text):
    """
    Converte texto em voz.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def main():
    """
    Função principal do programa.
    """
    path = "imagem.jpg"  # Substitua com o caminho da imagem que você deseja analisar
    image = load_image(path)
    describe_image(image)
    objects = understand_image(image)
    suggest_items(objects)

if __name__ == "__main__":
    main()
