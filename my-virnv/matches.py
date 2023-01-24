import matplotlib.pyplot as plt
import numpy as np
import csv

franchise = []
matches= {}

with open("/home/himalaya/Downloads/matches - matches.csv") as csvfile:
    matchfile = csv.DictReader (csvfile)

    for row in matchfile:
        if row["team1"] in franchise:
            pass
        else:
            franchise.append (row["team1"])

        if row["season"] in matches:
            if row["team1"] in matches[row["season"]]:
                matches[row["season"]][row["team1"]] += 1
            else:
                matches[row["season"]][row["team1"]] = 1
            if row["team2"] in matches[row["season"]]:
                matches[row["season"]][row["team2"]] += 1
            else:
                matches[row["season"]][row["team2"]] = 1
        
        else:
            matches[row["season"]] = {row["team1"]:1}
            matches[row["season"]] = {row["team2"]:1}
   
  
    
matches = {i : matches[i] for i in sorted (matches.keys())}

season = list(matches.keys())

teams= []
mats= []

# for i in franchise:
#     for year in season:
#         matches[year].keys()

# for year in season:
#     matches[year] = {i : matches[year][i] for i in sorted (matches[year].keys())}
#     team=list(matches[year].keys())
#     mat=list(matches[year].values())
#     teams.append (team)
#     mats.append (mat)


franchise.sort()


listdata = []
for i in range(len(franchise)):
    temp1=list()
    listdata.append(temp1)

for key in season:
    for i in range(len(franchise)):
        listdata[i].append(matches[key].get(franchise[i],0))

y = np.array ([0]*len(listdata[0]))

clr=['r','b','y','g','k','m','c','#E8ABAB','#E8ABE6','#812CD7', '#b84730', '#990000','#298a6a' ,'#330033']

plt.title ("Number of matches played per year")
plt.xlabel ("Year")
plt.ylabel ("Number of matches")


for i in range(len(listdata)):
    temp3=np.array(listdata[i])
    plt.bar(season,temp3,bottom=y,color=clr[i])
    y+=temp3
plt.legend (franchise)
plt.show()
