#49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = dict()
        for i, n in enumerate(strs):
            if str(sorted(n)) not in storage:
                storage[str(sorted(n))] = [i]
            else:
                storage[str(sorted(n))].append(i)
        ret = list()
        for key in storage:
            anagrams = list()
            for i in storage[key]:
                anagrams.append(strs[i])
            ret.append(anagrams)
        return ret
