more_bidders = True
bidders = {}
print('Welcome To Blind Auction!')
while more_bidders:
    def name_bid():
        name = input('What is your name? ')
        bid = int(input('What is your bid amount? $'))
        bidders[name] = bid


    name_bid()
    anybody_else = input("Are there any other bidders? Type 'Yes' or 'no'")

    if anybody_else == 'no':
        more_bidders = False
        bid_amount = 0
        for key in bidders:
            bidders[key] > bid_amount
            bid_amount = bidders[key]
        print(f'The winner is {key} with a bid of ${bid_amount}.\nThanks for participating.')
