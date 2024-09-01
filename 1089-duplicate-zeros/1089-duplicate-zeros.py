class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)  # Insert 0 at the current position
                i += 1  # Skip the newly inserted zero
                arr.pop()  # Remove the last element to maintain the original length
            i += 1
