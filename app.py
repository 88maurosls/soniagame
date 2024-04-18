import streamlit as st
import pygame
import random
import numpy as np

# Inizializzazione
pygame.init()

# Dimensioni finestra di gioco
WIDTH, HEIGHT = 800, 400

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Personaggio
girl_img = pygame.image.load("girl.png")
girl_img = pygame.transform.scale(girl_img, (50, 50))
girl_vel = 5

# Sneakers (ostacoli)
sneaker_img = pygame.image.load("sneaker.png")
sneaker_img = pygame.transform.scale(sneaker_img, (50, 50))
sneaker_list = []
sneaker_speed = 5

# Punteggio
score = 0

# Funzione per muovere le sneakers
def move_sneakers():
    global sneaker_speed
    for sneaker in sneaker_list:
        sneaker[0] -= sneaker_speed

# Funzione per creare nuove sneakers
def spawn_sneaker():
    sneaker_list.append([WIDTH, random.randint(50, HEIGHT - 50)])

# Funzione per controllare le collisioni
def check_collisions():
    global score

    girl_rect = pygame.Rect(50, HEIGHT // 2, girl_img.get_width(), girl_img.get_height())
    for sneaker in sneaker_list:
        sneaker_rect = pygame.Rect(sneaker[0], sneaker[1], sneaker_img.get_width(), sneaker_img.get_height())
        if girl_rect.colliderect(sneaker_rect):
            sneaker_list.remove(sneaker)
            score += 1

    for sneaker in sneaker_list:
        if sneaker[0] <= 0:
            return True

# Funzione principale
def main():
    global score, sneaker_speed

    st.title("Girl's Catching Game")

    st.write("Use the arrow keys to move the girl and catch the sneakers!")

    # Avvio del gioco
    if st.button("Start Game"):
        game_over = False
        score = 0
        sneaker_speed = 5
        sneaker_list.clear()

        while not game_over:
            move_sneakers()

            if np.random.rand() < 0.03:
                spawn_sneaker()

            game_over = check_collisions()

            st.image(girl_img, width=50)

            for sneaker in sneaker_list:
                st.image(sneaker_img, width=50)

            st.write(f"Score: {score}")

            st.write("")

if __name__ == "__main__":
    main()

