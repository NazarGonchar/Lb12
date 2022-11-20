from scipy import integrate 
import math 
eps = 0.0001 
def f1(x): 
    return math.tan(x**2+1)/(x**2) 
def simpson(a,b,n): 
    h = (b - a) / n 
    integr = f1(a) + f1(b) 
    for i in range(1,n): 
        k = a + i*h 
        if i%2 == 0: 
            integr += 2 * f1(k) 
        else:
            integr += 4 * f1(k) 
    integr *= h/3 
    return integr 
if abs(simpson(0.8,1.6,2*8) - simpson(0.8,1.6,8))/ 15. <= eps: 
   print("Simpsone method:",round (simpson(0.4,0.8,8), 5)) 
v,err = integrate.quad(f1,0.4,0.8)#Перевірка 
print("Check for the simpsone method = ",round(v, 5)) 