class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        indices = {}

        for i, word in enumerate(list1):
            indices[word] = i

        min_sum = float('inf')
        result = []

        for i, word in enumerate(list2):
            if word in indices:
                index_sum = indices[word] + i

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [word]

                elif index_sum == min_sum:
                    result.append(word)

        return result


solution = Solution()
list1 = input().split()
list2 = input().split()
result = solution.findRestaurant(list1, list2)
print(result)
