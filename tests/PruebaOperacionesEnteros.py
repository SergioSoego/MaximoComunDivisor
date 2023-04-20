class OperacionesEnteros:
    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
             numero2 = numero1 % numero2
            numero1 = temporal
        return numero1
    def MCD_recursivo(self, numero1, numero2):
         if numero2 == 0:
             return numero1
         return self.MCD_recursivo(numero2, numero1 % numero2)
