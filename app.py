import streamlit as st
import pygame
import random
import numpy as np
from PIL import Image

# Inizializzazione di Pygame
pygame.init()

# Dimensioni finestra di gioco
WIDTH, HEIGHT = 800, 400

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Caricamento delle immagini
girl_img = pygame.image.load("girl.png")
girl_img = pygame.transform.scale(girl_img, (50, 50))
sneaker_img = pygame.image.load("sneaker.png")
sneaker_img = pygame.transform.scale(sneaker_img, (50, 50))

# Funzione per creare una nuova sneaker
def spawn_sneaker():
    return [WIDTH, random.randint(50, HEIGHT - 50)]

# Funzione principale
def main():
    st.title("Girl's Catching Game")
    st.write("Use the arrow keys to move the girl and catch the sneakers!")

    # Avvio del gioco
    if st.button("Start Game"):
        sneaker_list = []
        score = 0
        sneaker_speed = 5

        while True:
            sneaker_speed *= 1.0001  # Aumento esponenziale della velocità

            # Movimento delle sneakers
            for sneaker in sneaker_list:
                sneaker[0] -= sneaker_speed

            # Generazione di nuove sneakers
            if np.random.rand() < 0.03:
                sneaker_list.append(spawn_sneaker())

            # Disegno del personaggio e delle sneakers
            girl_pil_img = Image.fromarray(pygame.surfarray.array3d(girl_img))
            st.image(girl_pil_img, width=50)

            for sneaker in sneaker_list:
                sneaker_pil_img = Image.fromarray(pygame.surfarray.array3d(sneaker_img))
                st.image(sneaker_pil_img, width=50)

            # Aggiornamento del punteggio
            st.write(f"Score: {score}")

            st.write("")

            # Controllo delle collisioni e fine del gioco
            if any(sneaker[0] <= 0 for sneaker in sneaker_list):
                break

if __name__ == "__main__":
    main()
