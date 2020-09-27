#In the matrix 0 means traverse is not possible and  1 means possible 
matrix = [
   #0 1 2 3 
   [0,1,1,0], #0
   [0,0,1,0], #1
   [1,0,0,1], #2
   [0,0,0,1], #3
]

#the visited node 
visited = [0]*len(matrix)

#Add the start node to the queue
# Node 0 in this case  
queue = [0]

#set the visited value of node 0 to be visited 
visited[0] = 1

#print(visited)

node = queue.pop(0)
print(node)

while True:
    for x in range(len(matrix)):
        #check route is possible and node is not visited yet 
        if matrix[node][x] == 1 and visited[x] == 0:
            #set the node to be visited
            visited[x] = 1
            queue.append(x)
    if len(queue) == 0:
        break
    else:
        node = queue.pop(0)
        print(node)



