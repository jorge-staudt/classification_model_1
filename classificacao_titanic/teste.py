def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a) ao VSCode."

if __name__ == "__main__":
    nome = input("Qual seu nome? ")
    mensagem = saudacao(nome)
    print(mensagem)
