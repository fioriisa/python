def right_justify(palavra, tamanhopalavra):
    espaço = ' '
    resultado =  espaço * (70 - tamanhopalavra)
    return espaço + palavra


palavra = str(input("digite uma palavra"))
tamanhopalavra = len(palavra)

justificado = right_justify(palavra, tamanhopalavra)

print(justificado)



