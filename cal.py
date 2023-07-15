from calendar import month
from datetime import datetime

mont = ['january','february','march','april','may','june','july','august','september','october','november','december']
m = datetime.now().month
y = datetime.now().year
# print(m,y)
def cl(d=f"calander of {mont[m-1]} {y}"):
	try:
		l = d.split()
		year = int(l[3])
		month = int(mont.index(l[2])+1)
		print(month(year,month))
	except:
		print("\nUsage: speak - calendar of MONTH_NAME YEAR")
		pass
if __name__ == "__main__":
	cl()