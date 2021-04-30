# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
'''

class PetrolPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance

class Solution:
    def printTour(self, arr):
        n = len(arr)
        start = 0
        end = 1
        currPetrol = arr[start].petrol - arr[end].distance
        while end != start or currPetrol < 0:
            while start != end and currPetrol < 0:
                currPetrol -= arr[start].petrol - arr[start].distance
                start = (start+1)%n
                if start == 0:
                    return -1
            currPetrol += arr[end].petrol - arr[end].distance
            end = (end+1)%n
        return start

if __name__=='__main__':
    arr = [PetrolPump(4, 6), PetrolPump(6, 5), PetrolPump(7,3), PetrolPump(4, 5)] 
    sol = Solution()
    print(sol.printTour(arr))