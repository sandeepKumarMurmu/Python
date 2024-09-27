'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	
    str : x = "Hello World"

Numeric Types:	
    int : x = 1
    float : x = 1.0
    complex : x = 1j

Sequence Types:	
    list : x = [1, 2, 3, 4]  
    tuple : x = (1, 2, 3, 4)
    range : x = range(4)

Mapping Type:	
    dict : x = {"name" : "John", "age" : 36}

Set Types:	
    set : x = {"apple", "banana", "cherry"} 
    frozenset : x = frozenset({"apple", "banana", "cherry"})

Boolean Type:	
    bool : True
Binary Types:	
    bytes : x = b"Hello"
    bytearray : x = bytearray(5)
    memoryview : x = memoryview(bytes(5))

None Type:	
    NoneType : none
'''


'''
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:

Example	                                            Data Type	
x = str("Hello World")	                            str	
x = int(20)	                                        int	
x = float(20.5)	                                    float	
x = complex(1j)	                                    complex	
x = list(("apple", "banana", "cherry"))	            list	
x = tuple(("apple", "banana", "cherry"))	        tuple	
x = range(6)	                                    range	
x = dict(name="John", age=36)	                    dict	
x = set(("apple", "banana", "cherry"))	            set	
x = frozenset(("apple", "banana", "cherry"))    	frozenset	
x = bool(5)	                                        bool	
x = bytes(5)	                                    bytes	
x = bytearray(5)	                                bytearray	
x = memoryview(bytes(5))	                        memoryview
'''