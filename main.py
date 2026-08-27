import time
import json
try:
    with open("disciplinas.json", "r") as arquivo:
        disciplinas = json.load(arquivo)
except FileNotFoundError:
    disciplinas = {}

def salva_disciplinas():
    with open("disciplinas.json", "w") as arquivo:
        json.dump(disciplinas, arquivo, ensure_ascii=False)

def adicionar_disciplinas():
    nova_disciplina = input('Disciplina a ser adicionada: ')    
    if nova_disciplina in disciplinas:
        print('\033[91mEssa disciplina já existe! Tente novamente!\033[0m')
    else:
        disciplinas[nova_disciplina] = []
        salva_disciplinas()
        print(f'\033[92mDisciplina {nova_disciplina} foi adicionada com sucesso!! ✅\033[0m')  

def remover_disciplina(numero_remover):
    indice_remover = verificacao_valor(numero_remover, lista_disciplinas)
    if indice_remover != None:
        removida = lista_disciplinas[indice_remover]
        print(f"Disciplina '{removida}' removida com sucesso!")
        del disciplinas[removida]
        salva_disciplinas()
    else:
        print('\033[91mOpção inválida. Tente novamente!\033[0m')

def verificacao_valor(valor, condicao):
    if valor.isdigit():
        valor = int(valor)
        if valor <= len(condicao) and valor > 0:
            indice = valor - 1
            return indice
        else:
            print('\033[91mOpção inválida. Tente novamente!\033[0m')


def ver_disciplina():
    lista_disciplinas = [] 
    cont = 1
    for chave in disciplinas:
        quantidade_tarefas = len(disciplinas[chave])
        lista_disciplinas.append(chave)
        print(f'{cont} - {chave} ({quantidade_tarefas} tarefas)')
        cont += 1
    return lista_disciplinas

def tela_disciplina(escolhida):
    while True:
        print(f'-=-=-=-=- {escolhida.upper()} -=-=-=-=-=-')
        i = 1
        for tarefa in disciplinas[escolhida]:
            if tarefa["feita"] == True:
                marca = '[X]'
            else:
                marca = '[ ]'
            print(f'{i} - {marca} {tarefa["nome"]}')
            i += 1
        print('V - Voltar')
        print('A - Adicionar Tarefa')
        print('M - Marcar/Desmarcar Tarefa')
        print('R - Remover Tarefa')
        escolha_tela = input('Escolha: ').upper()
        if escolha_tela == 'A':
            nome_tarefa = input('Tarefa a ser adicionada: ')
            nova_tarefa = {"nome": nome_tarefa, "feita": False}
            disciplinas[escolhida].append(nova_tarefa)
            salva_disciplinas()
            print(f'\033[92mTarefa "{nome_tarefa}" adicionada com sucesso!! ✅\033[0m')
        elif escolha_tela == 'V':
            break
        elif escolha_tela == 'R':
            tarefas_disciplina = disciplinas[escolhida]
            numero_remover_tarefa= input('Qual o número da tarefa que quer remover? ')
            indice_remover = verificacao_valor(numero_remover_tarefa, tarefas_disciplina)
            if indice_remover != None:
                tarefas_disciplina.pop(indice_remover)
                print(f'Tarefa removida com sucesso')
                salva_disciplinas()
            else:
                print('\033[91mOpção inválida. Tente novamente!\033[0m')
                
        elif escolha_tela == 'M':
            numero_marcar = input('Qual o número da tarefa que você deseja marcar/desmarcar? ')
            indice_marcar = verificacao_valor(numero_marcar, disciplinas[escolhida])
            if indice_marcar != None:
                disciplinas[escolhida][indice_marcar]["feita"] = not disciplinas[escolhida][indice_marcar]["feita"]
                salva_disciplinas()
            else:
                print('\033[91mOpção inválida. Tente novamente!\033[0m')
        else:
            print('\033[91mOpção inválida. Tente novamente!\033[0m')




print("=" * 30)
print("Bem-vindo(a) ao seu Organizador de Estudos!")
print("=" * 30)
time.sleep(1)
while True:
    print('01 - Ver disciplinas')
    print('02 - Adicionar disciplina')
    print('03 - Sair')
    escolha = input('Escolha: ')
    if escolha == '03':
        print("Até mais! Bons estudos! 📚")
        break 
    elif escolha == '01':
        lista_disciplinas = ver_disciplina()
        print('R - Remover disciplina')
        print('V - Voltar')
        escolha_disciplina= input('Escolha: ')
        if escolha_disciplina in 'Rr':
            numero_remover = input('Qual o número da disciplina que quer remover? ')
            remover_disciplina(numero_remover)
        elif escolha_disciplina.isdigit():
            indice_disciplina = verificacao_valor(escolha_disciplina, lista_disciplinas)
            if indice_disciplina != None:
                escolhida = lista_disciplinas[indice_disciplina]
                tela_disciplina(escolhida)
            else:
                print('\033[91mOpção inválida. Tente novamente!\033[0m')

        elif escolha_disciplina in 'Vv':
            pass
        else:
            print('\033[91mOpção inválida. Tente novamente!\033[0m')
    elif escolha == '02':
        adicionar_disciplinas()       
    else:
       print('\033[91mOpção inválida. Tente novamente!\033[0m')


