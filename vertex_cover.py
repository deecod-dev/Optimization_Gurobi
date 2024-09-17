


# 1 2
# 1 3 
# 1 4
# 1 5
# 2 3
# 2 4 
# 2 5
# 3 4
# 3 5
# 4 5
# # # mera graph:

#uncomment this for the first code with normal vertex cover(without any optimization like using the min num of vertices) :
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
# # m.setObjective(sum(x[i-1] for i in nodes),GRB.MINIMIZE) #sum of 0s and 1's
# edges=[]
# for i in graph.keys():
#     # print(graph[i])
#     for j in graph[i]:
#         if(i<j):
#             # print(i,j)
#             edges.append([x[i-1],x[j-1]])
#             # edges.append([i-1,j-1])
# print(edges)
# # print(x[0].x)
# for i in edges:
#     # print(i)
#     # m.addConstr(i[0]==1 or i[1]==1)
#     # if(i>j)
#     m.addConstr((i[0]+i[1])>=1)
# m.optimize()
# print(m.ObjVal)
# print(x)






# # dusra graph to paste on the site
# # 1 2
# # 1 3
# # 3 4
# # 4 5
# # 5 6
# # 6 7

#uncomment this for the second code with min vertex cover :
# graph = {
#     1: [2, 3], 
#     2: [1],     
#     3: [1, 4],   
#     4: [3, 5],   
#     5: [4, 6],    
#     6: [5, 7],   
#     7: [6]       
# }
# nodes=[i for i in graph.keys()]
# print(nodes)
# # for any problem in which we have to select something(upar bhi), we can give that thing a binary variable and the use the select or don't select method\
# from gurobipy import *
# import gurobipy as gp
# m=Model("cover")
# x=m.addVars(len(nodes),vtype=GRB.BINARY,name="x") #ye array
# m.setObjective(sum(x[i-1] for i in nodes),GRB.MINIMIZE) #sum of 0s and 1's basically the line to find min ver cov
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

#uncomment this for the 3rd code with vertex cover with minimum weights:
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
#     # print(i[0],i[1])
#     m.addConstr((x[i[0]-1]+x[i[1]-1])>=1)

# # m.setObjective(sum( e[2] for e in edges if( x[e[0]-1] + x[e[1]-1]>=2 )), GRB.MINIMIZE)
# m.setObjective(sum( e[2]*x[e[0]-1]*x[e[1]-1] for e in edges), GRB.MINIMIZE)
# m.optimize()
# print("min weights:",m.ObjVal) 
# print(x)



