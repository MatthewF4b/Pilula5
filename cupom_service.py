from models.cupom import Cupom


def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    codigo_cupom = codigo_cupom.upper()

    cupom10 = Cupom("CUPOM10", 0.10, 0)
    cupom25 = Cupom("CUPOM25", 0.25, 100)
    descontovip = Cupom("DESCONTOVIP", 0.35, 500)

    lista_cupons = [cupom10, cupom25, descontovip]

    for cupom in lista_cupons:
        if codigo_cupom == cupom.codigo:
            if valor_compra > cupom.valor_minimo:
                return cupom.desconto

            if cupom.codigo == "CUPOM10":
                return cupom.desconto

    return 0.0
