class Arquivo:
    @staticmethod
    def gera_arquivo(usuario,jogo,dificuldade,erroIngrediente,erroMovimento,tempo):
        texto = "Nome:" + usuario + " \tJogo:" + jogo + "\tDificuldade: " + str(dificuldade) + "\tErro Movimento: " + str(erroMovimento) + "\tErro Ingrediente: " + str(erroIngrediente) + "\tTempo: " + str(tempo) + "\n"
        f = open(usuario+".txt", 'a')
        f.write(texto)
        f.close()

   





