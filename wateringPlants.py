class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
      steps = 0
      i = 0
      bucket = capacity
      while i < len(plants):
        if(bucket < plants[i]):
          steps = steps + (i * 2)
          bucket = capacity
        else:
          bucket = bucket - plants[i]
          steps = steps + 1
          i = i + 1
      return steps
         
        
