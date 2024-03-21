class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pathMap = {}
        for p in paths:
            pathMap[p[0]] = p[1]
        print(pathMap)

        start = paths[0][0]
        while start in pathMap.keys():
            start = pathMap[start]
        return start
