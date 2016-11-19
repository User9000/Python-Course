

def c_to_f(celcius):
   if celcius < -273.15:
       print("impossible")
   else:
       farenheit= celcius-32*5/9
       return farenheit

print("Farenheit:",c_to_f(230))
