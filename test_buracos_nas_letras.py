# Este problema foi utilizado em 157 Dojo(s).
# Se você pensar em um papel como um plano e uma letra como uma marcação neste plano, 
# então estas letras dividem o plano em regiões. 
# Por exemplo, as letras A, D e O dividem o plano em 2 pois possuem um espaço 
# confinado em seu desenho, ou um “buraco”. 
# Outras letras como B possuem 2 buracos e letras como C e E não possuem buracos.
# Deste modo podemos considerar que o número de buracos em um texto é 
# igual a soma dos buracos nas palavras dele.
# A sua tarefa é, dado um texto qualquer, encontre a quantidade de buracos nele.

# ANDREYEV
# ANDRE
# EDGAR
# GUILHERME
# LUCAS

# lista = {'a' : 1,'e' : 1,'i' : 0, 'o' : 1, 'u' : 0}
import pytest

lista = {
    'a' : 1, 'A' : 1,
    'b' : 1, 'B' : 2,
    'd' : 1, 'D' : 1,
    'e' : 1,
    'g' : 2,
    'o' : 1, 'O' : 1,
    'p' : 1, 'P' : 1,
    'q' : 1, 'Q' : 1,
    'R' : 1,
}


def conta_buraco(letra: str) -> int :
    try:
        return lista[letra]
    except: 
        return 0 

def conta_buraco_frase(frase: str) -> int :
    contador = 0
    for letra in frase:
        contador += conta_buraco(letra)

    return contador

  
       
@pytest.mark.parametrize("letra",["a", "A", "e", "o", "O"])
def test_vogais_um_buraco(letra) -> None:
     assert conta_buraco(letra) == 1

@pytest.mark.parametrize("letra", [ "E", "i", "I", "u", "U",])
def test_vogais_sem_buraco(letra) -> None:
     assert conta_buraco(letra) == 0

@pytest.mark.parametrize("letra", [ "b", "d", "D", "p", "P", "q", "Q", "R"])
def test_consoantes_com_um_buraco(letra) -> None:
    assert conta_buraco(letra) == 1

@pytest.mark.parametrize("letra", [ "B", "g"])
def test_consoantes_com_dois_buracos(letra) -> None:
    assert conta_buraco(letra) == 2

@pytest.mark.parametrize("letra", [ "c", "C", "f", "F", "G", "h", "H", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "r", "s", "S", "t", "T"
, "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"])
def test_consoantes_sem_buracos(letra) -> None:
    assert conta_buraco(letra) == 0

def test_deve_contar_buracos_em_uma_frase() -> None:
    assert conta_buraco_frase("CFGhjkv yY,z!") == 0
    