class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        
        def traverse(start, path, n):
            if n < 0:
                return
            
            if n == 0 and len(path) == k:
                combinations.append(path[:])
                return
            
            for i in range(start, 10):
                path.append(i)
                traverse(i + 1, path, n - i)
                path.pop()
        
        traverse(1, [], n)
        return combinations