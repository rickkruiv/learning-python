def multiplication_or_sum(num1, num2):
    product = num1 * num2
    
    if product <= 1000:
        return product
    
    else:
        return num1 + num2

result = multiplication_or_sum(20, 30)
print('The result is', result)

result = multiplication_or_sum(40, 30)
print('The result is', result)

num1 = int(input('Put a number: '))
num2 = int(input('Put another number: '))

result = multiplication_or_sum(num1, num2)
print('The result is ', result)