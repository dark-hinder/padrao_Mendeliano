import random
codons = {
    "Phe": ("UUU", "UUC"),
    "Leu": ("UUA", "UUG", "CUU", "CUC", "CUA", "CUG"),
    "Ile": ("AUU", "AUC", "AUA"),
    "Met": ("AUG"),
    "Val": ("GUU", "GUC", "GUA", "GUG"),
    "Ser": ("UCU", "UCC", "UCA", "UCG", "AGU", "AGC"),
    "Pro": ("CCU", "CCC", "CCA", "CCG"),
    "Thr": ("ACU", "ACC", "ACA", "ACG"),
    "Ala": ("GCU", "GCC", "GCA", "GCG"),
    "Tyr": ("UAU", "UAC"),
    "His": ("CAU", "CAC"),
    "Gln": ("CAA", "CAG"),
    "Asn": ("AAU", "AAC"),
    "Lys": ("AAA", "AAG"),
    "Asp": ("GAU", "GAC"),
    "Glu": ("GAA", "GAG"),
    "Cys": ("UGU", "UGC"),
    "Trp": ("UGG"),
    "Arg": ("CGU", "CGC", "CGA", "CGG", "AGA", "AGG"),
    "Gly": ("GGU", "GGC", "GGA", "GGG"),
    "Stop": ("UAA", "UAG", "UGA")
}

Inverter = {
    "1": ("Phe", "His"),
    "2": ("Leu", "Gln"),
    "3": ("Ile", "Asn"),
    "0": ("Met", "Trp", "Stop"),
    "4": ("Val", "Lys"),
    "5": ("Ser", "Asp"),
    "6": ("Pro", "Glu"),
    "7": ("Thr", "Cys"),
    "8": ("Ala", "Arg"),
    "9": ("Tyr", "Gly")
}
#Numero em amino
def Conversor(Genes = None):
    x = random.randint(0,1)
    genoma = []
    for gene in Genes:
        seq = []
        for n in str(gene):
            nucletideo = Inverter[n][x]
            seq.append(nucletideo)
        genoma.append(seq)
    return genoma

#Amino em Codons
def DecodificandoAmino(Amino = None):
    genoma = []
    for a in Amino:
        genes = []
        for carater in a:
            opcoes = codons[carater]
            if isinstance(opcoes, str):
                codificado = opcoes
            else:
                x = random.randint(0, len(opcoes) - 1)
                codificado = opcoes[x]
            genes.append(codificado)
        genoma.append(genes)
    return genoma

#Codons em Amino
def codificandoCodons(codons_Recebido):
    genoma = []
    for cod in codons_Recebido:
        genes = []
        for i in cod:
            for chave in codons:
                if i in codons[chave]:   
                    genes.append(chave)
        genoma.append(genes)
    return genoma

#Amino em Numeros
def codificando_inNumeros(proteina):
    genoma = []
    for a in proteina:    
        genes = [] 
        for i in a:
            for chave in Inverter:
                if i in Inverter[chave]:  
                    genes.append(chave)
        genoma.append(genes)
    return genoma  
    

def taxaCG(gene): 
    seq = gene
    gc = seq.count("G") + seq.count("C")
    calculo = gc / len(seq)
    variedadeRandomica = round(random.random(), 1)
    resultado = (calculo + variedadeRandomica)/2 
    return round(resultado,2)
    
        
def aDominancia(m='AAA',f='AAA'):
    def comulo(a):
        for i in codons:
            if a in codons[i]:
                a = i 
        
        for j in Inverter:
            if a in Inverter[j]:
                a = j
        return a
    
    m = comulo(m)
    f = comulo(f)
    
    media = (int(m) + int(f))/2
    media = int(media)
    rand = random.randint(0,1)
    proteina = Inverter[str(media)][rand]  
    quantia = len(codons[proteina])
    rand = random.randint(0,quantia-1)
    aminoacido = codons[proteina][rand]
    return aminoacido
       
def Reproducao(x,y):
    x = Conversor(x)
    y = Conversor(y)
    
    x = DecodificandoAmino(x)
    y = DecodificandoAmino(y)
    genomaFilho = []

    for i in range(3):
        genes = []
        for j in range(3):
            cgX = taxaCG(x[i][j])
            cgY= taxaCG(y[i][j])
            if cgX > cgY:
                morph = Mutacao(x[i][j])
                genes.append(morph)
            elif cgX < cgY:
                morph = Mutacao(y[i][j])
                genes.append(morph)
            else:
               domin = aDominancia(y[i][j],x[i][j])
               ge = Mutacao(domin)
               genes.append(ge)
        genomaFilho.append(genes)
    return genomaFilho
                
    
def Mutacao(genes='ATT'):
    nucleotideos = ['A','T','C','G']
    def _mutacao():  
        taxa = 0.03
        taxaMut = random.random()
        prob = taxa > taxaMut
        return prob
    nova_genes = genes
    mut = _mutacao()
    if mut:
        genesDestruido = random.randint(0, len(genes)-1)
        nova_genes = ''
        for i in range(3):
            if i == genesDestruido:
                number = random.randint(0, len(nucleotideos) - 1)
                nova_genes += nucleotideos[number]
            else:
                
                nova_genes += genes[i]
    
    return nova_genes  
        

def GeraVida():
    r = random.randint(0,255)
    r = str(r).zfill(3)
    g = random.randint(0,255)
    g = str(g).zfill(3)
    b = random.randint(0,255)
    b = str(b).zfill(3)
    cor = (r,g,b)
    return cor



def MostrarGenetica(genotipo, nome):

    proteinas = Conversor(genotipo)

    codons = DecodificandoAmino(proteinas)

    newProt = ' '.join(
        amino for proteina in proteinas
        for amino in proteina
    )

    newCodons = ' '.join(
        codon for lista in codons
        for codon in lista
    )

    print(f'\n--- {nome} ---')
    print(f'Genótipo: {genotipo}')
    print(f'Proteínas: {newProt}')
    print(f'Codons: {newCodons}')



pai = GeraVida()
mae = GeraVida()
filho = Reproducao(pai, mae)



#filho

filho = codificandoCodons(filho)
filho = codificando_inNumeros(filho)

status = {'Filho':True}

listaFilho = []
for num in filho:
    numero = ''
    for i in num:
        numero += i
    listaFilho.append(numero)
tuplaFilho = tuple(listaFilho)


for number in tuplaFilho:
    if int(number) > 255:
        status['Filho'] = False



def retornarValor():
    return tuplaFilho

MostrarGenetica(tuplaFilho, 'Filho')

if __name__ == "__main__":
    MostrarGenetica(pai, 'Pai')
    MostrarGenetica(mae, 'Mãe')
    print(status)