def calcular_imc(peso, altura):
    """
    Calcula o IMC (Índice de Massa Corporal) com base no peso e altura.

    Args:
        peso (float): O peso em quilogramas.
        altura (float): A altura em metros.

    Returns:
        float: O IMC calculado.
    """
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC em diferentes categorias.

    Args:
        imc (float): O IMC calculado.

    Returns:
        str: A classificação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Sua classificação é: {classificacao}")

if __name__ == "__main__":
    main()