print("1. Pythagorean theorem")
# A right angled triangle has the catheti: a = 3 and b = 4 length units. Compute the hypothenuse of the triangle. (*)
a = 3
b = 4
c = (pow(a,2)+pow(b,2))**0.5
print'a) If a=3 and b=4, then c=', c
#A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. Compute the other cathetus and round to one decimal. (*)

c = 7 
a = 5
b = (pow(c,2)-pow(a,2))**0.5

print'b) If c=7 and a=5, then b=', b
print'\b'

print'2. Classification accuracy'
#A machine learning algorithm has been trained to predict whether or not it would rain the next day. Out of 365 predictions, it got 300 correct, compute the accuracy of this model.

daysOfTheYear = 365
accurateDays = 300
accuracy = 100*accurateDays/daysOfTheYear

print'Having ',accurateDays,' accurate out of ',daysOfTheYear,' days means the prediction algorithm has ',accuracy, '% accuracy'
print'\b'
print'3. Classification accuracy'


TP = 2
FN = 2
FP = 11
TN = 985
accuracy = (100*(TP+TN))/(TP+TN+FP+FN)

if (accuracy>95):
    print'The accuracy is',accuracy,'% and this is a good model'
else :
    print'The accuracy is',accuracy,'% and this is a bad model'

print'\b'
print'4. Line'

A=(4,4)
B=(0,1)
k=float(A[1]-B[1])/float(A[0]-B[0])

print'The slope k of this line is equal to',k

m=round((0-A[1])/k + (A[0]),2)
print'The constant term m of this line is equal to ',m

print'\b'







