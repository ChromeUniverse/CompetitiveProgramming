# https://codeforces.com/problemset/problem/1015/A
num_seg, bound = [int(num) for num in input().split()]

x_axis = [False for _ in range(1,bound+1)]

for _ in range(num_seg):
    point1, point2 = [int(num) for num in input().split()]
    for point in range((point1)-1, point2):
        if x_axis[point] == False:
            x_axis[point] = True

remain_points = []

for i in range(len(x_axis)):
    if x_axis[i] == False:
        remain_points.append(i+1)

size = len(remain_points)
print(size)

if size != 0:
    for i in range(size):
        remain_points[i] = str(remain_points[i])
    print(' '.join(remain_points))
