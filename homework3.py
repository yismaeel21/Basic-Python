a = [[2,0],[0,1]]
b = [[1,0],[0,2]]
def is_strictly_dominant_first(u1,s1):
    player_one_strategy = u1[s1]
    for i in range(len(player_one_strategy)):
        for y in range(len(u1)):
            if u1[y][i]>u1[s1][i]:
                return False
    return True

def is_strictly_dominant_second(u2,s2):
    player_two_strategy = u2[s2]
    j = len(player_two_strategy)
    for i in range(j-1):
        for y in range(len(u2)):
            if u2[s2][i]>u2[y][i+1]:
                return False
    return True


def find_strictly_dominant_strategies(u1,u2):
    for y in range(len(u1[0])):
        for x in range(len(u1)):
            if is_strictly_dominant_first(u1,u1[x])== True and is_strictly_dominant_second(u2,u2[y])==True:
                Sdom1= u1[x]
                Sdom2= u2[x]
    return "The first player has strictly dominant strategy", Sdom1, "The second player has strictly dominant strategy", Sdom2