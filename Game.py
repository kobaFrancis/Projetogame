import pygame # Importa a biblioteca Pygame
import random # Importa a biblioteca random (para gerar números aleatórios)

# Cria uma nova obstaculo
def criaObstaculos():
    # Cria um dicionário com as informações da obstaculo
  
    velocidade = random.randint(7, 10) # Velocidade aleatória
    tipo = random.choice(['energia', 'arbusto', 'rocha', 'arvore']) # Tipo aleatório
    tamanho = random.randint(5, 20) # Tamanho aleatório
    vidas = random.randint(1, 10) # Vidas aleatórias

    # Retorna o dicionário com as informações da obstaculo para ser adicionado na lista
    return {
        "posicao": [1300, random.randint(450, 550)],
        "velocidade": velocidade,
        "cor": cor,
        "tamanho": tamanho,
        "vidas": vidas,
        "direcao": pygame.Vector2(1, 1)
    }

def criaPersonagem():
    # Cria um dicionário com as informações do personagem
    imagem = pygame.image.load("Personagem/Samurai/Acoes/Jump1.png")

    velocidadepersonagem = random.randint(7, 10) # Velocidade aleatória
    tipo = random.choice(['samuray', 'figther']) # Tipo aleatório
    tamanhopersonagem = 300 # Tamanho aleatório
    corpersonagem = (0,0,0)
   # vidas = random.randint(1, 10) # Vidas aleatórias

    # Retorna o dicionário com as informações da obstaculo para ser adicionado na lista
    return {
        "velocidadepersonagem": velocidadepersonagem,
        "corpersonagem": corpersonagem,
        "tamanhopersonagem": tamanhopersonagem,
        "retangulo": imagem.get_rect(center=(300, 600)),
        "imagem": imagem
        #"vidas": vidas,
        #"direcao": pygame.Vector2(1, 1)
    }

# Inicializa o Pygame
pygame.init()
# Configurações da mapa
tamanho = (1300, 650)
# Cria o mapa e define o tamanho
mapa = pygame.display.set_mode(tamanho)
# Define o título da mapa
pygame.display.set_caption("SAMURAY RUNNER")

# Criar um relogio para controlar os FPS
relogio = pygame.time.Clock()

# Parametros dos obstaculos
cor = (255, 0, 0)
posicao = [150, 60]
raio = 50
velocidade = 0
cor_tela = (255, 255, 255)

corpersonagem = (0,0,0)
posicaopersonagem = [300,300]
velocidadepersonagem = 0
tamanhopersonagem = 50

# Lista de bolas que vão ser desenhadas e movimentadas
listaObstaculos= []

# Evento para o tempo
EventonovoObstaculo = pygame.USEREVENT + 1

# Cria o evento a cada 10 segundos
pygame.time.set_timer(EventonovoObstaculo, 500)

personagem = criaPersonagem()
gravidade = 0


##################### Importar as imagens para o jogo #######################




#personagem pulando
listaPersonagempulando = []
for index in range(1, 13):
    imagem = pygame.image.load(f"Personagem/Samurai/Acoes/Jump{index}.png")
    imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
    listaPersonagempulando.append(imagem)

#personagem andando 
listaPersonagemandando = []
for index in range(1, 9):
    imagem = pygame.image.load(f"Personagem/Samurai/Acoes/Walk{index}.png")
    imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
    listaPersonagempulando.append(imagem)

#personagem correndo
listaPersonagemcorrendo = []
for index in range(1, 9):
    imagem = pygame.image.load(f"Personagem/Samurai/Acoes/Run{index}.png")
    imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
    listaPersonagempulando.append(imagem)

# LOOP PRINCIPAL
while True:
    # Pega os eventos que estão acontecendo
    for evento in pygame.event.get():
        if evento.type == EventonovoObstaculo:
            # Adiciona umm novo objeto na lista de objetos
            listaObstaculos.append(criaObstaculos())

        # Se o evento for de fechar o mapa
        if evento.type == pygame.QUIT:
            pygame.quit() # Fecha o Pygame
            exit() # Fecha o programa

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            gravidade = -10

            #########################################

    # Pinta o mapa
    mapa.fill(cor_tela)

    listapersonagem = []
    corpersonagem = (0,0,0)
    posicaopersonagem = [300,300]
    velocidadepersonagem = 0
    tamanhopersonagem = 50

    gravidade += 1

    # #Personagem criado na parte esquerda do mapa
    # personagem in listapersonagem:

    #     personagens = pygame.draw.circle(
    #     mapa,
    #     personagem["corpersonagem"],  
    #     personagem["posicaopersonagem"],
    #     personagem["tamanhopersonagem"]
    #     )

    personagem["retangulo"].y += gravidade

    if personagem["retangulo"].y >= 450:
        personagem["retangulo"].y = 450

    mapa.blit(personagem["imagem"], personagem["retangulo"])

    # Processa a lista de obstáculos, desenhando e movendo
    for obstaculo in listaObstaculos:
        # Desenhar o obstaculo no mapa

        obstaculos = pygame.draw.circle(
            mapa, 
            obstaculo["cor"], 
            obstaculo["posicao"],
            obstaculo["tamanho"]
        )
        
        # Movimenta o obstaculo com a velocidade e direção
        obstaculo["posicao"][0] -= obstaculo["velocidade"] * obstaculo["direcao"].x
       

        # Verifica se o obstaculo bateu no eixo X
        if obstaculo["posicao"][0] <=0:
            # Reposiciona o obstaculo para não sair da mapa
            obstaculo["posicao"][0] = tamanho[0] - obstaculo["tamanho"]
          
        
       

    #########################################
    # Atualiza a mapa para exibir o que foi desenhado
    pygame.display.update()

    # Controla a quantidade de FPS
    relogio.tick(60)