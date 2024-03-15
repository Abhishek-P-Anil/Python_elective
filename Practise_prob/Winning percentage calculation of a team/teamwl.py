teams = {}

while True:
    winloss = []
    team_name = input("Enter the team name: ")
    win_count = int(input("Enter the number of wins: "))
    winloss.append(win_count)
    loss_count = int(input("Enter the number of loss: "))
    winloss.append(loss_count)
    teams[team_name] = winloss

    proceed = int(input("1.Contine Entering team\n2.Exit\nEnter your choice: "))
    if proceed == 2:
        break

print("\nTEAMS: " ,end="")
for key in teams:
    print(key,end=", ")

team_list = list(teams.keys())

win_list= []
for key in teams:
    win_list.append(teams[key][0])


loss_list= []
for key in teams:
    loss_list.append(teams[key][1])

win_index = win_list.index(max(win_list))
print("\nHighest win: ",team_list[win_index])

loss_index = loss_list.index(max(loss_list))
print("Highest loss: ",team_list[loss_index])

name = input("\nEnter the name of the team: ")
for key in teams:
    if key == name:
        win = teams[key] [0]
        total_game = win + teams[key] [1]
        print("Win percentage of ",name,": ","%.2f"%((win/total_game)*100))