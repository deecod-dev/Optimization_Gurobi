# from gurobipy import *
# mod=Model(name="linear_optimizer")
# x=mod.addVar(name="x",vtype=GRB.CONTINUOUS, lb=0)
# y=mod.addVar(name="y",vtype=GRB.CONTINUOUS, lb=0)

# obj=5*x+4*y
# mod.setObjective(obj,GRB.MINIMIZE)

# c1=mod.addConstr(x+y>=8,name="c1")
# c2=mod.addConstr(2*x+y>=10,name="c2")
# c3=mod.addConstr(x+4*y>=11,name="c3")

# mod.optimize()
# mod.write("lp\out.lp")

# print("objective_val",mod.ObjVal)
# for v in mod.getVars():
#     print(v.VarName,v.x)

#obj fn:           ci xi
#constraints:      aij bi
#                  xi>0
# i= 1-m, j=i-n



# knapsack
w=[4,2,5,4,5,1,3,5]
v=[10,5,18,12,15,1,2,8]
c=15
n=len(w)
from gurobipy import *
knapsack=Model("knapsack")
x=knapsack.addVars(n,vtype=GRB.BINARY,name="x")
print(x)
knapsack.setObjective((sum(v[i]*x[i] for i in range(n))),GRB.MAXIMIZE)
arr2=[w[i]*x[i] for i in range(n)]
knapsack.addConstr(sum(arr2)<=c)
knapsack.optimize()
# print(knapsack.ObjVal)
# print(x[1].x)



# # MAX FLOW
# from gurobipy import *
# graph = [[0, 16, 13, 0, 0, 0],
#         [0, 0, 10, 12, 0, 0],
#         [0, 4, 0, 0, 14, 0],
#         [0, 0, 9, 0, 0, 20],
#         [0, 0, 0, 7, 0, 4],
#         [0, 0, 0, 0, 0, 0]]
# s = 0; t = 5
# nodes=[i for i in range(len(graph))]
# edges,capacities=[],{}
# for i in range(len(nodes)):
#     for j in range(len(nodes)):
#         if graph[i][j]!=0:
#             edges.append((i,j))
#             capacities[(i,j)]=graph[i][j]
# print(edges)
# print(capacities)
# m=Model("max_flow")
# flows = {}
# for (u, v) in edges:
#     flows[(u, v)] = m.addVar(lb=0, ub=capacities[(u, v)], obj=0, vtype=GRB.CONTINUOUS, name=f"f{u}->{v}")
# # print(flows[edges[0]])
# m.setObjective(sum(flows[(s,v)] for v in nodes if (s,v) in edges) , GRB.MAXIMIZE) # v in nodes if
# for (u,v) in edges:
#     m.addConstr(flows[(u,v)]<=capacities[(u, v)])
#     m.addConstr(flows[(u,v)]>=0)

# #for each node, outflow-inflow should be same
# print(flows)
# for u in nodes:
#     if u != s and u != t: 
#         # inflow = sum(flows[(v,u)] for (v, u) in flows)
#         # outflow = sum(flows[(u,w)] for (u, w) in flows)
#         inflow = sum(flows.get((v, u), 0) for v in nodes if (v, u) in flows)
#         outflow = sum(flows.get((u, w), 0) for w in nodes if (u, w) in flows)
#         m.addConstr(inflow - outflow == 0, f"FlowConservation_{u}")

# m.optimize()
# print(flows[(0,1)].x)
# print(m.ObjVal)
