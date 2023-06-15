import numpy as np      
import pandas as pd
from pylab import plt,mpl
import ccxt
import calendar
from datetime import datetime
from sympy import Symbol,expand
import Tools as tl

#Set parameters of Matplotlib
np.random.seed(100)
plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'

#Uses the binance method of the ccxt library to download the data
binance = ccxt.binance()
now = datetime.utcnow()

unixtime = calendar.timegm(now.utctimetuple())
da = (unixtime - 300*300) * 1000 

ohlcv = binance.fetch_ohlcv(symbol='ETH/BTC', timeframe='5m',since=da)
df1 = pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
df1['Time'] = [datetime.fromtimestamp(float(time)/1000) for time in df1['Time']]
df1.set_index('Time')

#Set the resample interval of 15 minute
df1_risultato = df1.resample('15T', on = 'Time').mean()

#View the 'Close' price chart of the ETH / BTC pair of the Binance exchange
df1_risultato.plot(y='Close',figsize=(10,6), title="ETH/BTC Close Price")
plt.show()

#Perform standardization
l = df1_risultato['Close'].values
l = (l-l.mean()) / np.std(l)
f = np.linspace(-2,2, len(l))

#Displays the standardized values ​​of the ETH / BTC cryptocurrency pair
plt.figure(figsize=(10,6))
plt.plot(f,l,'ro')
plt.title('Standardized values of ETH/BTC Close Price')
plt.xlabel('Time')
plt.ylabel('Labels: Price')
plt.show()

#Calculate the fifth degree equation with the estimated coefficients
reg = np.polyfit(f,l,deg=5)
equazione = np.poly1d(reg)
x=Symbol('x')
#print function with coefficients
print(expand(equazione(x)))

#Calculate the approximate functions of the third, fifth and seventh degree
p = np.polyval(reg,f) #valori predetti di quinto grado 
reg1 = np.polyfit(f,l,deg=3) #coefficienti funzione di terzo grado
reg2 = np.polyfit(f,l,deg=7) #coefficienti funzione di settimo grado
p1 = np.polyval(reg1,f) #valori predetti di terzo grado
p2 = np.polyval(reg2,f) #valori predetti di settimo grado


tl1 = tl.Tools()
#Print MSE values
print('%.12f' % tl1.MSE(l,p1)) #terzo grado
print('%.12f' % tl1.MSE(l,p)) #quinto grado
print('%.12f' % tl1.MSE(l,p2)) #settimo grado

#Displays the approximation functions
plt.figure(figsize=(10,6))
plt.plot(f,l,'ro',label='real values')
plt.plot(f,p1,'--', label = 'regression 3 degree')
plt.plot(f,p, '--', label = 'regression 5 degree') 
plt.plot(f,p2,'--', label = 'regression 7 degree')
plt.legend()


#Set the labels in the fifth degree function
"""for a,b in zip(f, p2): 
    plt.text(a, b, "{:.12f}".format(b))"""

plt.show()

#Calculate the step of 5 minute for the future value
c = 2*2 / f.size #measure of 5 minute; 2 (remember size -2 to +2) equal max = last value of time
d = 2+c #last value of time plus c 

#add value d to numpy array f1
f1= np.append(f,d)
#add len(l)-1 to numpy array l1
l1 = np.append(l,l[len(l)-1])


#Calcolate the future value (in this case 5 minute) 
predetto5grado = np.polyval(reg,d)
predetto3grado = np.polyval(reg1,d)
predetto7grado = np.polyval(reg2,d)

#add predict value to numpy array of regression degree on last position
p1p = np.append(p1,predetto3grado)
p2p = np.append(p2,predetto7grado)
pp = np.append(p,predetto5grado)
print('*********************')
print('Predict values: ')
print('*********************')
print('%.12f' % predetto3grado) 
print('%.12f' % predetto5grado) 
print('%.12f' % predetto7grado) 

#print of regression degree + predict value
plt.plot(f1,l1,'ro',label='real values')
plt.plot(f1,p1p,'--',label='regression 3 degree + predict value')
plt.plot(f1,pp,'--',label='regression 5 degree + predict value')
plt.plot(f1,p2p,'--',label='regression 7 degree + predict value')
plt.legend()
plt.show()

#trasform the predict value in price value
print(np.std(l1))
cl = df1_risultato['Close'].values
price3grado = (float(predetto3grado) * float(np.std(cl))) +float(cl.mean())
price5grado = (float(predetto5grado) * float(np.std(cl))) +float(cl.mean())
price7grado = (float(predetto7grado) * float(np.std(cl))) +float(cl.mean())

print('*********************')
print('Price values: ')
print('*********************')
print(price3grado)
print(price5grado)
print(price7grado)