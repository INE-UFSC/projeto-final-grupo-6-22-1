import pygame as pg
import os

# Pré-carregamento de imagens
image_cache = {}

def get_image(folder, key):
    """
    Retorna imagem do cache, se não está carregada, carrega
    """
    if not key in image_cache:
        image_cache[key] = pg.image.load(os.path.join("images", folder, key)).convert_alpha()

    return image_cache[key]
