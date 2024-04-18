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
    st.write("Use the dropdown menu in the sidebar to move the girl and catch the sneakers!")

    # Avvio del gioco
    if st.button("Start Game"):
        sneaker_list = []
        score = 0
        sneaker_speed = 5
        girl_x, girl_y = 50, HEIGHT // 2

        while True:
            sneaker_speed *= 1.0001  # Aumento esponenziale della velocità

            # Movimento delle sneakers
            for sneaker in sneaker_list:
                sneaker[0] -= sneaker_speed

            # Generazione di nuove sneakers
            if np.random.rand() < 0.03:
                sneaker_list.append(spawn_sneaker())

            # Disegno del personaggio e delle sneakers
            st.image(girl_img, width=50, caption="Girl")
            for sneaker in sneaker_list:
                st.image(sneaker_img, width=50, caption="Sneaker")

            # Aggiornamento del punteggio
            st.write(f"Score: {score}")

            st.write("")

            # Controllo delle collisioni e fine del gioco
            if any(sneaker[0] <= 0 for sneaker in sneaker_list):
                break

            # Movimento del personaggio tramite la barra laterale
            direction = st.sidebar.selectbox("Move the girl", ["Up", "Down"])
            if direction == "Up" and girl_y > 0:
                girl_y -= 5
            elif direction == "Down" and girl_y < HEIGHT - 50:
                girl_y += 5

if __name__ == "__main__":
    main()
