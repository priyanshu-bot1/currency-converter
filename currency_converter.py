import numpy as np
currencies = ["INR", "USD", "EUR", "GBP","AUD","CAD","JPY","CNY"]

rates = np.array([
    [1,0.012, 0.011,0.0097,0.018,0.016,1.78,0.087],
    [83,1,0.93,0.81,1.56,1.36,147.5,7.22 ],
    [90,1.07,1,0.87,1.68,1.47,158,7.75 ],
    [103,1.23,1.15,1,1.93,1.7,182,8.92 ],
    [56,0.64,0.59,0.52,1,0.88,94.3,4.62 ],
    [62,0.74,0.68,0.59,1.13,1,107.2,5.15 ],
    [0.56,0.0068,0.0063,0.0055,0.0106,0.0093,1,0.048],
    [11.45,0.138,0.129,0.112,0.216,0.194,20.9,1]
])


def convert(amount, from_curr, to_curr):
    i = currencies.index(from_curr)
    j = currencies.index(to_curr)
    return amount * rates[i][j]


print("Available Currencies: INR, USD, EUR, GBP, AUD, CAD, JPY, CNY")

From =input("Convert from: ").upper()
to = input("Convert to: ").upper()

amt = float(input("Enter amount: "))
if amt>=0:
    result = convert(amt, From, to)
    print(amt,From,'=',result,to)
else:
    print("amount cannot be negative")