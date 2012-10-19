miniature_pricer
================

Minature Pricing Server

This is a sample project for Regentmarket Markets Group company recruitement process.

For purpose of the test, assume a system that accepts following parameters and generate a price as decribed bellow. 

F = S * e ^ (r*t)

F : Future Contract
S : Current spot price, you will receive it from a third party provider in a realtime manner.
t: time in year for finding future price.
r : Annualized Interest rate. It is defined based on the following table

Day  | Rate
-----------
1    | 10%
30   | 5%
60   | 4%
90   | 2%
210  | 2

To find interest rates that are not in the table use interpolation.

For example:

Future contract if current price is 10 in thirty days is 

F = 10 * e ^ (5/100 * 30/365)


goal
================
Build a pricing server that can accept the required parameters and generate price.
The format to get data or to providing output is up to you.

Say you need to regularly send pricing parameters from a central server to 40 different
servers around the globe. Suggest a solution to this problem.