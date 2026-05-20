class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(i)
        return list(dictionary.values())