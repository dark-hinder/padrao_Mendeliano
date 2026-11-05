
import pygame
import Mendeliano
import random
import io
from contextlib import redirect_stdout


# ============================================================
# CONFIGURAÇÕES
# ============================================================

pygame.init()

LARGURA = 900
ALTURA = 700

FPS = 60

# Paleta de cores
FUNDO = (12, 18, 30)
PAINEL = (20, 30, 48)
CIANO = (0, 220, 255)
BRANCO = (235, 245, 255)
CINZA = (150, 170, 190)
VERDE = (50, 230, 140)
VERMELHO = (255, 80, 100)

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulador Genético")

clock = pygame.time.Clock()


# ============================================================
# FONTES
# ============================================================

fonte_titulo = pygame.font.SysFont("consolas", 34, bold=True)
fonte_subtitulo = pygame.font.SysFont("consolas", 18)
fonte_texto = pygame.font.SysFont("consolas", 20)
fonte_pequena = pygame.font.SysFont("consolas", 16)
fonte_genetica = pygame.font.SysFont("consolas", 17)


# ============================================================
# ORGANISMO
# ============================================================

class Organismo:

    def __init__(self, x, y, rgb):

        self.x = x
        self.y = y

        self.cor = rgb

        self.largura = 50
        self.altura = 50

    def desenhar(self, janela):

        pygame.draw.rect(
            janela,
            self.cor,
            (self.x, self.y, self.largura, self.altura),
            border_radius=8
        )

        pygame.draw.rect(
            janela,
            CIANO,
            (self.x, self.y, self.largura, self.altura),
            2,
            border_radius=8
        )


# ============================================================
# GERAÇÃO DO DESCENDENTE
# ============================================================

def CreateOrg():

    # Obtém a tupla genética do Mendeliano
    tuplaFilho = Mendeliano.retornarValor()

    # Converte os genes para valores RGB
    rgb = tuple(int(gene) for gene in tuplaFilho)

    # Verifica se o descendente possui genes válidos
    viavel = all(0 <= gene <= 255 for gene in rgb)

    # Captura a saída de MostrarGenetica
    # para exibir a genética dentro da interface
    saida = io.StringIO()

    with redirect_stdout(saida):

        Mendeliano.MostrarGenetica(
            tuplaFilho,
            "Filho"
        )

    geneticaFilho = saida.getvalue()

    # Posição fixa do organismo
    posX = 170
    posY = 300

    organismo = None

    if viavel:

        organismo = Organismo(
            posX,
            posY,
            rgb
        )

    return organismo, tuplaFilho, geneticaFilho, viavel


# ============================================================
# ELEMENTOS VISUAIS
# ============================================================

def desenhar_painel(x, y, largura, altura):

    pygame.draw.rect(
        janela,
        PAINEL,
        (x, y, largura, altura),
        border_radius=15
    )

    pygame.draw.rect(
        janela,
        CIANO,
        (x, y, largura, altura),
        2,
        border_radius=15
    )


def texto(conteudo, fonte, cor, x, y):

    superficie = fonte.render(
        str(conteudo),
        True,
        cor
    )

    janela.blit(
        superficie,
        (x, y)
    )




# ============================================================
# INTERFACE
# ============================================================

def desenhar_interface(
    organismo,
    tuplaFilho,
    geneticaFilho,
    viavel
):

    janela.fill(FUNDO)

    # --------------------------------------------------------
    # CABEÇALHO
    # --------------------------------------------------------

    texto(
        "Painel",
        fonte_titulo,
        CIANO,
        35,
        25
    )

    texto(
        "SIMULADOR DE HERANÇA GENÉTICA",
        fonte_subtitulo,
        CINZA,
        38,
        70
    )

    pygame.draw.line(
        janela,
        CIANO,
        (35, 105),
        (865, 105),
        2
    )

    # --------------------------------------------------------
    # PAINEL DO ORGANISMO
    # --------------------------------------------------------

    desenhar_painel(
        35,
        130,
        350,
        330
    )

    texto(
        "DESCENDENTE",
        fonte_texto,
        CIANO,
        55,
        150
    )

    if viavel and organismo is not None:

        organismo.desenhar(janela)

        texto(
            "Organismo viável",
            fonte_pequena,
            VERDE,
            115,
            365
        )

    else:

        texto(
            "DESCENDENTE LETAL",
            fonte_texto,
            VERMELHO,
            90,
            270
        )

        texto(
            "Gene fora do intervalo RGB",
            fonte_pequena,
            CINZA,
            65,
            310
        )

    # --------------------------------------------------------
    # PAINEL GENÉTICO
    # --------------------------------------------------------

    desenhar_painel(
        405,
        130,
        460,
        330
    )

    texto(
        "GENÉTICA DO FILHO",
        fonte_texto,
        CIANO,
        425,
        150
    )

    # Exibe a saída da função MostrarGenetica
    linhas = geneticaFilho.strip().splitlines()

    y = 195

    for linha in linhas:

        if linha.strip():

            texto(
                linha,
                fonte_genetica,
                BRANCO,
                425,
                y
            )

            y += 28

    # --------------------------------------------------------
    # PAINEL DE INFORMAÇÕES
    # --------------------------------------------------------

    desenhar_painel(
        35,
        480,
        830,
        125
    )

    texto(
        "INFORMAÇÕES",
        fonte_texto,
        CIANO,
        55,
        500
    )

    texto(
        f"Genótipo: {tuplaFilho}",
        fonte_pequena,
        BRANCO,
        55,
        540
    )

    texto(
        "Posição: (350, 280)",
        fonte_pequena,
        BRANCO,
        55,
        570
    )

    if viavel:

        texto(
            f"RGB: {tuple(int(gene) for gene in tuplaFilho)}",
            fonte_pequena,
            BRANCO,
            450,
            540
        )

        texto(
            "STATUS: VIÁVEL",
            fonte_pequena,
            VERDE,
            450,
            570
        )

    else:

        texto(
            "STATUS: LETAL",
            fonte_pequena,
            VERMELHO,
            450,
            570
        )



# ============================================================
# EXECUÇÃO
# ============================================================

organismo, tuplaFilho, geneticaFilho, viavel = CreateOrg()

executando = True

while executando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            executando = False

        
            
            

    desenhar_interface(
        organismo,
        tuplaFilho,
        geneticaFilho,
        viavel
    )

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
