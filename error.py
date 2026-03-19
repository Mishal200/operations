# exception handling
try:
    n=int(input('Enter a number: '))
    is_divisible=100%n==0
    print(x)
# except valueError as e:
#     print(e)
#     print('Invalid input.please enter a valid number')
# except ZeroDivisionError:
#     print('Number should not be zero.')
except (ValueError,ZeroDivisionError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    if is_divisible:
        print(f'{n}is a factor of 100.')
    else:
        print(f'{n} is not a factor of 100.')
finally:
    print('Exception handling completed.')