def solve_knapsack(profits, weights, capacity):
	return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, currentIndex):
	if capacity <= 0 or currentIndex >= len(profits):
		return 0

	# recursive call after choosing the element at the currentIndex
	# if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
	profit1 = 0
	if weights[currentIndex] <= capacity:
		profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, 
			capacity-weights[currentIndex], currentIndex+1)

	# recursive call after excluding the element at the currentIndex
	profit2 = knapsack_recursive(profits, weights, capacity, currentIndex+1)

	return max(profit1, profit2) 



print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))



