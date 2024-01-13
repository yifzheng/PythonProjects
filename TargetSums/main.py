def target_sum(list, target):
   # define a hashmap to store all seen idnex total pairs
   dp = {}
   
   # define backtracking function to calculate based on decision tree of +1 and -1 per index
   def backtrack(index, total):
      # check if the current index equals the length of the parameter list
      if index == len(list):
         # return 1 (a possible solution) or 0 (no solution) for this index
         return 1 if total == target else 0
      # check if this current (index, total) key appears in hashmap to prevent further processes
      if (index, total) in dp:
         # return the value for (index, total)
         return dp[(index, total)]
      # at this point, we then calculate all possible solutions recursively and store the sum into the (index, total) key in the hashmap
      dp[(index, total)] = (backtrack(index + 1, total + list[index]) + backtrack(index + 1, total - list[index]))
      # return the value after storing it to backtrack to previous call
      return dp[(index, total)]
   return backtrack(0, 0)

if __name__ == "__main__":
   print(target_sum([1,1,1,1,1], 3))
""" 
(0,0) -> (1, 1) + (1, -1) = 4 + 1 = 5
(1,1) -> (2, 2) + (2, 0) = 3 + 1 = 4 
(2, 2) -> (3, 3) + (3, 1) => 2 + 1 = 3
(3, 3) -> (4, 4) + (4, 2) => 1 + 1 = 2
(4, 4) -> (5, 5) + (5, 3) => (5, 5) -> 0 + => (5, 3) -> 1 = 1
(4, 2) -> (5, 3) + (5, 1) => (5, 3) -> 1 + (5, 1) -> 0 = 1
(3, 1) -> (4, 2) + (4, 0) => (4, 2) -> 1 + 0 = 1
(4, 0) -> (5, 1) + (5, -1) => 0 + 0 = 0
(2, 0) -> (3, 1) + (3, -1) = 1 + 0 = 1
(3, -1) -> (4, 0) + (4, -2) => 0 + 0 = 0
(4, -2) -> (5, -1) + (5, -3) => 0 + 0 = 0
(1, -1) -> (2, 0) + (2, -2) = > 1 + 0 = 1
(2, -2) -> (3, -1) + (3, -3) => 0 + 0 = 0
(3, -3) -> (4, -2) + (4, -4) => 0 + 0 =0
(4, -4) -> (5, -3) + (5, -5) => 0 + 0 = 0

"""