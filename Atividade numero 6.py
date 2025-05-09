from datetime import date
atividade = int(input("Digite o numero correspondente a atividade:\n atividade1\n atividade2\n atividade3\n atividade4"))
if atividade == 1:
    def mostrar_mensagem_e_numero(mensagem, numero):
        print("Mensagem:", mensagem)
        print("Número:", numero)


    def main():
        mensagem = input("Digite uma mensagem: ")
        numero = int(input("Digite um número: "))
        mostrar_mensagem_e_numero(mensagem, numero)


    if __name__ == "__main__":
        main()
if atividade == 2:
    def calcular_idade(ano_nascimento):
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento
        return idade


    def main():
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        idade = calcular_idade(ano_nascimento)
        print("Idade:", idade)

    if __name__ == "__main__":
        main()

if atividade == 3:
    def calculo(valor1,valor2,valor3):
        soma = valor1 + valor2 + valor3
        return soma


    if __name__ == "__main__":
        val1 = int(input("Digite um valor inteiro:"))
        val2 = int(input("Digite um valor inteiro:"))
        val3 = int(input("Digite um valor inteiro:"))
        som_resultado = calculo(val1,val2,val3)
        print("A soma dos 3 valores é:",som_resultado)

if atividade == 4:
    print("Escreva um programa em Python que utilize uma função para verificar se um número inteiro é par ou ímpar.\n A função deverá receber um número como argumento e retornar a string valor par e impar.\n A função principal (main) deverá ler um número digitado pelo usuário, chamar a função e exibir o resultado na tela.")
    def verificar_par_ou_impar(numero):
        if numero % 2 == 0:
            return "Par"
        else:
            return "Ímpar"


    def main():
        numero = int(input("Digite um número inteiro: "))
        resultado = verificar_par_ou_impar(numero)
        print(f"O número {numero} é {resultado}.")


    if __name__ == "__main__":
        main()