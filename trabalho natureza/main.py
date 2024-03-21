#joao pedro frigeri
class Funcao:
    def _init_(self, expressao):
        self.expressao = expressao

    def avaliar(self, x):
        return eval(self.expressao.replace('x', str(x)))


def composicao(g, f, x):
    return g.avaliar(f.avaliar(x))

expressao_f = input("Digite a expressão de f(x): ")
expressao_g = input("Digite a expressão de g(x): ")

f = Funcao(expressao_f)
g = Funcao(expressao_g)

gf = lambda x: composicao(g, f, x)
gg = lambda x: composicao(g, g, x)
ff = lambda x: composicao(f, f, x)
fg = lambda x: composicao(f, g, x)

print("(g ° f)(x) =", gf)
print("(g ° g)(x) =", gg)
print("(f ° f)(x) =", ff)
print("(f ° g)(x) =", fg)