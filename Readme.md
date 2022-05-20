User Manual.

**Welcome ,**

The project is devided into eight parts. 
In order for the process to be as smouth as possible, it is advised to run the following three .py programs first:

*date.py, inventory_creator.py , sold_creator.py*

This step creates the files that all data are stored. Their contents are:

*date.py*- The date of the user's current date

*inventory.py* details of all products are stored

*sold_creator.py* - All the details of sells are stored

After this step the user should just begin with the main.py program. The first time all programs are installed, it is adviced to run the program (main.py) to check for any errors before trying to use the command tool. If everything is in order, then this message will be projected:
```
usage: main.py [-h]
              
              {advancedate,income,incomedates,buy,sell,check} ...   

main.py: error: the following arguments are required: command-line
```
This confirms that there are no errors in both main.py and all other programs. As an adddition, all available commands are also projected in curly ({ }) brackets.

If the user enters the [-h] command, they will be greeted with this message:
```
Welcome to the supermarket.

positional arguments:
  
  {advancedate,income,incomedates,buy,sell,check}
   
   advancedate         Advance the date a number of days.
   
   income              Show all income ever received.
    
   incomedates         Show all income between two dates.
    
   buy                 Buy a product and add it on the inventory.
    
   sell                Sell a product and add a the transaction details on the 'sold' list.
    
   check               Shows all inventory.

optional arguments:
  
  -h, --help            show this help message and exit
```
Next, the user may enter one of the six available commands. The following is an example of how a command can and should be entered on the terminal:
```
python3 main.py [command]
```
The meanings behind all available commands are:

*advancedate* - The user is greeted by text that asks for a number. That number will be the amount of days that the date will advance once entered.

*income* - The user is showed all income from all sold products, regardles of date.

*incomedates* - The user is greeted by text that asks for two different dates. Afterwards, the income between these two days will be projected.

*buy* - The user ia able to add a product on the inventory by adding all its details. Such as the name, quantity, buying price and expiration date.The id number will be created automatically.

*sell* - The user ia able to sell a product.The transaction details are saved on the 'sold' list. If the product exists, then the some details need to be filled. Such as the name, quantity and selling price.The id number will be created automatically, also the inventory id of the product will be automatically filled.

*check* - Projects all available inventory regardles of date or quantity.

A complete example of a correctly added command and it's output is:
```
python3 main.py income

The total income is: 2.1 euro

Have a nice day!
```

**Thank you for using super.py!**
