Currency Converter

This is a simple currency converter program made using Python 
main idea of the project is to take an amount in one currency and convert it into another currency. 
The project is built only with the basic concepts teach in class.

---

 1. Project Overview
The program allows the user to:
- Enter the amount of money you want to convert
- Select the currency you want to convert from
- Select the currency you want to convert to  
- we will get output immediately

array is used to store all the exchange rates, and the program uses simple indexing to fetch the correct value.

---

 2. Features
- Supports only 8 currencies  
  INR, USD,EUR,GBP,AUD,CAD,JPY,CNY  
- Uses a NumPy matrix for conversion  
- if you gave wrong currency code it does not proceed further  
- negative or invalid output is not allowed

---

 3. Technologies Used
- Python 3
- NumPy
- Basic programming concepts:
   functions,loops,conditional,arrays

---

6. How It Works
 -user selects two currencies.
 - program detects the correct exchange rate using NumPy indexing.
 - the amout you write is multiply with the rate
 - converted value is shown on the terminal

7. Limitations
 -Rates of the currency are fixed
 -their is no graphical interface
 - only 8 currencies included

8. Future Improvements
 -Add live exchange rates using an API
 -Add a GUI using Tkinter
 -Add more currencies

