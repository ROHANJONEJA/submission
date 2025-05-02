#Defining a fucntion for the given problem statement
def palindrome(number):
    
    """
    This function checks if the given integer is a palindrome.
    """

    #Negative numbers cannot be palindromes
    if number<0:
        return False

    #All single digit numbers are palindromes
    elif 0<=number<10:
        return True

    #Converts the number to a string 
    else:
        numstr=str(number)

        #Checking if the reverse of the number matches the orignal number
        for i in range(len(numstr)//2):
            if numstr[i]!=numstr[len(numstr)-i-1]:
                return False
        return True 

#Sample
#Using try-except to eliminate errors which might occur after taking the input from the user
try:
    sample=int(input("Enter an integer: "))
    #calling the previously defined function to check if it's a palindrome or not
    if palindrome(sample):
        print("True")
    else:
        print("False")
#to communicate about any value error to the user 
except ValueError:
    print("Please enter a valid integer.")

#ROHAN JONEJA 12-C
#I have written the program in a quite elaborate manner as per the instructions given in the prompt.
#The same can also be written in a shorter way.


    
