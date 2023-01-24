import matplotlib.pyplot as plt
import numpy as np
import csv

district = {}
schools = []

with open ("/home/himalaya/Downloads/primaryschool - primaryschool.csv") as csvfile:
    matchfile = csv.DictReader (csvfile)

    for row in matchfile:
        if row["cat"] in schools:
            pass
        else:
            schools.append (row["cat"])

        if row["district_name"] in district:
            if row["cat"] in district[row["district_name"]]:
                district[row["district_name"]][row["cat"]] += 1
            else:
                district[row["district_name"]][row["cat"]] = 1
        
        else:
            district[row["district_name"]] = {row["cat"]:1}
        
    dist_name = list(district.keys())

    district = {i : district[i] for i in sorted (district.keys())}
    schools.sort()

    scl_data = []

    for i in range (len(schools)):
        temp1 = list()
        scl_data.append (temp1)
    
    for key in dist_name:
        for i in range (len(schools)):
            scl_data[i].append (district[key].get(schools[i],0))

    # print (schools)
    # print (district)
    # print (dist_name)
    # print(scl_data)
    # print (len(dist_name))
    # print (len(scl_data[0]))
    # print (len(scl_data))

    y = np.array ([0]*len(scl_data[0]))

    clr=['r','b','y','g']

    plt.title("Schools per district")
    plt.xlabel("District Name")
    plt.ylabel("Schools")
    plt.xticks (rotation = 90)

    
    for i in range (len (scl_data)):
        temp2 = np.array(scl_data[i])
        plt.bar (dist_name, temp2, bottom=y, color = clr[i])
        y += temp2
    
    plt.legend (schools)
    plt.show()