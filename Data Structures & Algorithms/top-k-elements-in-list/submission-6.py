class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        # starting point
        frequent_list = []
        for key in my_dict:
            frequent_list.append(my_dict[key])
        frequent_list.sort(reverse=True)
        return_list = []
        for i in range(0, k):
            return_list.append(frequent_list[i])
        top_k_list = []
        for key in my_dict:
            if my_dict[key] in return_list:
               top_k_list.append(key)
        return top_k_list
        