from utils import somma
lista = [1, 2, 3]

def show_max(lista:list) -> float:
    print(f"Massimo in lista: {max(lista)}")

def show_min(lista: list) -> float:
    print(f"Minimo in lista: {min(lista)}")

print(f"Lunghezza della lista: {len(lista)}")
show_min(lista)

a = 1
b = 10
print(somma(a, b))
