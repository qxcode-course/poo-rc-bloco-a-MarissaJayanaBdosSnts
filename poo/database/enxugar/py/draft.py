class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color 
        self.size: str = size
        self.wetness: int = 0
    
    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.isMaxWetness ():
            self.wetness = self.isMaxWetness ()
        print ("toalha suada")

    def isMaxWetness(self) -> int:
        if self.size == "P": 
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 

    def __str__(self) -> str: 
        return f"Color:{self.color}, Size:{self.size}, Wet:{self.wetness}"
    
    
def main():
        towel: Towel = Towel ("", "")
        while True:
            line: str = input ()
            args: list[str] = line.split(" ")
            
            if args [0] == "end":
                 break
            if args[0] == "end":
                break
            elif args [0] == "new":
                color: str = args [1]
                size: str = args[2]
                towel = Towel (color, size)
            elif args [0] == "dry":
                 amount: int = int(args[1])
                 towel.dry(amount)
            elif args [0] == "wow":
                    print(towel)
            else:
                print ("erro: comando não encontrado")
#towel1: Towel = Towel("blue", "P")
#print(towel1)
#towel1.dry(5)
#towel1.dry(50)
#print(towel1)        

main()