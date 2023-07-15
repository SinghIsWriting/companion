from colorama import Fore, init
init(autoreset=True)
from wolframalpha import Client   # this python module solves any query

# Include your own APP_ID of wolframalpha, you can visit https://www.wolframalpha.com
ID = "XXXXXXXXXXXXXX"

def wolf():
	while True:
		question = input("Your query(exit/quit to come out): ")
		if question == 'exit' or question == 'quit':
			break
		try:
			app_id = ID
			clnt = Client(app_id)
			resp = clnt.query(question)
			answer = next(resp.results).text
			print("Answer: ",f"{Fore.YELLOW}"+answer)
		except:
			print(f"{Fore.RED}Sorry, I didn't get you.")
		print()
if __name__ == "__main__":
		wolf()
