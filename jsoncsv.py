import json
import csv
import sys



def jsontocsv(textfile):
	jsonfile = open(str(textfile)+".json", "r") #open json file
	print("file loaded") #checks
	json_parsed = json.load(jsonfile) #turns the json file into dictionaries and lists
	
	json_headers = json_parsed["resultSets"][0]["headers"] #these are the headers
	json_players = json_parsed["resultSets"][0]["rowSet"] #these are the cases
	
	print("csv created") #just to check to see where code is
	jsoncsv = open(str(textfile)+".csv",'w') #create csv file with the same name as json file

	
	print("writing headers") #writing headers into the csv file
	numheader = len(json_headers)
	for i in range(numheader-2):
		jsoncsv.write(json_headers[i]+", ")
	jsoncsv.write(json_headers[numheader-1] + "\n")

	print("writing data") #writing player data into file
	for player in json_players:
		numstat = len(player)
		for i in range(numstat-2):
			jsoncsv.write(str(player[i]) +", ")
		jsoncsv.write(str(player[numstat-1]) +"\n")
		
	print("finished")
	jsoncsv.close()
	
	
def main():
	jsondata = sys.argv[1] #put file name WITHOUT EXTENSTION after the script in termina, program is made to add on .json
	jsontocsv(str(jsondata)) #run jsontocsv function
	

if __name__ == '__main__':
	main() #run main 




#extra stuff, ignore this
"""
print("json_parsed is:", type(json_parsed)) 
print("json_parsed[resultSets] is: ", type(json_parsed["resultSets"]))
print("json_parsed[resultSets][0] is: ", type(json_parsed["resultSets"][0]))
print("json_parsed[resultSets][0][headers] is: ", type(json_parsed["resultSets"][0]["headers"]))

json_headers = json_parsed["resultSets"][0]["headers"]
json_players = json_parsed["resultSets"][0]["rowSet"]
	
print (json_parsed["resultSets"][0].keys())

print("json_headers: ", type(json_headers))
print("json_players: ",type(json_players))

numheader = len(json_headers)
	for i in range(numheader-2):
		jsoncsv.write(json_headers[i],",",sep = "", end = "")
	print (json_headers[numheader-1], "\n")


	for player in json_players:
		numstat = len(player)
		for i in range(numstat-2):
			print (player[i],",",sep = "", end ="")
		print(player[numstat-1])
	
"""

	
