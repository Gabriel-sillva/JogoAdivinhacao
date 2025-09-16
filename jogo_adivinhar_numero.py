import random


# O QUE É POO? 

# A Programação Orientada a Objetos (POO) é uma forma de organizar seu código baseando-se em objetos do mundo real.

# Você usa:

# Classes → são moldes (ex: molde para um jogo).

# Objetos → são instâncias da classe (ex: um jogo real que está rodando).

# Atributos → são dados de um objeto (ex: número secreto).

# Métodos → são ações que o objeto pode executar (ex: verificar palpite).



class JogoAdivinhacao:
    #Aqui DEFINE UMA CLASSE, que ser como MOLDE para criar o "Objeto jogo".
    # A classe agrupa dadps e COMPORTAMENTOS relacionado ao jogo de adivinhação.
    
    #Analogia real:Pense numa "fábrica de jogos". Cada vez que você quiser jogar, você pede para a fábrica montar um novo jogo (um novo objeto da classe).

    def __init__(self, minimo=1, maximo=100, max_tentativas=10): 
        self.minimo = minimo
        self.maximo = maximo
        self.max_tentativas = max_tentativas
        self.numero_secreto = random.randint(self.minimo, self.maximo)
        self.tentativas = 0
    
    # Esses são os dados armazenados dentro do objeto.
    # Você pode imaginar isso como uma "ficha do jogo" com essas informações guardadas.

    # __init__ É o MÉTODO CONSTRUTOR, chamdo automaticamente quando vocé cria um novo objeto da classe.
    # self Representa O PROPIO OBJETO, e permite acessar os atributos e métodos dele.
    # sel.mumero_secreto e selft.tentativas são ATRIBUTOS DO OBJETOS, usados para manter o estado do jogo

    def obter_palpite(self): # esse método é responsável por pedir ao jogador que digite um nummero, Verificar se o número esta dentro do intervalo.
        while True:
            print("###### Adivinha o número ######")
            palpite = int(input(f"Tentatativa {self.tentativas + 1}: Digite um número entre {self.minimo} e {self.maximo}: "))
            
            if self.minimo <= palpite <= self.maximo:
                return palpite
            
            else:
                print(f"Digite um Número entre {self.minimo} e {self.maximo}.")


    def verificar_palpite(self, palpite): 

        #Compara o palpite do jogador com o número secreto.
        
        #Retorna: "acertou" se for igual, "maior" se o numero for maior e "menor" se for menor

        if palpite == self.numero_secreto:
            return "acertou"
        
        elif palpite < self.numero_secreto:
            return "maior"
        
        else:
            return "menor"
     

    def jogar(self):
        print("\nBem-vindo ao Jogo de Adivinhação!")
        print(f"Tente adivinhar o número entre {self.minimo} e {self.maximo}.")
        print(f"Você tem {self.max_tentativas} tentativas.\n")

        while self.tentativas < self.max_tentativas:
            palpite = self.obter_palpite()
            self.tentativas += 1

            resultado = self.verificar_palpite(palpite)
            
            if resultado == "acertou":
                print(f"\n Parabéns ! Vocé acertou o numero {self.numero_secreto} em {self.tentativas} tentativas.")
                break
            
            elif resultado == "maior":
                print(f"O numero é MAIOR.\n")
            
            else:
                print("O numero secreto é MENOR.\n")

            
            if self.tentativas == self.max_tentativas and resultado != "acertou":
                print(f"\n Fim de jogo! O número secreto era {self.numero_secreto}.")

    
# Executar o jogo
if __name__ == "__main__":
    jogo = JogoAdivinhacao()
    jogo.jogar()