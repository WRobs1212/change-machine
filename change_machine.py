#easy start is to implement the beginning number of coins, and print total command.
#To keep it simple, each number of coin will just be named after the coin itself
quarter = round(25)
nickel = round(25)
dime = round(25)
dollar = 0
five_dollar = 0
# the round should keep the coinage exact.
#this import allows me to use quit() which shuts down the code so another user can use the machine.
import site

tally = (f'''machine has:
 {quarter} quarters
 {dime} dimes
 {nickel} nickels
 {dollar} dollars
 {five_dollar} five dollar bills ''')

print(tally)

#ask what the price of the item being purchased is and prompt until correctly inputed. price takes the input from the user.
# realPrice converts the user's input to a floating point and gets rid of the zero so it can be divided by 5 (because the decimal division sucks)
# iteration is just used to continue the while loop.
#displayPrice converts realPrice to an integer to make the division easier.
#If the price entered is anything other than a number the program fails.
#This should not matter because this is where the price is entered so the user would only be able to look at number (or q).


iteration = 0
while iteration == 0:
    price = input('What is the price of the item you are purchasing? Price must be a multiple of 5 cents and non-negative. (must enter price as xx.xx whether all digits are used or not). Type "q" to quit.')

    if price == 'q' :
                print('Have a good day.')
                print(f'''machine has:
                 {quarter} quarters
                 {dime} dimes
                 {nickel} nickels
                 {dollar} dollars
                 {five_dollar} five dollar bills ''')
                quit()

    realPrice = float(price) * 100
    displayPrice = int(realPrice)
    if (len(price)) == 5 and price[2] == '.' and displayPrice % 5 == 0 and not '-' in price :
        print('''Valid price.

        ''')
        break

    else:
        print('''Invalid price.

        ''')
        continue



#allows the user to insert each different kind of currency and eventually results in a completed transaction
while displayPrice > 0 :

    coin = input('''What legal tender would you like to insert?
    "qu" for quarter
    "n" for nickel
    "d" for dime
    "od" for one dollar
    "fd" for five dollar
    "q" to quit the program
    ''')
    print(coin)

#functions as the quarter counter and increments the machine's number of quarters as well as the displayPrice
    if coin == 'qu':
        print(' you inserted a quarter ')
        quarter = quarter + 1
        displayPrice = displayPrice - 25
        #checks to see if displayPrice is positive (money is still owed). If it is, finds the dollars due and the number of cents due.
        if displayPrice >= 0 :
            remainingDollars = displayPrice // 100
            remainingCents = displayPrice - remainingDollars * 100
            print('Balance due: ',remainingDollars, 'dollars and', remainingCents, 'cents')
        else :
            #checks to see if displayPrice is negative (money is paid and the machine owes the user money). If it is, finds the dollars due and the number of cents due.
            remainingDollars = -displayPrice // 100
            remainingCents = displayPrice + remainingDollars * 100
            print('Balance owed: ',-remainingDollars, 'dollars and', -remainingCents, 'cents')

#functions as the nickel counter and increments the machine's number of nickels as well as the displayPrice
#Practically the same as the quarter counter. remainingDollars and remainingCents are the same.
    if coin == 'n':
        print('you inserted a nickel')
        nickel = nickel + 1
        displayPrice = displayPrice - 5
        if displayPrice >= 0 :
            remainingDollars = displayPrice // 100
            remainingCents = displayPrice - remainingDollars * 100
            print('Balance due: ',remainingDollars, 'dollars and', remainingCents, 'cents')
        else :
            remainingDollars = -displayPrice // 100
            remainingCents = displayPrice + remainingDollars * 100
            print('Balance owed: ',-remainingDollars, 'dollars and', -remainingCents, 'cents')

#functions as the dime counter and increments the machine's number of dimes as well as the displayPrice
#remainingCents and remainingDollars are the same as above (and will continue to be until the end of this segment.)
    if coin == 'd':
        print('you inserted a dime')
        dime = dime + 1
        displayPrice = displayPrice - 10
        if displayPrice >= 0 :
            remainingDollars = displayPrice // 100
            remainingCents = displayPrice - remainingDollars * 100
            print('Balance due: ',remainingDollars, 'dollars and', remainingCents, 'cents')
        else :
            remainingDollars = -displayPrice // 100
            remainingCents = displayPrice + remainingDollars * 100
            print('Balance owed: ', -remainingDollars, 'dollars and', -remainingCents, 'cents')

#functions as the one dollar counter and increments the machine's number of ones as well as the displayPrice
    if coin == 'od' :
        print('you inserted a dollar')
        dollar = dollar + 1
        displayPrice = displayPrice - 100
        if displayPrice >= 0 :
            remainingDollars = displayPrice // 100
            remainingCents = displayPrice - remainingDollars * 100
            print('Balance due: ',remainingDollars, 'dollars and', remainingCents, 'cents')
        else :
            remainingDollars = -displayPrice // 100
            remainingCents = displayPrice + remainingDollars * 100
            print('Balance owed: ', -remainingDollars, 'dollars and', -remainingCents, 'cents')

#functions as the five dollar counter and increments the machine's number of fives as well as the displayPrice.
    if coin == 'fd' :
        print('you inserted five dollars')
        five_dollar = five_dollar + 1
        displayPrice = displayPrice - 500
        if displayPrice >= 0 :
            remainingDollars = displayPrice // 100
            remainingCents = displayPrice - remainingDollars * 100
            print('Balance due: ',remainingDollars, 'dollars and', remainingCents, 'cents')
        else :
            remainingDollars = -displayPrice // 100
            remainingCents = displayPrice + remainingDollars * 100
            print('Balance owed: ',remainingDollars, 'dollars and', -remainingCents, 'cents')

#allows the user to quit at any time
    if coin == 'q' :
        #double checks to ensure no accidents happen with a quarter command.
        quitPrompt = input('Are you sure you want to quit?"y" for yes, "n" for no.')
        if quitPrompt == 'y' :
            print('Have a good day!')
            quit()
        if quitPrompt == 'n' :
            continue

#there has to be a prettier way to do this, but after trying for an hour I could not get it and this works so here we are
#Checks to make sure that none of the allowable values have been entered, and if that is true, it repeats the loop after printing invalid coinage.
    if coin != 'qu':
        if coin != 'd':
            if coin != 'n':
                if coin != 'od':
                    if coin != 'fd':
                        print('invalid coinage.')
                        continue

#this allows the subtraction of available coins compared to unavailable ones.
returnPrice = displayPrice * -1


#this will trigger when the user inserts more money than necessary
while returnPrice > 0 :

#this triggers a) if quarters are available and b) if the return price is divisible by 25
#Essentially, the most valuable coins should always be dispensed first (if possible) so that the least total amount of coins is dispensed
    if quarter > 0 and returnPrice // 25 > 0 :
        quartersReturned = int(returnPrice // 25)
        #says that if there are more quarters needed than quarters available then the amount needed becomes the avalable amount and it gets subtracted from the total amount due. It also sets the availble quarters to zero.
        if quartersReturned > quarter :
            quartersReturned = quarter
            returnPrice = returnPrice - int(quartersReturned * 25)
            print(f'you get {quartersReturned} quarters back')
            quarter = 0
            continue
        else :
            #this is what happens when there are enough available quarters to satisfy the need, subtracting the used quarters from the stock.
            returnPrice = returnPrice - int(quartersReturned * 25)
            quarter = quarter - quartersReturned
            print(f'you get {quartersReturned} quarters back.')
            continue
#Again, dimes are second most valuable, so they are triggerd second to reduce total coins given back.
#The function of this block is the same as the previous block.
    if dime > 0 and returnPrice // 10 > 0 :
        dimesReturned = int(returnPrice // 10)
        if dimesReturned > dime  :
            dimesReturned = dime
            returnPrice = returnPrice - int(dimesReturned * 10)
            print(f'you get {dimesReturned} dimes back.')
            dime = 0
            continue
        else :
            returnPrice = returnPrice - int(dimesReturned * 10)
            dime = dime - dimesReturned
            print(f'you get {dimesReturned} dimes back.')
            continue
#nickels are least valuable, so they should be triggered last.
#functions the same as the previous two blocks
    if nickel > 0 and returnPrice // 5 > 0 :
        nickelsReturned = int(returnPrice // 5)
        if nickelsReturned > nickel :
            nickelsReturned = nickel
            returnPrice = returnPrice - int(nickelsReturned * 5)
            print(f'you get {nickelsReturned} nickels back.')
            nickel = 0
            continue
        else :
            returnPrice = returnPrice - int(nickelsReturned * 5)
            nickel = nickel - nickelsReturned
            print(f'you get {nickelsReturned} nickels back.')
            continue

#shows user how much money they get in return if the machine does not have enough change (triggers last).
    if returnPrice > 0 :
        #owedDollars and owedCents function similarly to remainingDollars and remainingCents.
        owedDollars = returnPrice // 100
        owedCents = returnPrice - owedDollars * 100
        print(f"you must collect {owedDollars} dollar(s) and {owedCents} cents from a store manager. Have a nice day!")
        returnPrice = 0
        break
#prints the contents of the machine
print(f'''machine has:
 {quarter} quarters
 {dime} dimes
 {nickel} nickels
 {dollar} dollars
 {five_dollar} five dollar bills ''')
