graph={}
n=int(input("Enter the number of nodes : "))
for i in range(n):
    ver=input("Enter the vertice : ")
    neigh=input("Enter the neighbouring nodes : ").split()
    graph[ver]=neigh
startnode=input("Enter the start node :")
print(graph[startnode])
