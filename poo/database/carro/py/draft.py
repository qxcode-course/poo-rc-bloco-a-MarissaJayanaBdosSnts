class Carro:
    def __init__(self):
        self.passageiros: int = 0
        self.max_passageiros: int = 2
        self.gasolina: int = 0
        self.max_gasolina: int = 100
        self.km: int = 0

    def __str__(self) -> str:
        return f"pass: {self.passageiros}, gas: {self.gasolina}, km: {self.km}"
    
    def entrar(self) -> None:
        if self.passageiros < self.max_passageiros:
            self.passageiros += 1
        else:
            print("fail: limite de pessoas atingido")
    
    def sair(self) -> None:
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passageiros -= 1
    
    def abastecer(self, quantidade: int) -> None:
        self.gasolina += quantidade
        if self.gasolina > self.max_gasolina:
            self.gasolina = self.max_gasolina

    def dirigir(self, distancia: int) -> None:
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gasolina == 0:
            print("fail: tanque vazio")
        elif self.gasolina < distancia:
            self.km += self.gasolina
            print(f"fail: tanque vazio apos andar {self.gasolina} km")
            self.gasolina = 0
        else:
            self.km += distancia
            self.gasolina -= distancia


def main():
    carro = Carro()

    while True:
        linha: str = input()
        print("$" + linha)
        partes: list[str] = linha.split(" ")

        comando = partes[0]

        if comando == "end":
            break
        elif comando == "enter":
            carro.entrar()
        elif comando == "leave":
            carro.sair()
        elif comando == "fuel":
            incremento = int(partes[1])
            carro.abastecer(incremento)
        elif comando == "drive":
            distancia = int(partes[1])
            carro.dirigir(distancia)
        elif comando == "show":
            print(carro)


main()
