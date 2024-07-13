from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def main():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    
    for _ in range(n):
        node = input("Enter node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
    
    start_node = input("Enter the starting node: ")
    
    print("BFS Traversal: ", end="")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()

