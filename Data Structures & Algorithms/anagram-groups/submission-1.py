class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        # set the hasp map's pair -> (sorted_str, idx)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [] # create new hash map inside the mac
            
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in hash_map:
                hash_map[sorted_str].append(string)

        strs_lists = []
        for key in hash_map:
            str_list = []
            for value in hash_map[key]:
                str_list.append(value)
            strs_lists.append(str_list)
        
        return strs_lists
                


        
        