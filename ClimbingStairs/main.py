""" 
Bottom up solution

Starting at 0 and up to n=5
index: 0, 1, 2, 3, 4, 5
dp:   [8, 5, 3, 2, 1, 1] //Number of possible ways it takes to reach the specific index
"""
def climbing_stairs(n):
   """ Define the base case variables """
   one, two = 1, 1
   """ loop through n-1 times to calculate the final number of steps """
   for _ in range(n-1):
      """ continuously update variables one and two """
      temp = one
      one = one + two
      two = temp
   return one

""" Min-Cost Climbing Stairs """
def min_cost_climbing_stairs(costs):
   """ append a 0 for two-variable sliding window """
   costs.append(0)
   """ loop costs list in reverse starting from the third to last element """
   for i in range(len(costs) - 3, -1, -1):
      costs[i] += min(costs[i+1], costs[i+2])
   """ Return the min between the first two elements of the array because starting points are 0 and 1 """
   return min(costs[0], costs[1])   

def main():
   print(climbing_stairs(6))

if __name__ == "__main__":
   print(min_cost_climbing_stairs([10, 15, 2, 5, 17]))