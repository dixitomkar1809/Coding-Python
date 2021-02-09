# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reorder-data-in-log-files/submissions/

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digilogs = []
        letterlogs = []
        for log in logs:
            if log.split(' ', 1)[1][0].isdigit():
                digilogs.append(log)
            else:
                letterlogs.append(log)
                
        def sortfunction(log):
            logList= log.split(' ', 1)
            return 1, logList[1], logList[0]
        
        letterlogs.sort(key=sortfunction)
        return letterlogs + digilogs