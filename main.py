from services.cupom_service import aplicar_cupom


codigo = input("Digite o código do cupom: ")
valor = float(input("Digite o valor da compra: "))

desconto = aplicar_cupom(codigo, valor)

print(f"Desconto aplicado: {desconto * 100}%")
