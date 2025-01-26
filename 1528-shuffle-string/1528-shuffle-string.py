class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create a list with the same size as s to store rearranged characters
        result = [''] * len(s)
        
        # Place each character at its target index
        for i, index in enumerate(indices):
            result[index] = s[i]
        
        # Join the list to form the rearranged string
        return "".join(result)
