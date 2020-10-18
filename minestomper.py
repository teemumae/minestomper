def count_ninjas(x, y, p_room):
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well.
    """
    
    ninjas = 0
    if room[y][x] == "N":
        ninjas += 1
    for y1 in range(len(p_room)):
        for x1 in range(len(p_room[y1])):
            if p_room[y1][x1] == "N" and y1 == y-1 and x1 == x:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y-1 and x1 == x-1:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y-1 and x1 == x+1:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y and x1 == x-1:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y and x1 == x+1:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y+1 and x1 == x:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y+1 and x1 == x-1:
                ninjas += 1
            elif p_room[y1][x1] == "N" and y1 == y+1 and x1 == x+1:
                ninjas += 1
    return ninjas
room = [['N', ' ', ' ', ' ', ' '],
        ['N', 'N', 'N', 'N', ' '],
        ['N', ' ', 'N', ' ', ' '],
        ['N', 'N', 'N', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']]
ninjas = count_ninjas(1,2,room)
print(ninjas)