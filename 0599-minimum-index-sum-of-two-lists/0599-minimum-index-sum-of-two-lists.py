class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        tracker_dict = {}
        for i in range(len(list2)):
            tracker_dict[list2[i]] = [i, -1]
        for j in range(len(list1)):
            item = list1[j]
            if item in tracker_dict:
                tracker_dict[item][1] = tracker_dict[item][0] + j
        print(tracker_dict)
                
        least_index_list = []       #tracker_dict = {"name": [i, index_sum]}
        for key, value in tracker_dict.items():
            if (not least_index_list) and value[1] != -1:
                least_index_list.append(key)
            elif not least_index_list: continue
            else:
                if (value[1] < tracker_dict[least_index_list[0]][1]) and (value[1] != -1):
                    least_index_list = [key]        #Overwritting
                elif value[1] == tracker_dict[least_index_list[0]][1] and value[1] != -1:
                    least_index_list.append(key)
        return least_index_list
        