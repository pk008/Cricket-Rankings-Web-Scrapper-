import requests
from bs4 import BeautifulSoup


def printdata(r):
	soup=BeautifulSoup(r.content,"html.parser")
	table= soup.find_all("tr",{"class":"table-body"})
	print("\tPos\t\tTeam\t\t\tMatches\t\t\tRatings\n")
	for data in table:
		s=data.find_all("td",{"class":"table-body__cell"})
		i=0
		lis=[]
		for l in s:
			lis.insert(i,l.text.strip())
			i=i+1
		if(len(lis[1])<8):
			print("\t"+lis[0]+"\t\t"+lis[1]+"\t\t\t"+lis[2]+"\t\t\t"+lis[4])
		else:
			print("\t"+lis[0]+"\t\t"+lis[1]+"\t\t"+lis[2]+"\t\t\t"+lis[4])



def printChoices():
	print("\t\t\t\tView Rankings")
	print("1.Mens")
	print("2.Womens")
	ch=input("Enter choice : ")
	if(ch=='1'):
		Format = {
		'1': "Test",
		'2': "ODI",
		'3': "T20I"
		}
		print("Select Format")
		for i in Format:
			print(i+" "+Format[i])
		c=input("Enter Choice : ")
		print("\n\n")
		print("\t\t\t\t"+Format[c].upper()+" Rankings\n")
		r=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/'+Format[c].lower())
		printdata(r)
	if(ch=='2'):
		print("\t\t\t\tWOMEN'S Team Rankings\n")
		r=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/')
		printdata(r)


if(__name__=="__main__"):
	printChoices()