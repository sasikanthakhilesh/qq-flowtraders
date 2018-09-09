##################################################################################
##################################################################################
## Template file for problem 1. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
#Suppose Dice is having 2 sided No.of roles =(1/2)*1+(1/1)1
#Expected Sum=(1/2)*1
#lets suppose its a fair dice of 3 sides. then expected value for one roll will be   
#E(X=3) = 1* (1/3) + 2*(1/3) + 3*(1/3) = 2   
#hence average sum when dice of 3 side is rolled comes out to be 2. 
#
#
##################################################################################
##################################################################################
## You have to fill in two functions BELOW 					##
## Both take in input n = number of sides in the die 				##
## 										##									##
## 1. findSumDieRoll(n)	: Return expected value of sum 				##
## 2. findNumberOfRolls(n)  : Return expected value of number of rolls 		##
## 										##									##
## For both, you only have to fill in the math function where indicated     	##
## 										##									##
## You can run this template file to see the output of your functions       	##
## for a 6 sided die.								##
## Simply run: `python problem1_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################


def findSumDieRoll(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	sumRolls = 0 # Replace me with your answer\
	i = 0
	while(i < n)
	sumRolls = sumRolls + (i+1)/(n-i)
	i = i+1

	return round(sumRolls, 2)
def findNumberOfRolls(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	numRolls = 0 # Replace me with your answer\
	i = 0
	while(i < n)
	numRolls = numRolls + 1/(n-i)
	i = i+1

	return round(numRolls, 2)

if __name__ == "__main__":
	numberOfSides = 6.0
	sumOfRolls = findSumDieRoll(numberOfSides)
	numberOfRolls = findNumberOfRolls(numberOfSides)
	print('For a %i-sided die, expected value of sum: %.2f and number of rolls: %.2f'%(numberOfSides, sumOfRolls, numberOfRolls))
