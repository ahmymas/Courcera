hour = input("Enter hours :")
rate = input("Input rate :")
h = float(hour)
p = float(rate)

def computepay(h):
    if h<=40:
        s=h*p
    elif h>40:
        s=h*p+0.5*p*(h-40)
    return s

print("Pay", computepay(h))
