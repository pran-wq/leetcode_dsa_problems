def combinationSum(candidates,target):
    candidates.sort()
    results=[]
    def backtrack(start, current_target,path):
        if current_target==0:
            results.append(list(path))
            return

        for i in range (len(candidates)-1):
            if candidates[i] > current_target:
                break 
        
            if i >start and candidates[i] == candidates[i+1]:
                continue
            backtrack(candidates[i+1], current_target-candidates[i], path)
            path.pop()
        backtrack(0,target,[])
        return results
