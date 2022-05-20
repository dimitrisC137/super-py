The program begins with the appropriate libraries being imported. What is very important is that the files of inventory, sold, and dates need to be created for this program to run correctly. 
About the csv files, there are only two, because on the inventory file the products can be added (with the buy function) and stored there. When the user tries to sell an item, the program first checks the inventory for availability before confirming that the requested product can actually be sold. There lies the biggest personal challenge of the whole project, connecting the csv files with each other and the command-line. While commands such as "income" are relatively simple. 
The parser code is as simple in comparison as well. It just connects every available command with the appropriate function.

All functions are accompanied by comments. This next section shows the key words that are used and what they mean relative to the project from a technical standpoint.
These key words are:

Add - addition, this type of function finds and puts together all the required information, using the mathematical function. ask-requires an input from the user

Calculate - a more complex mathematical equation, the lines of code need to be read in order for the exact details to be understood

Check - a background operation that the program will do, none of the results will be shown to the user, these are used in order to brake down complex operations into a single value,many main or project functions have values that translate to many of these functions. 

Count- simply counting of amount of anything that is needed

Create - makes a new file or value for a file

Get - another background operation, this type of function finds data from other parts of the code, none of the findings are shown to the user, these operations is very important and connects multiple other functions that could not operate otherwise

The functions that are directly connected to the parsers are:

Main - the single function that connects all information in one place, typickly it will show some text to the user and wait for a response

Project - shows the user directly the information they want, it is a combination of other information but does not need input from the user.