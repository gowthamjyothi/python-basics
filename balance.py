balance=1000
while balance>0:
  amount=int(input(f"enter tne amount to withdraw"))
  if amount==0:
    print("enter a valid amount")
    continue
  if amount > balance:
    print("insufficient balance")
  else:
    balance=balance-amount
    print(f"your withdrawl of {amount} is sucessful")
    print(f"you have {balance} in your account ")