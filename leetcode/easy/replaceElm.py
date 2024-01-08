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
#Temporarily hold onto the highest value encountered thus far.
#Compare the current element with this highest value:
#If the current element exceeds the highest value, update the highest value to reflect this new maximum.
#Then, replace the current element in the array with the previously held highest value.
