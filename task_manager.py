import json

ARQUIVO = 'tasks.json'

def carregar_tarefas():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas):
    nome = input('Digite a sua Side Quest: ')
    prazo = input('Prazo (opcional, Ex: DD/MM/YYYY): ')
    nova_tarefa = {
        'descricao': nome,
        'concluida': False,
        'prazo': prazo if prazo else None
    }
    tarefas.append(nova_tarefa)
    print('Tarefa adicionada com sucesso! 👍')
    input('Pressione Enter para voltar ao menu principal...')

def Mostrar_tarefas(tarefas):
    if not tarefas:
        print('Sem tarefas no momento.')
        input('Pressione Enter para voltar ao menu principal...')
        return
    for i, t in enumerate(tarefas, 1):
        status = "✔️" if t["concluida"] else "❌"
        prazo = f"(Prazo: {t['prazo']})" if t['prazo'] else ''
        print(f'{i}. {status} {t["descricao"]} {prazo}')
    input('Pressione Enter para voltar ao menu principal...')

def conclusao_task(tarefas):
    Mostrar_tarefas(tarefas)
    try:
        i = int(input('Escolha o número da tarefa para finalizar: ')) - 1
        if 0 <= i < len(tarefas):
            tarefas[i]['concluida'] = True
            print('Missão concluída! 😁')
        else:
            print('Número de tarefa inválido.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
    input('Pressione Enter para voltar ao menu principal...')

def remover_tarefa(tarefas):
    Mostrar_tarefas(tarefas)
    try:
        i = int(input('Escolha o número da tarefa que deseja remover: ')) - 1
        if 0 <= i < len(tarefas):
            del tarefas[i]
            print('Tarefa removida com sucesso.')
        else:
            print('Número de tarefa inválido.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
    input('Pressione Enter para voltar ao menu principal...') 
