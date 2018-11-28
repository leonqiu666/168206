#coding=utf-8
#狄克斯特拉算法
#乐谱换钢琴问题
graph={}
graph["yuepu"]={}
graph["yuepu"]["changpian"]=5
graph["yuepu"]["haibao"]=0
graph["changpian"]={}
graph["changpian"]["jita"]=15
graph["changpian"]["jiazigu"]=20
graph["haibao"]={}
graph["haibao"]["jita"]=30
graph["haibao"]["jiazigu"]=35
graph["jita"]={}
graph["jita"]["gangqin"]=20
graph["jiazigu"]={}
graph["jiazigu"]["gangqin"]=10
graph["gangqin"]={}
infinity=float("inf")
costs={}
costs["changpian"]=5
costs["haibao"]=0
costs["jita"]=infinity
costs["jiazigu"]=infinity
costs["gangqin"]=infinity
parents={}
parents["changpian"]="yuepu"
parents["haibao"]="yuepu"
parents["jita"]="None"
parents["jiazigu"]="None"
parents["gangqin"]="None"
processed=[]

def find_low_cost_node(cost):
    low_cost = float("inf") 
    low_node = None
    for node in costs :
        cost = costs[node]
        if(cost<low_cost and node not in filter1) :
            low_cost = cost
            low_node = node
    return low_node
    node = find_low_cost_node(costs)

 
while node is not None :
    cost = costs[node]  
    neighbors = graph1[node]    
    for n in neighbors.keys() :
        new_cost = cost + neighbors[n]  
        if(costs[n] > new_cost) :costs[n] = new_cost   
        parents[n] = node        
    filter1.append(node)            
    node = find_low_cost_node(cost)
    

def get_course(sign) :
    if(sign != "yuepu") :
        return get_course(parent[sign]+" --> "+sign)
    else :
        return sign
print(get_course("gangqin"))
