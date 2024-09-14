

#mera graph:
# graph = {
#     1: [2, 3, 4, 5],
#     2: [1, 3, 4, 5], 
#     3: [1, 2, 4, 5], 
#     4: [1, 2, 3, 5],
#     5: [1, 2, 3, 4]  
# }
# nodes=[i for i in graph.keys()]
# print(nodes)
# # for any problem in which we have to select something, we can give that thing a binary variable and the use the select or don't select method\
# from gurobipy import *
# import gurobipy as gp
# m=Model("cover")
# x=m.addVars(len(nodes),vtype=GRB.BINARY,name="x") #to ye array ho gayi variables x ki
# m.setObjective(sum(x[i-1] for i in nodes),GRB.MINIMIZE) #sum of 0s and 1's
# edges=[]
# for i in graph.keys():
#     # print(graph[i])
#     for j in graph[i]:
#         if(i<j):
#             edges.append([x[i-1],x[j-1]])
#             # edges.append([i-1,j-1])
# # print(edges)
# # print(x[0].x)
# for i in edges:
#     # print(i)
#     # m.addConstr(i[0]==1 or i[1]==1)
#     # if(i>j)
#     m.addConstr((i[0]+i[1])>=1)
# m.optimize()
# print(m.ObjVal)
# print(x)






#dusra graph to paste on the site
# 1 2
# 1 3
# 3 4
# 4 5
# 5 6
# 6 7
# graph = {
#     1: [2, 3],     # Node 1 is connected to Node 2 and Node 3
#     2: [1],        # Node 2 is connected to Node 1 (undirected)
#     3: [1, 4],     # Node 3 is connected to Node 1 and Node 4
#     4: [3, 5],     # Node 4 is connected to Node 3 and Node 5
#     5: [4, 6],     # Node 5 is connected to Node 4 and Node 6
#     6: [5, 7],     # Node 6 is connected to Node 5 and Node 7
#     7: [6]         # Node 7 is connected to Node 6
# }
# nodes=[i for i in graph.keys()]
# print(nodes)
# # for any problem in which we have to select something, we can give that thing a binary variable and the use the select or don't select method\
# from gurobipy import *
# import gurobipy as gp
# m=Model("cover")
# x=m.addVars(len(nodes),vtype=GRB.BINARY,name="x") #ye array
# m.setObjective(sum(x[i-1] for i in nodes),GRB.MINIMIZE) #sum of 0s and 1's
# edges=[]
# for i in graph.keys():
#     # print(graph[i])
#     for j in graph[i]:
#         if(i<j):
#             edges.append([x[i-1],x[j-1]])
#             # edges.append([i-1,j-1])
# # print(edges)
# # print(x[0].x)
# for i in edges:
#     # print(i)
#     # m.addConstr(i[0]==1 or i[1]==1)
#     # if(i>j)
#     m.addConstr((i[0]+i[1])>=1)
# m.optimize()
# print(m.ObjVal)
# print(x)
# for i in x:
#     print(i+1,x[i].x)







# #minimizing the weights:
# # 1 2 2
# # 1 3 3
# # 1 4 1
# # 1 5 4
# # 2 3 5
# # 2 4 2
# # 2 5 3
# # 3 4 1
# # 3 5 2
# # 4 5 4
# graph = {
#     1: [(2, 2), (3, 3), (4, 1), (5, 4)],
#     2: [(1, 2), (3, 5), (4, 2), (5, 3)],
#     3: [(1, 3), (2, 5), (4, 1), (5, 2)],
#     4: [(1, 1), (2, 2), (3, 1), (5, 4)],
#     5: [(1, 4), (2, 3), (3, 2), (4, 4)]
# }

# nodes=[i for i in graph.keys()]
# # print(nodes)
# # for any problem in which we have to select something, we can give that thing a binary variable and the use the select or don't select method\
# from gurobipy import *
# import gurobipy as gp
# m=Model("cover")
# x=m.addVars(len(nodes),vtype=GRB.BINARY,name="x") #ye array
# # m.setObjective(sum(x[i-1] for i in nodes),GRB.MINIMIZE) #sum of 0s and 1's
# edges=[]
# weights={}
# for i in graph.keys():
#     for j in graph[i]:
#         if(i<j[0]):
#             edges.append([i,j[0],j[1]])
# print(edges)

# for i in edges:
#     m.addConstr((x[i[0]-1]+x[i[1]-1])>=1)
# # m.setObjective(sum( e[2] for e in edges if( x[e[0]-1] + x[e[1]-1]>=2 )), GRB.MINIMIZE)
# m.setObjective(sum( e[2]*x[e[0]-1]*x[e[1]-1] for e in edges), GRB.MINIMIZE)
# m.optimize()
# print("min weights:",m.ObjVal) 
# print(x)





# #chess:
# from gurobipy import *
# import gurobipy as gp
# m=Model("queens")
# n=8
# x=m.addVars(n,vtype=GRB.INTEGER,name="x",lb=1,ub=n)
# m.addConstr(x[0]>=1)
# m.addConstr(x[0]<=8)
# M=100
# for i in range(n-1): #0 to 6, 1
#     it=0
#     for j in range((i+1)-1,-1,-1):#1,0
#         #x2!=x1, x2!=x0
#         # print(i+1,"!=",i-it,"+",0)
#         b = m.addVar(vtype=GRB.BINARY)
#         m.addConstr(x[i+1]<x[i]+ M * b)
#         m.addConstr(x[i+1]>x[i])
#         # print(i+1,"!=",i-it,"+",(i-j+1))
#         b = m.addVar(vtype=GRB.BINARY)
#         m.addConstr(x[i+1]>x[i]+(i-j+1))
#         m.addConstr(x[i+1]<x[i]+(i-j+1))
#         # print(i+1,"!=",i-it,"-",(i-j+1))
#         b = m.addVar(vtype=GRB.BINARY)
#         m.addConstr(x[i+1]>x[i]-(i-j+1))
#         m.addConstr(x[i+1]<x[i]-(i-j+1))
#         it+=1
    

# # chess:
# from gurobipy import *
# import gurobipy as gp
# m=Model("queens")
# n=8
# x=m.addVars(n,n,vtype=GRB.INTEGER,name="x",lb=1,ub=n)
# lst=[]


#chess:
from gurobipy import *
import gurobipy as gp
m=Model("queens")
n=8
x=m.addVars(n,n,vtype=GRB.BINARY,name="x")
# print(x[0,0])
for i in range(n):
    m.addConstr(sum(x[j,i] for j in range(n))==1)
    m.addConstr(sum(x[i,j] for j in range(n))==1)

# # 3. No two queens on the same main diagonal (i - j is constant)
# for d in range(-n + 1, n):  # d is the difference between i and j
#     m.addConstr(quicksum(x[i, j] for i in range(n) for j in range(n) if i - j == d) <= 1, name=f"diag_main_{d}")

# # 4. No two queens on the same anti-diagonal (i + j is constant)
# for d in range(2 * n - 1):  # d is the sum of i and j
#     m.addConstr(quicksum(x[i, j] for i in range(n) for j in range(n) if i + j == d) <= 1, name=f"diag_anti_{d}")


# for i in range(8):
#     # for j in range(i+1):
#     #     print(7-j,7+j-i) 
#     #     print(i-j,j)
#     # print()
#     m.addConstr(sum( x[7-j,7+j-i] for j in range(i+1) )<=1)
#     m.addConstr(sum( x[i-j,j] for j in range(i+1) )<=1)

# for i in range(8):
#     # for j in range(i+1):
#     #     print(j,7-(i-j))
#     #     print(7-(i-j),j)
#     # print()
#     m.addConstr(sum( x[j,7-(i-j)] for j in range(i+1) )<=1)
#     m.addConstr(sum( x[7-(i-j),j] for j in range(i+1) )<=1)
m.setObjective(0,GRB.MINIMIZE)
m.optimize()


solution = []
for i in range(n):
    row = ""
    for j in range(n):
        if x[i, j].x > 0.5:
            row += "Q "  # Queen placed
            solution.append((i, j))  # Store queen position
        else:
            row += ". "  # Empty cell
    print(row)
print(f"Solution: {solution}")