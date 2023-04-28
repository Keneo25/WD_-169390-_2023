import matplotlib.pyplot as plt
import numpy as np

#zad1/zad2
#x = np.arange(0.0,21.0,1.0)
#plt.plot(x,1/x,'g--^', label="f(x)=1/x")
#plt.xlabel("x")
#plt.ylabel("f(x")
#plt.title("Wykres funkcji f(x) dla [1,20]")
#plt.legend()


#plt.show()


#zad3
#x = np.arange(0.0,30.0,0.1)
#s = np.sin(x)
#c = np.cos(x)
#plt.plot(x,s,'g', label="f(x)=sin(x)")
#plt.plot(x,c,'r', label="f(x)=cos(x)")
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.title("Wykres funkcji f(x) dla [0,30]")
#plt.legend()
#plt.show()

#zad4
x = np.arange(0.0,30.0,0.1)
s = np.sin(x)
plt.plot(x,s,'g', label="f(x)=sin(x)")
plt.plot(x,s**2,'r', label="f(x)=sin(x)")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla [0,30]")
plt.legend()
plt.show()

