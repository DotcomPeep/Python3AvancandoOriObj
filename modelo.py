class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} - ano: {self.ano} minutos - Likes: {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - ano: {self.ano} - duração: {self.duracao} minutos - Likes: {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - ano: {self.ano} - temporadas: {self.temporadas} temporadas - Likes: {self._likes}'

def pula_linha():
    print("\n")

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


Helsing = Filme('Van Helsing - O caçador de monstros', 2004, 131)
Helsing.dar_like()
Helsing.dar_like()
Helsing.dar_like()
Helsing.dar_like()
Helsing.dar_like()

tmep = Filme('Todo mundo em pânico', 2000, 88)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

himym = Serie('How I met your mother', 2005, 9)
himym.dar_like()
himym.dar_like()
himym.dar_like()
himym.dar_like()
himym.dar_like()

b99 = Serie('Brooklyn Nine-Nine', 2013, 8)
b99.dar_like()
b99.dar_like()
b99.dar_like()


filme_e_series = [Helsing, tmep, himym, b99]
playlist_fim_de_semana = Playlist('Fim de semana', filme_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

#após __getitem__ --> pode-se percorrer pela lista
#print(playlist_fim_de_semana[0]) Van Helsing

#print(b99 in playlist_fim_de_semana) verificando se b99 está dentro da lista após adicionar 
# a função __getitem__

for programa in playlist_fim_de_semana:
    print(programa)

#for programa in playlist_fim_de_semana.listagem:
#    print(programa)

#print(f'tá ou não tá? {himym in playlist_fim_de_semana}')