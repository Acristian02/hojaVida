class calculadoraGastos:
    def __init__(self, ingresos):
        self.ingresos = ingresos
        self.gastos = {}

    def agrega_gastos(self, categoria, cantidad):
        if categoria in self.gastos:
            self.gastos[categoria] += cantidad
        else:
            self.gastos[categoria] = cantidad

    def calculo_balance(self):
        total_gastos = sum(self.gastos.values())
        balance = self.ingresos - total_gastos
        return balance

    def suma(self):
        print("Resumen Financiero:")
        print(f"Ingreso Mensual: ${self.ingresos}")
        print("Gastos:")
        for categoria, cantidad in self.gastos.items():
            print(f"- {categoria}: ${cantidad}")
        print(f"Saldo Final: ${self.calculo_balance()}")

try:
    PresuPuesto = float(input("Ingrese su presupuesto mensual: $"))
except ValueError:
    print("El monto no es valido.")   
    exit 
calculo = calculadoraGastos(PresuPuesto)

while True:
    categoria = input("Ingrese la categoría del gasto (o 'fin' para terminar): ")

    if categoria.lower() == 'fin':
        break

    try:
        cantidad = float(input("Ingrese el monto del gasto: $"))
        if cantidad>PresuPuesto:
            desicion = input("El gasto ingresado supera el presupuesto del mes(¿esta seguro de continuar? 'si' para continuar o 'no' para finalizar)")

            if desicion.lower() =='si':

                calculo.agrega_gastos(categoria, cantidad)

            elif desicion.lower() == 'no':
                break
            else:
                print("Opción no válida.Ingrese 'si' o 'no'.")
        else:
            calculo.agrega_gastos(categoria, cantidad)
    except ValueError:
        print("Por favor, ingrese un monto válido.")
        continue
calculo.suma()