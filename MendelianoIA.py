
import random


TAXA_MUTACAO = 0.02 
VALOR_MINIMO = 0
VALOR_MAXIMO = 255


# ============================================================
# GERAÇÃO DOS PROGENITORES
# ============================================================

def gera_vida():
    """
    Gera um indivíduo com três genes:
    vermelho (R), verde (G) e azul (B).
    """

    return tuple(
        random.randint(VALOR_MINIMO, VALOR_MAXIMO)
        for _ in range(3)
    )


# ============================================================
# VERIFICAÇÃO DE GENES LETAIS
# ============================================================

def gene_letal(genotipo):
    """
    O indivíduo possui um gene letal se algum dos
    valores RGB estiver fora do intervalo de 0 a 255.

    Retorna True se for letal.
    """

    r, g, b = genotipo

    # Verifica se algum gene está fora do intervalo RGB
    if not all(VALOR_MINIMO <= gene <= VALOR_MAXIMO
               for gene in genotipo):

        return True

    return False


# ============================================================
# MUTAÇÃO GENÉTICA
# ============================================================

def mutacao(gene):
    """
    Aplica uma mutação ao gene com determinada probabilidade.

    A mutação pode gerar valores fora do intervalo RGB,
    que serão considerados letais.
    """

    if random.random() < TAXA_MUTACAO:

        novo_gene = random.randint(-100, 1000)

        return novo_gene

    return gene


# ============================================================
# REPRODUÇÃO
# ============================================================

def reproducao(pai, mae):
    """
    Cada canal RGB do descendente herda um valor
    do pai ou da mãe.

    Depois ocorre a possibilidade de mutação.
    """

    filho = []

    for gene_pai, gene_mae in zip(pai, mae):

        # Escolhe aleatoriamente um dos alelos parentais
        alelo = random.choice([
            gene_pai,
            gene_mae
        ])

        # Aplica mutação
        alelo = mutacao(alelo)

        filho.append(alelo)

    return tuple(filho)


# ============================================================
# SIMULAÇÃO DE VIDA
# ============================================================

def simular_vida(pai, mae):

    filho = reproducao(pai, mae)

    # Verifica se o descendente possui gene letal
    if gene_letal(filho):

        return {
            "genotipo": filho,
            "sobrevive": False,
            "motivo": "Gene fora do intervalo RGB (0-255)"
        }

    return {
        "genotipo": filho,
        "sobrevive": True,
        "motivo": "Descendente viável"
    }


# ============================================================
# EXECUÇÃO DO SIMULADOR
# ============================================================

pai = gera_vida()
mae = gera_vida()

resultado = simular_vida(pai, mae)

filho = resultado["genotipo"]

print("=" * 50)
print("       SIMULADOR DE HERANÇA GENÉTICA")
print("=" * 50)

print(f"\nPai:         {pai}")
print(f"Mãe:         {mae}")
print(f"Descendente: {filho}")

print("\nResultado da reprodução:")

if resultado["sobrevive"]:

    print("STATUS: DESCENDENTE VIÁVEL")

else:

    print("STATUS: DESCENDENTE LETAL")

print(f"Motivo: {resultado['motivo']}")

print("\n" + "=" * 50)
