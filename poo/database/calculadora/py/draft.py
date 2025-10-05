class Calculadora:
    def __init__(self,batteryMax:int):
        self.batteryMax:int=batteryMax
        self.battery:int=0
        self.display:float=0.0
    
    def __str__(self):
        return (f"display = {self.display:.2f}, battery = {self.battery}")
    
    def Charge(self, increment:int)->None:
        self.battery+=increment
        if self.battery>self.batteryMax:
            self.battery=self.batteryMax
    
    def Soma(self, n1:float, n2:float)->None:
        if self.battery==0:
            print("fail: bateria insuficiente")
            return
        else:
            self.display=n1+n2
            self.battery-=1
    
    def Divisao(self, n1:float, n2:float)->None:
        if self.battery==0:
            print("fail: bateria insuficiente")
            return
        if n2==0:
            print("fail: divisao por zero")
            self.battery-=1
            return
        else:
            self.display=n1/n2
            self.battery-=1
        
def main():
    calculadora:Calculadora=None #type: ignore
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")   
        
        if args[0]=="end":
            break
        if args[0]=="init":
            batteryMax:int=int(args[1])
            calculadora=Calculadora(batteryMax)
        if args[0]=="charge":
            incremento:int=int(args[1])
            calculadora.Charge(incremento)
        if args[0]=="show":
            print(calculadora)
        if args[0]=="sum":
            n1:float=float(args[1])
            n2:float=float(args[2])
            calculadora.Soma(n1,n2)
        if args[0]=="div":
            n1:float=float(args[1])
            n2:float=float(args[2])
            calculadora.Divisao(n1,n2)

main()