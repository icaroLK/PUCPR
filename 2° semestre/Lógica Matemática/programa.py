# fazer a tabela verdade
#   →   ↔   ∧   ∨

expressao = input('Insira a expressão lógica: ').strip().replace('->', '→').replace('<->', '↔').replace('^', '∧').replace('v', '∨').replace('~', '¬').replace(' ','')

alf = 'abcdefghijklmnopqrstuvwxyz'
qtd = [0] * 26

if alf in expressao:
    print('tem variavel')

print('Expressão: {}'.format(expressao))
print(qtd)