def count_ninjas(x, y, p_room):
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well.
    """
room = [['N', ' ', ' ', ' ', ' '],
        ['N', 'N', 'N', 'N', ' '],
        ['N', ' ', 'N', ' ', ' '],
        ['N', 'N', 'N', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']]
ninjas = count_ninjas(1,0,room)