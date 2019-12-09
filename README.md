# Open, reading, writing files & error handling

## Topics covered:
- Open()
- Try * Except
- With & Finally
- Exceptions and error handling

        ````
        "All that can go wrong, will go wrong"
        ````

        

## Definitions
- Exceptions: These occur when an error occurs
- Error Handling: Assuming things will break (Murphy's law), handling your errors when they do.
                   Providing adequate feedback wile failing with grace. When handling erros
                   code can continue to run
- Try: / Except: / Finally:   These blocks of code are used in conjunction to error handle

````
try:
    file = open("orders.txt")
except:
    print('Check file name &/or path - file cannot be found')
````

- Using open() with with():  'with open()' means the file is opened and closed for you and no 
                             need for close()
````
with open(<filename>, <option>) as <placeholder>:
    <placeholder>.readlines()