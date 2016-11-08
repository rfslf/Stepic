ercl_dict = dict()
n = int(input())
for i in range(n):
    cl = str(input()).split(" : ")
    if len(cl) == 1:
        cl.append(" : ")
    ercl_dict[(cl[0])] = cl[1].split()


def bfs(start, end):
    # maintain a queue of paths
    queue = list()
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in ercl_dict.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

# "Yes", если класс 0 является предком класса 1, и "No", если не является.
m = int(input())
que = []
for j in range(m):
    que.append(str(input()))

for x in range(m-1):
    for y in range(x+1):

        if bfs(que[x+1 - m], que[y]):
            print(que[x+1-m])
            break
