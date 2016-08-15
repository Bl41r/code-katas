import math
def calc_dist(x_n, x_ni):        #calculate distance from x_n to x_n+i
    dist = math.sqrt(float(x_ni)**2 - float(x_n)**2)
    return dist

def tour(friends, friend_towns, home_to_town_distances):
    master_dict = {}  
    x = ''
    y = ''
    z = 0.0
    friend_towns_dict = {}

    for friend_town in range(0, len(friend_towns)):  # make dict for easy ref
      friend_towns_dict[friend_towns[friend_town][0]] = friend_towns[friend_town][1]

    for friend in friends:  # make dict of tuples with all 3 data info
      x = friend
      try:
        y = friend_towns_dict[friend]
      except KeyError:
        break
      z = home_to_town_distances[y]
      master_dict[x] = [y,z]

    total_dist = master_dict[friends[0]][1]
    for i in range(0, len(friends)-1):
      try:
        key1 = friends[i]
        key2 = friends[i+1]
        dist1 = master_dict[key1][1]
        dist2 = master_dict[key2][1]

        total_dist += calc_dist(dist1, dist2)
      except KeyError:
        break
    finished = False
    i = len(friends)-1
    while not finished:
      key1 = friends[i]
      try:
        total_dist += master_dict[key1][1]
        finished = True
      except:
        i -= 1
        if i == 0:
          finished == True
    return int(total_dist)
