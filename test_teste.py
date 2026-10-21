from main import bubble_sort

print("Área de Testes")

def test_lista_Padrao():
    lista = [60,4,0,100,2]
    # quero verificar se no teste vai dar o resultado esperado, 
    # chamar a função "lista" , e depois vou comparar se o resultado é o igual o esperado.
    assert bubble_sort(lista) == [0,2,4,60,100]

def test_lista_Decimal():
    lista = [70.00,90.20,10.15]
    # quero verificar se no teste vai dar o resultado esperado, 
    # chamar a função "lista" , e depois vou comparar se o resultado é o igual o esperado.
    assert bubble_sort(lista) == [10.15,20.10,70.00]

def test_lista_Negativas():
    lista = [-55,-15,0,5,-20]
    # quero verificar se no teste vai dar o resultado esperado, 
    # chamar a função "lista" , e depois vou comparar se o resultado é o igual o esperado.
    assert bubble_sort(lista) == [-55,-20,-15,0,5]
