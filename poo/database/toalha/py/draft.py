class Towel: 
    def __init__(self, color: str, size: str):
        self.color: str = color \
        
        self.size: str = size 
        self.wetness: int = 0
    def __str__(self) -> str:
        return f({self.color} :)
        
print("Qual a cor da sua toalha e o tamanho?")
color = input()
size  = input()

towel: Towel = Towel("blue", " p")
print(f"sua toalha é {towel.color}")

        

