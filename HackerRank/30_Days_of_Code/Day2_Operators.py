'''Day 2 : Operators
Objective 
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are  lines of numeric input: 
The first line has a double,  (the cost of the meal before tax and tip). 
The second line has an integer,  (the percentage of  being added as tip). 
The third line has an integer,  (the percentage of  being added as tax).

Output Format
Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).

Sample Input
12.00
20
8
Sample Output
15'''

meal_cost=float(input("meal cost"))
tip= int(input("tip"))/100
tax= int(input("tax"))/100
total_cost= meal_cost + (tip*meal_cost) +(tax*meal_cost)
print(int(round(total_cost,0)))# Rounds to the nearest greatest value .eg.12.5 to 13.0

'''
Compiler Message
Success
1.
Input (stdin)
12.00
20
8
Expected Output
15

2.
Input (stdin)
10.25
17
5
Expected Output
13

3.
Input (stdin)
15.50
15
10
Expected Output
19

