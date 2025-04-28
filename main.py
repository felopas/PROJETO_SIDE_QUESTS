import os
from task_manager import carregar_tarefas, salvar_tarefas, adicionar_tarefa, Mostrar_tarefas, conclusao_task, remover_tarefa

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('\n🧾 Side_quest_day - Suas Missões Diárias.')
    print('1. Adicionar Tarefas')
    print('2. Mostrar Tarefas')
    print('3. Concluir Tarefa')
    print('4. Remover Tarefa')
    print('5. Sair')

def main():
    tarefas = carregar_tarefas()
    
    while True:
        limpar()
        menu()    
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '2':
            Mostrar_tarefas(tarefas)
            input('\nPressione Enter para continuar...')
        elif escolha == '3':
            conclusao_task(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '4':
            remover_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif escolha == '5':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')
            input('\nPressione Enter para continuar...')

if __name__ == '__main__':
    main()