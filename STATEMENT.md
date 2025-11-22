**Project Statement — Currency Converter** 

1\. Problem Statement



People deal with different currencies in daily life, especially students, travelers, and online shoppers.

Checking exchange rates and converting amounts manually can be confusing and may lead to calculation mistakes.

To make this easier, I decided to create a small Python program that can convert one currency to another quickly.



2\. Scope of the Project



This project is made only with the basic concepts taught in the course.

The main focus is on:



&nbsp;-Using Python functions

&nbsp;-Storing exchange rates in a NumPy array

&nbsp;-Converting any amount using simple indexing

&nbsp;-Taking user input and showing the result clearly



The project does not include advanced features like API calls, GUI, or database storage.

It is kept simple on purpose to match the basic Python + NumPy syllabus.



3\. Target Users

The program can be useful for:

&nbsp;-Students who want quick currency conversion

&nbsp;-Beginners learning Python and NumPy

&nbsp;-Anyone who needs a simple conversion tool



4\. High-Level Features

&nbsp;-Currency Selection

&nbsp;	The user can choose the “from” and “to” currencies.

&nbsp;	Supported currencies: INR, USD, EUR, GBP, AUD, CAD, JPY, CNY.



&nbsp;-NumPy-Based Rate Matrix

&nbsp;	All the exchange rates are stored inside a NumPy 2D array.

&nbsp;	This makes the conversion fast and easy.



&nbsp;-Conversion Logic

&nbsp;	The program multiplies the entered amount with the correct rate from the matrix:

&nbsp;	converted\_amount = amount \* rate\[from\_index]\[to\_index]



5\. Summary



This project shows how Python and NumPy can be used to build a simple currency converter.

It is easy to understand, works without the internet, and helps in practicing basic programming concepts.

The project is suitable for a beginner-level Python course and demonstrates practical use of NumPy arrays.

