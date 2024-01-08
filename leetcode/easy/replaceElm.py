class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr) - 1
        largest = -2
        past = -1
        for n in range(l, -1, -1):
            temp = past
            if arr[n] > past:
                past = arr[n]
            arr[n] = temp
                    

        return arr
