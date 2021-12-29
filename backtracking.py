from typing import List

# candidates: List of numbers that the algo to go through for combination
# target: the end goal of the search
# ans: list of list of answer to the target
# combine: the current result that is trying to build
# index: the current index from the candidates list
def dfs(candidates:List, target:int, ans:List, combine:List, index:int):
    if len(candidates) == index:
        return
    if target == 0:
        # has to make a copy here, other it will get removed since it is a refence type
        ans.append(combine[:])
        return
    dfs(candidates, target, ans, combine, index + 1)
    if (target - candidates[index] >= 0):
        combine.append(candidates[index])
        dfs(candidates, target - candidates[index], ans, combine, index)
        # combine is a reference type, need to remove the last element before
        # backtracking to the last layer
        combine.pop(len(combine) - 1)
