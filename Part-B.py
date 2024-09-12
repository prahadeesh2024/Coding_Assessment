#Finding the Total no of combinations(Same as Part-A(1))
def combinations():
    Die_A = [1,2,3,4,5,6]
    Die_B = Die_A.copy()
    count = 0
    for i in Die_A:
        for j in Die_B:
            count += 1
    return count# Total number of combinations 

#Finding the probability of the sum of all possible combinations (Same as Part-A(3))
def prob(DieA, DieB):
    combinations = []
    for i in DieA:
        for j in DieB:
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

#Umdooming the dice
def undoom_dice(Die_A, Die_B):
    
    New_Die_A=[]
    New_Die_B=[]
    for i in Die_A:
        if i> 4: # As in question "No New_Die A[x] > 4"
            New_Die_A.append(i-3)
        else:
            New_Die_A.append(i)
    for i in Die_B:
        if i % 2 == 0: # "Even" because desired output doesn't results in Odd
            New_Die_B.append(i+2)
        else:
            New_Die_B.append(i)
    return sorted(New_Die_A), sorted(New_Die_B)

def main():
    DieA = [1, 2, 3, 4, 5, 6]
    DieB = [1, 2, 3, 4, 5, 6]
    
    original_probabilities = prob(DieA, DieB)
    New_Die_A, New_Die_B = undoom_dice(DieA, DieB)
    modified_probabilities = prob(New_Die_A, New_Die_B)

    ###Original probabilities###
    print("\nOriginal probability:")
    for i in original_probabilities.values():
        print(i)

    #Undoomed Dies
    print('\n Undoomed Dies\n A-', New_Die_A, '\n B-', New_Die_B)# printing the Undoomed dice
    
    ####modified probabilities###
    print("\nModified probability:")
    for i in modified_probabilities.values():
        print(i)

    # Check if probabilities remain the same after adjustment
    if original_probabilities == modified_probabilities:
        print("\n Probabilities remain the same after adjustment.\n")
    else:
        print("\n Probabilities change after adjustment.\n")

if __name__ == '__main__':
    main()