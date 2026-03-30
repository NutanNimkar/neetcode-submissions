class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        hashMap = {}
        result = []

        for string in strs:
            sortedString = str(sorted(string)) # O(n.logn)
            if sortedString not in hashMap:  # O(1)
                hashMap[sortedString] = [string]
                # hashMap[sortedString].append(string) # O(1)
            else:
                hashMap[sortedString].append(string) 


        for value in hashMap.values():
            result.append(value)

        return result