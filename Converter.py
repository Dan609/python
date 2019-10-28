class UnitConverter:
    def metresToFeet(self, m):
        f = m / 0.3048
        return f
    def feetToMetres(self, f):
        m = f * 0.3048
        return m

converterObj = UnitConverter()

print(converterObj.metresToFeet(1.89))

print(converterObj.feetToMetres(6.0))

print(8**0.5)
