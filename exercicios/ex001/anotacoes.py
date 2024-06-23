# EXEMPLOS DA AULA 1

disciplina = 'Logica de programação'
nota = 8.5
###########################################################
# PARA DESCOBRIR TAMANHO DAS CADEIAS DE CARACTERES (length)

tamanho = len(disciplina)

print(tamanho)

###########################################################

# COMPOSIÇÕES COM MARCADORES DE POSIÇÃO

#print('Disciplina:', disciplina , 'com nota de:', nota)

#print('A nota que você tirou foi de: %f, Parabéns' % nota)

#print('A nota que você tirou foi de: %.2f, Parabéns' % nota)

#print('A nota que você tirou foi de: %i Parabéns' % nota)

#print('A nota que você tirou foi de: %s, Parabéns' % nota)

s1 = 'A nota que você tirou foi de: %s, Parabéns' % nota

print(s1)

###########################################################

# COMPOSIÇÃO MODERNAS

s2 = 'A nota que você tioru foi de: {}, na disciplina de {}' .format(nota, disciplina)

print(s2)

###########################################################

# COMPOSIÇÃO COM f-strings

s3 = f'A nota que você tirou foi de: {nota}, na disciplina de {disciplina}'

print(s3)