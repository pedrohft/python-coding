# Top Down
def house_robber_tp(houses, index, temp):
    if index >= len(houses): return 0
    else:
        if index not in temp:
            steal_first_house = houses[index] + house_robber_tp(houses, index+2, temp)
            skip_first_house = house_robber_tp(houses, index+1, temp)
            temp[index] = max(steal_first_house, skip_first_house)
        return temp[index]

# print(house_robber_tp([6,7,1,30,8,2,4], 0, {}))

# Bottom Up
def house_robber_bu(houses):
    temp_arr = [0]*(len(houses)+2)

    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i] + temp_arr[i+2], temp_arr[i+1])
        print(temp_arr)
    return temp_arr[0]

print(house_robber_bu([6,7,1,30,8,2,4]))