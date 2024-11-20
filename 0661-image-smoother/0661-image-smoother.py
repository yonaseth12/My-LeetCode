class Solution(object):
    def average(self, list1):
        height = len(list1) 
        width = len(list1[0])
        size = height * width
        sum = 0
        for i in list1:
            for j in i:
                sum += j
        return int(floor(sum/size))
    
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        smoothed_list = [[] for j in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[i])):
                y_start = max(i-1,0)
                y_end = min(i+1,len(img)-1)
                x_start = max(j-1,0)
                x_end = min(j+1, len(img[i])-1)
                surr_list = [row[x_start: x_end+1] for row in img[y_start: y_end+1]]
                smoothed_list[i].append(self.average(surr_list))
                
        return smoothed_list