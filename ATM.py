answer = '1234'

counter = 0


while True:
    guess = input('Please enter your 4-digit PIN: ')
    if guess == answer:
        print('Your bank account is loaded!')
        break

    if guess != answer: #Reject any type of input that is not the answer
        print('Invalid PIN.  Please try again.')
        counter += 1

    if counter ==3: #Three attempts
        print('Account locked. Nice Try.')
        counter += 1
        break
