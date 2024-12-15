import pygame

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Panorama Looping")

# Cores
BLACK = (0, 0, 0)

# Carregar a imagem
image_path = "panorama.png"  # Substitua pelo caminho do seu arquivo PNG
panorama = pygame.image.load(image_path).convert_alpha()
image_width = panorama.get_width()
image_height = panorama.get_height()

# Verificar se a imagem tem o tamanho esperado
#if image_width != 6000 or image_height != 600:
#    raise ValueError("A imagem deve ter exatamente 6000px de largura por 600px de altura.")

# Posição inicial do deslocamento
offset = 0
scroll_speed = 5  # Velocidade do movimento

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obter teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_UP]:
        offset -= scroll_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_DOWN]:
        offset += scroll_speed

    # Manter o offset no intervalo correto para o looping
    offset %= image_width

    # Preencher o fundo
    screen.fill(BLACK)

    # Desenhar a imagem principal e a parte "reiniciada" do loop
    screen.blit(panorama, (-offset, 0))
    if offset > 0:
        screen.blit(panorama, (image_width - offset, 0))
    else:
        screen.blit(panorama, (-offset - image_width, 0))

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()

