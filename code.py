class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        n=len(startTime)
        i=0
        c=0
        while i<n:
            if startTime[i]<=queryTime <=endTime [i]:
                c+=1
            i+=1
        return c
        
