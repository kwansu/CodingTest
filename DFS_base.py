# 각 노드가 정수인 인접 리스트가 주어졌을 때, 깊이우선 탐색을 실행하라.
# 리스트에서 인덱스는 각 노드의 번호이다. (0~7)
# 처음 시작할 노드의 번호는 0이다.

adjacency_list = [[1, 2, 7], [0, 6, 7], [0, 3, 4],
                  [2, 4], [2, 3], [6], [1, 5, 7], [0, 6]]

explored_nodes = [0]
search_stack = [0]

# DFS
while len(search_stack) != 0:
    cur_node = search_stack[-1]
    ad_nodes = adjacency_list[cur_node]

    print(cur_node+1, ' -> ', end='')
    can_not_explore = True
    for node in ad_nodes:
        if node not in explored_nodes:
            explored_nodes.append(node)
            search_stack.append(node)
            can_not_explore = False
            break

    if can_not_explore:
        search_stack.pop()

print()
print(explored_nodes)
