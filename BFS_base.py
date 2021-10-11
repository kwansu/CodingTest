adjacency_list = [[1, 2, 7], [0, 6, 7], [0, 3, 4],
                  [2, 4], [2, 3], [6], [1, 5, 7], [0, 6]]

explored_nodes = [0]
search_queue = [0]

while len(search_queue) != 0:
    i = search_queue.pop(0)
    print('(', end='')
    for j in adjacency_list[i]:
        if j not in explored_nodes:
            print(j+1, end=' ')
            explored_nodes.append(j)
            search_queue.append(j)
    print(') -> ', end='')

print(explored_nodes)