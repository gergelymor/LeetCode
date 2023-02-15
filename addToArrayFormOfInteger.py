#989. Add to Array-Form of Integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        additive = int("".join(map(str, num)))
        result = str(additive + k)
        arrayForm = list()
        for i in result:
            arrayForm.append(int(i))
        return arrayForm
