def c_to_f(c):
    if c < -273.15:
        return "That temperature does not make sens!"
    else:
        f=c*9/5 +32
