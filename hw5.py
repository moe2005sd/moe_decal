#Question 1

#1. pwd
#2. ls
#3. cd ../brianna_repo
#   git pull origin main
#4. cp homework.py ../judy_decal/homework
#5. cd ../judy_decal/homework
#   nano homework.py
#6. Edit directly in the page jumped out.
#7. ^X to exit, Y to save, return(or enter) to go back to the original terminal page
#   git add .
#   git commit -m "Adding homework.py"
#   git push origin main
#8. git pull origin main
#   git push origin main
#   Judy pushed new changes to the remote repository before updating the local copy. Judy needs to sync the local repository with the latest changes before pushing new files.
#9. cd ~/Recents


#Question 2

#2.1
def checkDataType(x):
    print(type(x).__name__)

checkDataType(3.14)
checkDataType(True)

#2.2
def evenOrOdd(n):
    if n % 2 == 0:
      print("Even")  
    else:
      print("Odd")

evenOrOdd(7)
evenOrOdd(10)


#Question 3
def sumWithLoop(nums):
    total = 0
    for i in nums:
        total += i
    print(total)

numbers = [1, 2, 3, 4, 5]
sumWithLoop(numbers)


#Question 4

#4.1
def duplicateList(list):
    new_list = []
    for i in list:
        new_list.append(i)
        new_list.append(i)
    print(new_list)

duplicateList(['a', 'b', 'c'])

#4.2
#There's a ":" missing at the end of the first line. It should be:
def square(num):
    return num * num
