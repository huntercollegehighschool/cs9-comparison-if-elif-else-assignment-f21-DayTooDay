'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
number_3 = int(input("Enter another number: "))

if number_1 <= number_2:
  smallest = number_1
elif number_2 < number_1:
  smallest = number_2

if number_3 < smallest:
  smallest = number_3
  
print("\nThe smallest number is ", smallest)
