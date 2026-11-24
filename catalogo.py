from musica import Musica
import musica

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favoritos = []

    @staticmethod
    def _normalizar(texto):
        return texto.strip().lower()

    def verificar_duplicidade(self, musica):
        if not isinstance(musica, Musica):
            raise TypeError("É necessário informar um objeto da classe Musica.")

        for cadastrada in self.musicas:
            if (self._normalizar(cadastrada.nome) == self._normalizar(musica.nome) and
                self._normalizar(cadastrada.cantor) == self._normalizar(musica.cantor) and
                self._normalizar(cadastrada.genero) == self._normalizar(musica.genero)and
                cadastrada.duracao == musica.duracao and cadastrada.ano == musica.ano):
                return True
        return False

    def adicionar_musica(self, musica):
            # Validação
            if not isinstance(musica, Musica):
                raise TypeError("É necessário informar um objeto da classe Musica.")
            
            if self.verificar_duplicidade(musica):
                print("A música já está cadastrada no catálogo.")
                return False
            
            self.musicas.append(musica)
            self.reproducoes[musica] = 0 # personalizar da forma que quiser!
            return True

    def remover_musica(self, musica):
        if musica not in self.musica:
            return False
        if self.musica_atual is musica:
            self.musica_atual = None
        
        if musica in self.favoritos:
            self.favoritos.remove(musica)
        
        self.reproducoes.pop(musica, None)
        self.musica.remove(musica)

    def listar_musicas(self):
        for musica in self.musicas:
            print(musica)

    def buscar_nome(self, termo):
        termo = self._normalizar(termo)
        return [ musica for musica in self.musicas
                if termo in self._normalizar(musica.nome)]

    def buscar_cantor(self, termo):
        termo = self._normalizar(termo)
        return [ musica for musica in self.musicas
                if termo in self._normalizar(musica.cantor)]

    def buscar_genero(self, termo):
        termo = self._normalizar(termo)
        return [ musica for musica in self.musicas
                if termo in self._normalizar(musica.genero)]
    
    def buscar_duracao(self, min_min, min_max):

        segundos_min = min_min * 60
        segundos_max = min_max * 60
        
        return [ musica for musica in self.musicas
                if segundos_min <= musica.duracao <= segundos_max]

    def buscar_ano(self, ano):
        return [musica for musica in self.musicas if musica.ano == ano]