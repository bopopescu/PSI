# Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin. Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.

def przelicznik(wartosc, temperature_type):
    if temperature_type=="Fahrenheit":
        print(str(wartosc) + " stopni/e Celsjusza to")
        wartosc=(9/5)*wartosc+32
        return (str(wartosc) + " stopni/e Fahrenheita")
    elif temperature_type=="Rankine":
        print(str(wartosc) + " stopni/e Celsjusza to")
        wartosc=1.8*wartosc+491.67
        return (str(wartosc) + " stopni/e Rankine'a")
    elif temperature_type=="Kelvin":
        print(str(wartosc) + " stopni/e Celsjusza to")
        wartosc=wartosc+273.15
        return (str(wartosc) + " stopni/e Kelvina")
    else:
        return ("zly typ temperatury")


wartosc=-273.15
temperature_type="Kelvin"

print(przelicznik(wartosc, temperature_type))