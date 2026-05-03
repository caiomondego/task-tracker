import sys
import json

if len(sys.argv) < 2:
    print("Use: add | list | done | remove")
    sys.exit()
    
comando = sys.argv[1]

if comando == "add":
    tarefa = sys.argv[2]

    with open("tasks.json", "r") as arquivo:
        tarefas = json.load(arquivo)

    nova_tarefa = {"nome": tarefa, "concluida": False}
    tarefas.append(nova_tarefa)

    with open("tasks.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

    print("Tarefa adicionada!")


elif comando == "list":
    with open("tasks.json", "r") as arquivo:
        tarefas = json.load(arquivo)

    print("Suas tarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(i + 1, "-", tarefa["nome"], status)


elif comando == "done":
    numero = int(sys.argv[2])

    with open("tasks.json", "r") as arquivo:
        tarefas = json.load(arquivo)

    if numero - 1 < 0 or numero - 1 >= len(tarefas):
        print("Tarefa não existe!")
    else:
        tarefas[numero - 1]["concluida"] = True

        with open("tasks.json", "w") as arquivo:
            json.dump(tarefas, arquivo)

        print("Tarefa concluída!")

elif comando == "remove":
    numero = int(sys.argv[2])

    with open("tasks.json", "r") as arquivo:
        tarefas = json.load(arquivo)

    if numero - 1 < 0 or numero - 1 >= len(tarefas):
        print("Tarefa não existe!")
    else:
        tarefas.pop(numero - 1)

        with open("tasks.json", "w") as arquivo:
            json.dump(tarefas, arquivo)

        print("Tarefa removida!")
