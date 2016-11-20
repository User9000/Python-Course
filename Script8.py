temperatures=[10,-20,-289,100]

file = open("example3.txt","w")

def c_to_f(c):
    if c < -273.15:
        return "That temperature does not make sens!"
    #else:
        f=c*9/5 +32
        return f


for item in temperatures:
    
    result = c_to_f(item)
    file.write("Celcius: "+str(result)+"\n")

file.close()