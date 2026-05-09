num = int(input("Enter a number: "))
order = len(str(num))  
temp = num
arm_sum = 0

while temp > 0:
    digit = temp % 10          
    arm_sum += digit ** order  
    temp //= 10                

if num == arm_sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
