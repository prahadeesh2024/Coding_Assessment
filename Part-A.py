Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]

# 1) Finding the total possible combinations
total_combinations = len(Die_A) * len(Die_B)
print("Total combinations possible:", total_combinations)

#--------------------------------------------------------------------------------------------------------------------------#

# 2) Finding The distribution of all possible combinations that can be obtained when rolling both DieA and DieB together
combination_distribution = [[0] * 6 for _ in range(6)]#This creates 6 array with [0,0,0,0,0,0]
for i in range(6):
    for j in range(6):
        combination_distribution[i][j] = Die_A[i] + Die_B[j]#Adding both arrays
#print(combination_distribution[2][5])
print("\nCombination distrubution on rolling both the Dies")
for row in combination_distribution:
    print(row)

#--------------------------------------------------------------------------------------------------------------------------#

# 3) Finding the Probability of the sum of all possible combinations 
def prob(DieA, DieB):
    combinations = []
    for i in Die_A:
        for j in Die_B:
            c = i + j 
            combinations.append(c)
    
    count = {}
    probabilities = {}
    for i in combinations:
        count[i] = count.get(i, 0) + 1 #This checks for same values based on their frequency in the combinations list and adds them to the count dictionary.
        

    for i in range(2, 13):
        count_i = count.get(i, 0)
        probability_i = count_i / len(combinations)
        probabilities[i] = {"Value": i, "occurrence": count_i, "Probability": round(probability_i,4)}
    return probabilities

probability = prob(Die_A, Die_B)
print("\n\nProbability:")
for i in probability.values():
        print(i)