def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} (comma-separated): ").split(',')
        graph[node] = [neighbor.strip() for neighbor in neighbors if neighbor.strip()]
    
    return graph

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = input_graph()
start_node = input("Enter the start node for DFS: ")

print("DFS Traversal:")
dfs(graph, start_node)

