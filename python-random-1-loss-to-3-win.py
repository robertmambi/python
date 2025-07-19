import random

# This is sample demo
# si ta trade 10 pip loss vs 20 pip win
# randomize win/loss 
# Account = 1000


month_stop = 12  # Number of months
day_stop = 100 # Number of loops
Account  = 50000
loss = 1
win  = 1.5
win_trade  = 0
loss_trade = 0
win_rev_total  = 0
loss_rev_total = 0
percentage = 0.01  # 1% of the account
Account_start = Account
trans_cost = 0.1
Account_saving = 0
Account_end = 0
trans_cost_total = 0
loss_rev = 0
win_rev = 0


for j in range(month_stop):
    if Account < 500:
        print(f"Account is too low to continue trading. Month {j+1}: Account = {Account:.2f}")
        break  
    if Account > (Account_start+100):
        Account_saving += Account - Account_start
        print(f"Month {j}: Account = {Account:,.2f} Account-Diff = {(Account - Account_start):,.2f} Account-Saving = {Account_saving:,.2f}")
        Account = Account_start  # Reset account to start for next month
    else:
        print(f"Month {j}: Account = {Account:,.2f} Account-Diff = {(Account - Account_start):,.2f} Account-Saving = {Account_saving:,.2f}")
            
    for i in range(day_stop):
        loss_rev = Account * percentage * loss
        win_rev  = Account * percentage * win
        trans_cost = loss_rev * 0.1
        # result = random.choice([True, False])
        result = random.random() < 0.40
        if result:
            Account += win_rev
            Account -= trans_cost
            win_trade += 1
            win_rev_total += win_rev
            # print(f"Loop {j+1}:{i+1}: {result} :win_rev  = {win_rev:.2f}  Account = {Account:.2f} trans_cost = {trans_cost:.2f}")
        else:
            Account -= loss_rev
            Account -= trans_cost
            loss_trade += 1
            loss_rev_total += loss_rev
            # print(f"Loop {j+1}:{i+1}: {result} :loss_rev = {loss_rev:.2f} Account = {Account:.2f} trans_cost = {trans_cost:.2f}")
        
        trans_cost_total += trans_cost
    Account_end = Account

    # print(f"""
    # Loop {j+1}
    # Account Start = {Account_start:.2f}
    # Account End   = {Account_end:.2f}
    # Total Win  Trades: {win_trade}
    # Total Loss Trades: {loss_trade}
    # Total Trades     : {loss_trade+win_trade}
    # Total Win  Revenue: {win_rev_total:.2f}
    # Total Loss Revenue: {loss_rev_total:.2f}
    # Final Account Balance: {Account_end:.2f}
    # Win Percentage:  {win_trade  / (win_trade + loss_trade) * 100:.2f}%
    # Loss Percentage: {loss_trade / (win_trade + loss_trade) * 100:.2f}%
    # Account Change: {(Account_end-Account_start):.2f}
    # Account Saving: {Account_saving:.2f}
    # """)  

print(f"""
Account Start = {Account_start:,.2f}
Account End   = {Account_end:,.2f}
Account Change: {(Account_end-Account_start):,.2f}
loss_rev      : {loss_rev:,.2f}
win_rev       : {win_rev:,.2f}

Total Win  Trades: {win_trade}
Total Loss Trades: {loss_trade}
Total Trades     : {loss_trade+win_trade}
Win Percentage:  {win_trade  / (win_trade + loss_trade) * 100:,.2f}%
Loss Percentage: {loss_trade / (win_trade + loss_trade) * 100:,.2f}%

Total Win  Revenue: {win_rev_total:,.2f}
Total Loss Revenue: {loss_rev_total:,.2f}
trans_cost_total  : {trans_cost_total:,.2f}
Account Saving    : {Account_saving:,.2f}


""")
