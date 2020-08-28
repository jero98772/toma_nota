class nomina:
    pass

    def CalculoGanancias(self,valor,porcentaje):

        return valor * (porcentaje/100)

    def CalculoDescuentos(self, devengado, porcentaje):
        descuento = devengado * (porcentaje/100)
        return descuento

    def CalculoRetencion(self, devengado):
        if devengado<=3000:
            return 0

        elif devengado > 3000 and devengado <= 5000:
            return  devengado*(1/100)

        elif devengado > 5000 and devengado <= 8000:
            return devengado*(3/100)

        elif devengado > 8000 and devengado <= 12000:
            return devengado * (5 / 100)
        else:
            return devengado * (8 / 100)