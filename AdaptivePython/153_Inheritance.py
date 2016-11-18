cl_dict = {}
n = int(input())
for i in range(n):
    cl = (input()).split(" : ")
    if len(cl) == 1:
        cl.append(" : ")
    cl_dict[(cl[0])] = cl[1].split()


def bfs(start, end):
    # maintain a queue of paths
    queue = []
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
        for adjacent in cl_dict.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

# "Yes", если класс 0 является предком класса 1, и "No", если не является.
q = int(input())
for q in range(q):
    quest = input().split(' ')
    if quest[1] not in cl_dict:
        print('No')
#    if quest[0] == quest[1]: print('Yes')
#   print(bfs(quest[1],quest[0]))
    if not bfs(quest[1], quest[0]):
        print('No')
    else:
        print('Yes')
