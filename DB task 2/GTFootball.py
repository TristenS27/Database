def game(file):
    game_list = []
    read_file = record_file.readlines()
    for i in read_file:
        i = i.split(",")
        game_list.append(i)
    game_list.sort()
    first_game = "Georgia Tech's first game ever played was against " + str(game_list[0][1])
    #---
    points = 0
    for i in game_list:
        if i[1] == "Auburn":
            points += int(i[3])
    Points_vs_Auburn = "Georgia Tech has scored " + str(points) + " points all time against Auburn"
    #---
    file.close()

print(game(record_file))