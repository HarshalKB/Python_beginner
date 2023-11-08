from os import system

logo = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = {}
flag = True
while flag:
    name = input('What is your name? ')
    bid = int(input("What's your bid? "))
    bids[name] = bid
    again = input('Are there any other bidders? type "yes" or "no"').lower()
    if again == 'yes':
        system("clear")
        print(logo)
    else:
        flag = False

m_name, m_bid = '', 0

for key, value in bids.items():
    if value > m_bid:
        m_name = key
        m_bid = value
system("clear")
print(f'The winner is {m_name} with a bid of ${m_bid}.')
