#This function is used to query the textual rating in GFC json result to give a numerical probability value for the query
#This return value of this function is the classification and the probability of the classification. In line with ALICE format.


#Default value of result is unclassified and probability is 1; querystr is textualRating from GFC json result
res = 0 
pr = 1
querystr = input("Enter textual rating: \n")

true_set = {"True", "true", "Correct", "correct"}
false_set = {"False", "false", "Incorrect", "incorrect", "Inaccurate", "inaccurate","Pants on fire", "Outdated", " Four Pinocchios" }
inaccurate_set = {"Missing Context", "Needs Context", "biased", "unsupported", "misleading", "Half True", "Half truth", "exaggerated" }

if querystr in~ true_set:
    res = 1
elif querystr in~ false_set:
    res = 2
elif querystr in~ inaccurate_set:
    res = 2
    pr =  0.5


print("Classification: \t", res )
print("Probability: \t", pr)

    