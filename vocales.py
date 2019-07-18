
regla = {
    'a': 'e', 'e':'i', 'i': 'o', 'o': 'u', 'u': 'a',
    'A': 'E', 'E':'I', 'I': 'O', 'O': 'U', 'U': 'A'
}

def checa_vocales(cad):
    cont = 0
    nueva_cad = ''
    for c in cad:
        if c in regla:
            nueva_cad += regla[c]
            cont += 1
        else:
            nueva_cad += c
        
    return {'cont': cont, 'res': nueva_cad}
    
    
if __name__ == "__main__":
    print('-- Vocales --')
    cad = input('Introduce cadena...')
    datos = checa_vocales(cad)
    
    print('Numero de vocales', datos['cont'])
    print('Cadena resultante', datos['res'])
        
    