def isOneDiff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def findLadders(start, end, dt):
    ret = []
    def loop(wa, wb, lt, res=[]):
        for i in lt:
            # wa表示当前单词，wb表示目的单词，lt表示剩余单词，i表示字典选择单词，res表示转化记录
            if isOneDiff(wa, i) and isOneDiff(i, wb): 
                r= res.copy()
                r.append(wa)
                r.append(i)
                r.append(wb)
                ret.append(r)
            if isOneDiff(wa, i) and not isOneDiff(i, wb):
                r = res.copy()
                r.append(wa)
                lt_copy = lt.copy()
                try:
                    lt_copy.remove(wa)  
                except:
                    pass
                loop(i, wb, lt_copy, r)
    loop(start, end, dt)
    return ret

print(findLadders('hit', 'cog', ["hot","dot","dog","lot","log"]))

[
    ['hit', 'hot', 'dot', 'dog', 'cog'],
    ['hit', 'hot', 'dot', 'lot', 'log', 'cog'],
    ['hit', 'hot', 'lot', 'dot', 'dog', 'cog'],
    ['hit', 'hot', 'lot', 'log', 'cog']
]
