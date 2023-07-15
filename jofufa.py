from randfacts import get_fact
from pyjokes import get_joke
from path import path
jk = get_joke(language="en", category="all")

from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
e = CurrencyRates()
b = BtcConverter() # force_decimal=True to get Decimal rates
try:
	x = get_fact()
	fac = "Did you know that? "+x
	f = round(float(e.get_rates('USD')['INR']),3)
	g = round(float(e.get_rates('EUR')['INR']),3)
	h = round(float(e.get_rates('INR')['USD']),3)
	y = round(float(e.get_rates('CNY')['INR']),3)
	yu = round(float(e.get_rates('CNY')['USD']),3)
	p = round(float(e.get_rates('GBP')['INR']),3)
	j = round(float(e.get_rates('JPY')['INR']),3)
	bi = str(b.get_latest_price('USD'))
	dic = {
		"joke":jk,
		"jokes":jk,
		"fact":fac,
		"facts":fac,
		"$1":"$1 equals "+str(f)+" Indian rupee",
		"€1":"€1 equals "+str(g)+" Indian rupee",
		"rs 1":"Rs 1 equals "+str(h)+" USD",
		"rupees":"Rs 1 equals "+str(h)+" USD",
		"chinese currency":"¥1 equals "+str(y)+" Indian rupee and "+str(yu)+" USD",
		"one pound":"£1 equals "+str(p)+" Indian rupee",
		"£1":"£1 equals "+str(p)+" Indian rupee",
		"japanese currency":"¥1 equals "+str(j)+" Indian rupee",
		"btc":"1 Bitcoin equals "+bi+" USD",
	}
except:
	print("Opps, something went wrong.")

def iname(name):
	with open(path+"txt/owner.txt","w") as g:
		g.write(name)
		g.close()

if __name__ == "__main__":
	print(f,g,h,y,yu,p,j,jk)