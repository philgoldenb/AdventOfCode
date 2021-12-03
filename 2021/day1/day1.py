def increase_count(depths):
    incr_count = 0
    for i in range(1,len(depths)):
        if depths[i] > depths[i-1]:
            incr_count += 1 
    return incr_count

def window_increase_count(depths):
    depth_windows = []
    for i in range(len(depths)-2):
        window_sum = depths[i] + depths[i+1] + depths[i+2]
        depth_windows.append(window_sum)
    return(increase_count(depth_windows))

with open("/Users/phil/repos/AdventOfCode/2021/day1/input.txt",'r') as input:
    depths = [int(line) for line in input]

print(increase_count(depths))
print(window_increase_count(depths))
