import matplotlib.pyplot as plt
import numpy as np
import csv

#season ={}

#city = {}

#wins = {}

# city_field = {}
# city_bat = {}

class Toss:
    bat=0
    ball=0
dict = {str, Toss}
d = {}


with open("/home/himalaya/Downloads/matches - matches.csv") as csvfile:
    matchfile = csv.DictReader (csvfile)

    for row in matchfile:
        if row["city"] in dict:

    # for row in matchfile:
    #     if row["city"] in city_field and row["toss_decision"] == "field":
    #         city_field[row["city"]]+=1
    #     elif row["city"] in city_bat and row["toss_decision"] == "bat":
    #         city_bat[row["city"]]+=1
    #     elif row["city"] not in city_field and row["toss_decision"] == "field":
    #         city_field[row["city"]]=1
    #     elif row["city"] not in city_bat and row["toss_decision"] == "bat":
    #         city_bat[row["city"]]=1

    # for row in matchfile:  
    #     if row["toss_decision"] == "field":
    #         if row["city"] in city_field:
    #             city_field[row["city"]]+=1
    #         else:
    #             city_field[row["city"]]=1
            
    #     if row["toss_decision"] == "bat":
    #         if row["city"] in city_bat:
    #             city_bat[row["city"]]+=1
    #         else:
    #             city_bat[row["city"]]=1



    print(city_field)
    print(city_bat)           
    # for row in matchfile:
    #     if row["winner"] in wins:
    #         wins[row["winner"]]+=1
    #     else:
    #         wins[row["winner"]]=1


    # for row in matchfile:
    #     if row["city"] in city:
    #         city[row["city"]] += 1
    #     else:
    #         city[row["city"]] = 1

#     for row in matchfile:
#         if row["season"] in season:
#             season[row["season"]]+=1
#         else:
#             season[row["season"]]=1

dict_field = {i : city_field[i] for i in sorted (city_field.keys())}
dict_bat = {i : city_bat[i] for i in sorted (city_bat.keys())}

#dict = {i : wins[i] for i in sorted (wins.keys())}

#dict = {i: city[i] for i in sorted(city.keys())}

#dict = {i: season[i] for i in sorted(season.keys())}



x1=dict_field.keys()
x2=dict_bat.keys()
y1=dict_field.values()
y2=dict_bat.values()

place=list(dict_field.keys())
ball=list(dict_field.values())
bat=list(dict_bat.values())
fun=list(dict_bat.keys())

print(place)
print(ball)
# bat.pop()
print(len(place))
print(len(ball))
print(len(bat))
print(len(fun))

# X_axis = np.arange(len(place))
  
# plt.bar(X_axis - 0.2, ball, 0.4, label = 'Ball')
# plt.bar(X_axis + 0.2, bat, 0.4, label = 'Bat')
  
# plt.xticks(X_axis, place, rotation=90)
# plt.xlabel("Place")
# plt.ylabel("Count")
# plt.title("Number of Students in each group")
# plt.legend()
# plt.show()



# plt.title("Matches played per IPL Season", loc="left")
# plt.xlabel("Season")
# plt.ylabel ("No. of Matches")

# plt.title ("No. of IPL matches played at different venues")
# plt.xlabel ("Venues")
# plt.xticks (rotation='vertical')
# plt.ylabel ("No. of matches")

# plt.title("Venues at which team won the toss and elected to bat or field")
# plt.xlabel ("Venues")
# plt.xticks (rotation='vertical')
# plt.ylabel ("Toss and field or bat")
# width = 0.40

# plt.bar (x1, y1, color="green")
# plt.bar (x2, y2, color="blue")

# plt.show()