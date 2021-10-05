class Dominos:
	# Simula um jogo de dominó
  def __init__(self):
  	# Inicializa um novo jogo
    ...
  def compra(self):  # retira uma peca nao sorteada do estoque, e o retorna  -- LEVANTA A EXCECAO ValueError se acabar as pecas
# Retira uma peça ainda não sorteada do estoque e a retorna. Levanta a exceção ValueError caso não existam mais peças
    ...
    def coloca(self,peca,extremidade):  #A PECA E SEMPRE UMA TUPLA
# Dada uma peça (tupla da forma a,b), e uma extremidade (0 ou 1),adiciona a peça ao jogo estendendo a extremidade dada. Retorna True se a peça foi colocada com sucesso ou False caso contrário
      ...
    def imprime(self):
# Imprime o jogo até o momento. A impressão tem que ser na forma de uma 'escadinha', isto é, as peças colocadas na mesa se alternam na orientação horizontal e vertical. O leiaute entre uma jogada e a próxima não pode mudar!


# SO TEM 1 JOGADOR
# VAI COMPRANDO PECA E COLOCABNDO
# SE A PECA NAO COUBER, VC JOGA ELA FORA
# SEMPRE TENTA COLOCAR NA POSICAO 0 E DPS NA POSICAO 1

# ESTREMIDADES SAO NA DIREITA OU EM CIMA OU EM BAIXO
# PODE INVERTER A PECA

# INPUT DE QUAIS PECAS VAO TER
# AS COMPRAS SEGUEM A ORDEM DESSA LISTA