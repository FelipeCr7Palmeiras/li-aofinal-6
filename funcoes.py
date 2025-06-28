def ler_usuarios():
    try:
        with open("usuarios.txt", "r") as f:
            return [linha.strip() for linha in f if linha.strip()]
    except:
        return []

def salvar_tarefa(usuario, descricao, prioridade):
    with open("tarefas.txt", "a") as f:
        f.write(f"{usuario}|{descricao}|{prioridade}\n")

def ler_tarefas():
    try:
        with open("tarefas.txt", "r") as f:
            return [linha.strip().split("|") for linha in f if linha.strip()]
    except:
        return []

def filtrar_tarefas(usuario):
    todas = ler_tarefas()
    return [t for t in todas if t[0] == usuario]
