class MyClass:

    def __init__(self):
        print('__init__ is the constructor for a class')

    def __del__(self):
        print('__del__ is the destructor for a class')

    def __enter__(self):
        print('__enter__ is for context manager')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ is for context manager')

    def greeting(self):
        print('hello python')


'''
$ python3 class.objects_instantiation.py
__init__ is the constructor for a class
__enter__ is for context manager
hello python
__exit__ is for context manager
__del__ is the destructor for a class
'''
# define a class
import tkinter as tk

import idlelib.tree
class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
class Bike:
    """ define a class """
    name = ""
    gear = 0
    def __init__(self, name="MntBike", gear=10):
        self.name = name
        self.gear = gear

class Example:
    def __init__(self):
        self._internal = 2
        self.external = 20
        print(f"#16 leading_ 4 internal use only: {self._internal=}, {self.external=}")
    def useVars(self):
        pass
class array:
    N=[]
    aNt = 0

    def __init__(self, name='Brice', age=42):
        self.name = name
        self.age = age

    def remove_last(self, N, i=-1):
        del N[i]
        return N
        
    def build():
        pass
    def sumNum(self,G):
        return sum(G)
        '''         From         f"C:/Users/Brice/source/repos/Macroxue/freecell-master/solver/array.h"        '''
        #The **'return'** statement in **C++** serves two primary purposes:
pop='''
1. **Exiting a Function**: 
        When encountered within a function, the 'return' statement immediately **terminates the function execution** and returns control to the calling code. It can be used without any conditional statements. As soon as the `return` statement is executed, the flow of the program stops, and the function exits.
    
2. **Returning a Value**: If you want the function to **return a value**, you can specify a data type (such as 'int', 'string', etc.) instead of 'void' in the function signature. Inside the function, use the 'return' keyword followed by an expression or value. For example:
            #cpp
                    int myFunction(int x) {     return 5 + x;    }
                    int main() { cout << myFunction(3); // Outputs 8 (5 + 3);  return 0;    }
            #        In the example above, the 'myFunction' returns the result of '5 + x', which is '8' when called with 'x = 3'.         Remember that the expression after `return` must be convertible to the function's return type.        Feel free to ask if you have any more questions about C++ or programming! 😊        Source: Conversation with Bing, 3/23/2024        (1) C++ Functions - Return - W3Schools. https://www.w3schools.com/cpp/cpp_function_return.asp.        (2) return statement - cppreference.com. https://en.cppreference.com/w/cpp/language/return.        (3) return statement in C++ with Examples - GeeksforGeeks. https://www.geeksforgeeks.org/return-statement-in-cpp-with-examples/.    
    '''
    
    
if __name__ == '__main__':
    with MyClass() as mycls:
        mycls.greeting()

    #with array() as n1:
    #    n2 = range(1,7)
    #    n1.remove_last(n2,-1)
    #    print(n1)

    print(f"{pop}")
    # create object of class
    bike1 = Bike("Mountain Bike1", 17)
    print(f"bike1 = Name: {bike1.name}, and Gears: {bike1.gear} ")

    # access attributes and assign new values
    bike1.gear = 11
    bike1.name = "Mountain Bike2"
    print(f"bike1 = Name: {bike1.name}, and Gears: {bike1.gear} ")

    ledzep = ["Pepsi", "Dr. Pepper", "Strawberry", "Grape", "Orange"]
    print(ledzep)
    anArray = array()
    anArray.remove_last(ledzep)
    print(ledzep)
    
    # #1 Slicing    def pop():    
    hW = "Hello World!"
    print(f"#01 Slicing relies on indexing. OG{hW=},sliced={hW[::-1]=}")
    
    """
    !dlroW olleH
    Slicing is a feature in Python that relies on indexing to allow users to access a subset of a sequence. 
    An index is simply the position of an element in a sequence. If the sequence type is mutable, 
    you can use slicing to extract and modify data. 
    Note: We may also use slicing on an immutable sequence, but trying to modify the slice will raise a TypeError. 
    The format in which slices are implemented is: sequence[start:stop:step]. 
    If no values are specified in the start, stop, and step parameters, then the sequence will implement the defaults. 
    The defaults are: 
    "start" defaults to 0 
    "stop" defaults to the length of the sequence
    "step" defaults to 1 if they are not specified. 
    When provided with sequence[start:stop] the elements returned will be from the starting index up to the stop - 1 (the stop index is not included). 
    We can also pass negative indices, which may be used to reverse the sequence. 
    For example, in a list of 4 elements, the 0th index is also the -4 index, and the last index is also -1. 
    In the example code above, this knowledge was applied to the step parameter of the sequence. 
    Consequently, the string was printed backward, starting from the end of the sequence to index 0.   
    """
    
    #2 Inplace Swap / Simultaneous Assignment
    
    a = 10
    b = 5
    print(f"#02 Inplace Swap / Simultaneous Assignment First: {a=}, {b=}",end=",    ")
    
    """
    First: (10, 5)
    """
    
    xxx, yyy = b, a + 2
    print(f"Second xxx, yyy = b, a + 2{xxx,yyy}: {xxx=}={b=}, {yyy=}={a=}+2",end=",    ")
    
    """
    Second: (5, 12)
    If your initial impression was that the value of b would be 7 instead of 12, you have fallen into the trap of in-place swapping. 
    In Python, we can unpack iterables to variables in a single assignment using automatic unpacking. For instance: 
    """
    ni = [1,2,3]
    a1, b2, c3 = ni #[1, 2, 3]
    print(f"{a1=}, {b2=}, {c3=} = {ni=}",end=",    ")#    print(b)    print(c)
    
    """
    1
    2
    3
    We can also collect several values into a single variable using * 
    this Python trick is called packing. Below is an example of packing.  
    """
    aB, *bB = 1, 2, 3, 4, 5, 6
    print(f"{aB=}, *{bB=}  =1,2,3,4,5,6")
    secondArray = array()
    print(f"{secondArray.sumNum(bB)=}, {sum(bB)=}",end=",    ")
    sumItme = 0
    for itme in bB:
        sumItme += itme
    print(f"sumItme=0  for itme in bB:  sumItme += itme  {sumItme=}")
    """
    1 [2, 3]
    Combining automatic packing and unpacking gives rise to a technique known as simultaneous assignment. 
    We can use simultaneous assignment to assign a series of values to a series of variables.
    """
    #def add_numbers(numbers):
    #return sum(numbers)

    #3 List vs. Tuples 
    
    import sys
    
    aList = [1, 2, 3, 4, 5]
    aTuple = (1, 2, 3, 4, 5)
    
    print(f"#03 List size: {sys.getsizeof(aList)=} bytes", end=",    ")
    print(f"Tuple size: {sys.getsizeof(aTuple)=} bytes",end=",    ")
    
    """
    List size: 112 bytes
    Tuple size: 96 bytes
    Most Python programmers are familiar with the list data structure. The same can't be said of tuples. They're both iterables, allow indexing, and permit storage of heterogeneous data types. But there are situations in which the use of a tuple may be preferred over a list. 
    First of all, lists are mutable, which means we can modify them as we wish: 
    """
    
    secondList = [1,2,3,4,5]    
    secondList[2] = 8
    print(f"secondList=[1,2,3,4,5], secondList[2] = 8, {secondList=}")
    
    """
    [1,2,8,4,5]
    Tuples, on the other hand, are immutable, which means trying to modify them will raise a TypeError. 
    For this reason, tuples are more memory efficient since Python can allocate the right memory block required for the data. In contrast, in a list, extra memory has to be allocated just in case we extend it - this is called dynamic memory allocation. 
    TLDR; In scenarios where you do not want the data to be changed, then a tuple data structure should be preferred over a list for memory reasons. Tuples are also faster than lists. 
    Learn more about Python Data Structures in this tutorial. 
    """
#4 Generators
    
    thirdList = [x * 2 for x in range(10)]
    thirdTuple = (x * 2 for x in range(10))
    
    print("#04 Generators:  thirdList=",thirdList,"     for itmd in thirdTuple: print(itmd) ",end=",    ")
    for itmd in thirdTuple:
        print(f"{itmd}",end=', ')
    print(
    """
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]        <generator object <genexpr> at 0x7f61f8808b50>
    List comprehensions are the pythonic way of creating a list from another iterable - It's much faster than using a for loop. But what happens if you accidentally change the brackets from [] to ()? 
    You get a generator object. In Python, rounded brackets with list comprehension logic create what is known as a generator object. Generators are a special kind of iterable. 
    Unlike lists, they do not store their items. Instead, they store instructions to generate each element in order and the current state of iterations.
    Each element is only generated upon request using a technique called lazy evaluation. The main benefit of this Python tip using a generator is that it uses less memory; the entire sequence isn't built at once""")

#5 Aliasing 

    aliasing = [1, 2, 3, 4 ,5]
    print(f"#05 {aliasing=}",end=",    ")
    bAliasing = aliasing

    # Change the 4th index in b
    bAliasing[4] = 7
    print(f"after bA=alising and bAliasing[4]=7,  {aliasing=}",end=",    ")
    print(f"{(id(aliasing))=}?={(id(bAliasing))=}")    #    print(id(bAliasing))
    print(f"{aliasing=} # Remember we did not explicitly make changes to aliasing.",end=",    ")
    
    """
    2278459070720
    2278459070720
    [1, 2, 3, 4, 7]
    Python is an object-oriented programming language - everything is an object. Thus, assigning an object to an identifier is creating a reference to the object. 
    When we assign one identifier to another identifier, we end up with two identifiers that reference the same object. This is a concept known as aliasing. Changes in one alias will affect the other. Sometimes this behavior is desired, but often, it catches us off guard. 
    One way around it is to refrain from aliasing when using mutable objects. Another solution could be to create a clone of the original object rather than a reference. 
    The most straightforward way to create a clone is to leverage slicing: 
    """

    bAliasing = aliasing[:] 
    print (f"Create a clone: bAliasing = aliasing[:] {aliasing=}, and {bAliasing=}")
    """
    This will create a new reference to a list object in the b identifier. 
    You could devise many other solutions, like calling list(a) when assigning the data to another identifier and using the copy() method. 
    """

#6 The ‘not’ Operator       if not then empty
    
    empty_ = []
    #print(not empty_)
    """
    True
    Our next Python tip is the easiest way to check if your data structure is empty by using the not operator. Python's built-in not is a logical operator that returns True if the expression is not true, or else it will return False – it inverts the truth value of Boolean expressions and objects.  
    Another way you may see it used is in an if statement: 
	"""
    
    if not empty_:
        print(f"#06 use not oper 2 chk if its empty_=[]  {(not empty_)=}")
        # do something... 
    """
    When a is True then the not operator will return False, and vice versa. 
    It's tricky to wrap your head around, so give it a go. 
    """
    
#7 F-strings
    
    first_naMe = "John"
    Aage = 19
    
    print(f"#07 FStrings: Hi, I'm {first_naMe=} and I'm {Aage=} years old!",end=",    ")
    
    """
    Hi, I'm John and I'm 19 years old!
    Occasionally, we may need to format a string object; Python 3.6 introduced a cool feature called f-strings to simplify this process. It helps to understand how strings were formatted before the new release to appreciate the new method better. 
    Here's how strings used to be formatted: 
    """
    
    first_namE = "John"
    agE  = 19
    
    print(".Format(first_name,age) Hi, I'm {} and I'm {} years old!".format(first_namE, agE))
    
    """
    Hi, I'm John and I'm 19 years old!
    Essentially, the new way of formatting is faster, more readable, more concise, and harder to get wrong.
    Another use of f-strings is to print an identifier name along with the value. This was introduced in Python 3.8.
    """
    
    #x = 10
    #y = 20
    #print(f"{x = }, {y = }")
    
    """
    x = 10, y = 20
    Check out this tutorial on F-string Formatting in Python to learn more. 
    """

#8 The Print Functions ‘end’ Parameter
    
    printEnd = ["english", "french", "spanish", "german", "twi"]
    print(f"#08 Print Functions ‘end’ Parameter: {printEnd=}",end=",    ")
    for language in printEnd:
        print(language, end=" ")   
    print()
    """
    english french spanish german twi
    It is quite common to use a print statement without defining any of its optional parameters. Consequently, several Pythonistas are unaware that you can control the output to some degree.
    One optional parameter we can change is end. The end parameter specifies what should be shown at the end of a call to a print statement. 
    The default of end is "\n" which tells Python to start a new line. In the code above, we changed it to space. Thus, the output returned all the elements of our list are printed on the same line.
    """

#9 Append to Tuple
    
    append2Tuple = (1, 2, [1, 2, 3])
    print(f"#09 Use list to {append2Tuple=}",end=",    ")
    append2Tuple[2].append(4)
    print(f"After a[2].append(4): {append2Tuple=}")
    
    """
    (1, 2, [1, 2, 3, 4])
    We already know tuples are immutable – see Python trick #3 List vs. Tuples. Attempting to change the state of a tuple would throw a TypeError. But, if you think of a tuple object as a sequence of names with bindings to objects that cannot be changed, you may see things differently.
    The first two elements of our tuple are integers - they are immutable. The last element of our tuple is a list, a mutable object in Python.
    If we consider our list to be just another name in a sequence with a binding to an object that cannot be changed, then we would realize that the list can still be modified from within the tuple.
    Would we recommend you do this in practice? Probably not, but it is one of those nice-to-know things!
    """

#10 Merging Dictionaries
    
    aDict = {"a": 1, "b": 2}
    bDict = {"c": 3, "d": 4}
    
    a_and_b = aDict | bDict
    print(f"#10 Use | to merge Dicts{aDict=}, {bDict=}, {a_and_b=}")
    
    """
    {"a": 1, "b": 2, "c": 3, "d": 4}
    In Python 3.9 and above, it is possible to merge dictionaries using | (bitewise OR). There is not much else to say about this particular Python trick other than it is a much more readable solution!  
    """

#11 Ternary Operator / Condition Expressions 
    
    condition = True
    name = "John" if condition else "Doe"
    
    print(f"#11 Ternary Operator / Condition Expressions: {condition=}; {name=} if condition else 'Doe'",end=",    ")
    
    """
    John
    In the code above, you can see what is known as a ternary operator - 
    it is also referred to as a conditional expression among names. 
    We use ternary operators to evaluate things based on whether a condition is T or F.
    Another way we could have written our code above is as follows:
    """
    
    if condition:
        name = "John"
    else:
        name = "Doe"
    """
    print(name)
    John
    Although both sets of code result in the same output, 
    notice how the ternary conditional permits us to write much shorter and clearer code.
    It's what Pythonistas would call the more 'Pythonic' way to write code. """
    t = 910
    (lambda: print(f"{t=}Water is not boiling: t >= 100"), lambda: print(f"{t=}Water is boiling: t >= 100"))[t >= 100]()
    '''x = -1
    if x < 0:
        print('x is less than zero')
    elif x > 0:
        print('x is greater than zero')
    else:
        print('x is equal to 0')'''
    #x is less than zero
    #We can rewrite this code using nested ternary operators:
    x = -1        #print(f"{condition=}; {name=} if condition else 'Doe'")
    literalx = 'x is less than zero' if x < 0 else 'x is greater than zero' if x > 0 else 'x is equal to zero'
    print(f"{x=} | {literalx=}: 'x is less than zero' if x < 0 else 'x is greater than zero' if x > 0 else 'x is equal to zero'")

#12 Remove Duplicates From Lists
    
    removeDups = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 2, 2]
    print(f"#12 {removeDups=} | {list(set(removeDups))=}")
    
    """
    [1, 2, 3, 4, 5, 6, 7]
    The simplest way to remove duplicate elements from a list is to convert the list into a set (then back to a list if you wish).
    Based on mutability, sets and lists are quite similar in Python. We can add and remove elements from both data structures at will, but they are still extremely different.
    Lists are ordered, zero-based indexed, and mutable. Sets are unordered and unindexed. The elements in a set must be of an immutable type, even though the set itself is mutable - trying to retrieve an element via an index or modify an element will raise an error.
    Another key difference between sets and lists is that sets cannot contain duplicates. This is what helped us remove the duplicate elements from our list.
    """

#13 Standalone Underscore 
    
    standalone_=1 + 2    #    print(_)    print(_)
    print(f"#13 {standalone_=} | _ = result of last oper.")
    
    """3
    Underscore (_) is a legal identifier in Python, thus, it's possible to use it to reference an object. 
    But underscore also has another responsibility: to store the result of the last evaluation.
    The documentation states that "the interactive interpreter makes the result of the last evaluation available in the variable _. (It is stored in the builtins module, alongside built-in functions like print)."
    Since we did not assign underscore an object before calling it on the first line, we got an error. However, when we calculated the output of 1 + 2, the interactive interpreter stored the result in the _ identifier for us. 
    """
#14 Underscore to Ignore Values
    print("#14 Ignore with _: for _ in range(10):",end=",    ")
    for _ in range(4):
        print("The _ index doesn't matter",end=", ")
    print()
    """
    The index doesn't matter, The index doesn't matter    ...
    In Python tip #13, we discovered the interactive interpreter makes the last result of an evaluation available in the underscore (_) identifier, but that's not its only use case.
    We may also use it to represent objects we don't care about or wouldn't use at a later point in the program. This is important because using an identifier instead of an underscore (_) will raise an F841 error when we attempt to do linting on our program. An F841 error simply states that a local variable name has been assigned but was not used in the program, which is a bad practice.
    """
#15 Trailing Underscores

    list_ = [0, 1, 2, 3, 4]
    global_ = "Hi there" 
    print(f"#15 avoid conflicts with Python keywords_| {list_=} {global_=}")
    """
    Continuing from the past two tricks, Python's underscore (_) usage, another purpose of it is to avoid conflicts with Python keywords. 
    PEP 8 mentions that a trailing underscore (_) should be "used by convention to avoid conflicts with Python keywords." It also states that "it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus list_ is better than lst."
    """
#16 Leading Underscores

    #class Example:
    #    def __init__(self):
    #        self._internal = 2
    #        self.external = 20
    #        print(f"leading_ 4 internal use only: {self._internal=}, {self.external=}")
    exEx = Example()    #    exEx.useVars()
    #exEx.__init__(any)

    """
    You would often find experienced Python programmers tend to prefix an underscore to an identifier or method name - and for good reason.
    The underscore prefixed to an identifier or method has a hidden meaning: 
    this variable or method is only meant for internal usage. 
    Essentially, it is a disclaimer to other programmers that have been defined in PEP 8
    but is not enforced by Python. Thus, leading underscores are a weak indicator.
    Unlike Java, Python doesn't have a strong distinction between private and public variables. 
    In other words, it only has meaning because the Python community has agreed for it to have meaning. 
    Their inclusion does not impact the behavior of your programs.
    """

#17 Underscore Visual
    #Here is the last tip on underscores; So far, we have covered three different use cases for the underscore, but you can check out our tutorial to learn more about the Role of Underscore(_) in Python. 
    	
    number = 1_500_000
    print(f"#17 visual separator for digit grouping in integral, floating-point, and complex number{(number:=150_000_000):,}")
    
    """
    15000000
    Another way we could use the underscore is as a visual separator for digit grouping in integral, floating-point, and complex number literals – this was introduced in Python 3.6. 
    The idea was to aid the readability of long literals, or literals whose value should clearly be separated into parts – you can read more about it in PEP 515.
    """

#18 __name__ == “__main__”

    #if __name__ == "__main__":
    #    print("Read on to understand what is going on when you do this.")
	
    print("#18 import from diff module: 'name != main': if __name__ == '__main__':")
    """
    There's a high chance you've seen this syntax in several Python programs; Python uses a special name called "__main__" and sets it to an identifier called __name__ if the Python file being run is the main program.
    If we decide to import the module displayed in the screenshot into another module (Python file) and run that file, the truth of the expression in our code will be false. This is because when we import from another module, the __name__ identifier is set to the name of the module (Python file). 
    """
#19 The ‘setdefault’ Method 
	
    import pprint
    
    text = "It's the first of April. It's still cold in the UK. But I'm going to the museum so it should be a wonderful day"
    
    counts = {}
    for word in text.split():
        counts.setdefault(word, 0)
        counts[word] += 1
    
    #pprint.pprint(counts)
    print(f"#19 .setdefault(key,set 2 if not found)")
    print('''    counts = {}
    for word in text.split():
        counts.setdefault(word, 0)
        counts[word] += 1
    ''')
    print(counts)
    """
    {'April.': 1,
    'But': 1,
    "I'm": 1,
    "It's": 2,
    'UK.': 1,
    'a': 1,
    'be': 1,
    'cold': 1,
    'day': 1,
    'first': 1,
    'going': 1,
    'in': 1,
    'it': 1,
    'museum': 1,
    'of': 1,
    'should': 1,
    'so': 1,
    'still': 1,
    'the': 3,
    'to': 1,
    'wonderful': 1}
    "
    
    You may wish to set a value for various keys in a dictionary. For example, when you're tracking the counts of words in a corpus. The common way to do this is as follows: 
    Check if the key exists in the dictionary
    If it does, increment the value by 1.
    If it does not, add it and set the value to 1.
    This is how it looks in code:
    
    
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
        counts[word] = 1
    
    A more concise way to do this is to use the setdefault() method on your dictionary object.
    The first argument passed to the method is the key we want to check for. The second argument passed is the value to set the key to if the key does not already exist in the dictionary - if the key exists, then the method would return the key value. Thus, it would not be changed.
    """
#20 Matching Regex
		
    import re
    
    number = re.compile(r"\d{10}")
    #number.search()
    num_1 = number.findall("My number is +447999999999")
    num_2 = number.search("My number is 07999999999")
    #num_1.group()
    print(f"#20 RegexMatch: {num_1=}, {num_2.group()=}",end=",    ")
    print('number = re.compile(r"(0?)(\+44)?\d(10)")     num_1 = number.search("My number is +447999999999")    num_2 = number.search("My number is 07999999999")')
    
    """
    '+447999999999'
    '07999999999'
    Regular expressions allow you to specify a pattern of text to search for; The majority of people know we can search for things using CTRL + F (Windows), but if you don't know the exact thing you're searching for, how could you find it? The answer is to search for patterns.  
    For example, UK numbers follow a similar pattern: they will have a zero at the beginning plus ten numbers or +44 instead of zero and ten numbers – the second instance indicates it's in its international format. 
    Regular expressions are a major time saver. If we were to code rules to catch the instances in our image instead of regex, it could take up to 10+ lines of code. 
    Learning how regular expressions work is vital even if you don't write code. Most modern text editors and word processors permit you to use regular expressions to find and replace features.
    """

#21 Regex Pipe
	
    import re
    
    heros = re.compile(r"Super(man|woman|human)")
    
    h1 = heros.search("This will find Superman")
    h2 =  heros.search("This will find Superwoman")
    h3 = heros.search("This will find Superhuman")
    
    print('#21 regex-pipe: heros = re.compile(r"Super(man|woman|human)") \t    h1 = heros.search("This will find Superman")\t    h2 =  heros.search("This will find Superwoman")\n    h3 = heros.search("This will find Superhuman")',end=',         ')
    print(f"{h1.group()=}, {h2.group()=}, {h3.group()=}")
    """
    Superman
    Superwoman
    Superhuman
    Regular expressions have a special character called pipe (|) that allows you to match one of many expressions, and they can be used anywhere. This is super handy for when you've got several similar patterns.
    For example, 'Superman,' 'Superwoman,' and 'Superhuman' all have the same prefix. Thus, you could leverage the pipe to retain the part of the pattern that is recurring and change the parts you need to be different. Once again, saving you precious time.
    Mind the gotcha: if all of the expressions you wish to match occur in the same text, the first occurrence of text to match would be returned - i.e., "An example text containing Superwoman, Superman, Superhuman," would return Superwoman.
    """

#22 The Print Function ‘sep’ Parameter
	
    day = "04"
    month = "10"
    year = "2022"
    
    print("#22 Print no sep=",day, month, year,end=",    ")
    print("'' sep=",day, month, year, sep = "",end=",    ")
    print("'.' sep=",day, month, year, sep = ".")
    
    
    """
    04 10 2022
    04/10/2022
    04.10.2022
    The number of Python programmers that aren't aware of the print() function's full capabilities is scary; If “Hello World” was your first program, the print() function was probably one of the first built-in functions you covered when learning Python. We use print() to display formatted messages on the screen, but there's a whole lot more to the print() function. 
    In the code above, we've shown different ways to display our formatted message. The sep parameter is an optional argument in the print() function that allows us to specify how objects should be separated if we include more than one. 
    The default is to separate them with a space, but we've changed this functionality with our print statements - one where sep is set to "" and another where sep is set to ".".
    """

#23 Lambda Functions 

    def reg_square(num:int) -> int:
        return num ** 2
    print(f"#23 def reg_square(num:int) -> int:        return num ** 2    Function call: {reg_square(4)=}")
    """
    Function call: 16
    """
    square_lambda = lambda x: x**2
    print(f'square_lambda = lambda x: x**2    Lambda function: {square_lambda(4)=}')
    """
    Lambda functional: 16
    Lambda functions take you to the more intermediate-advanced level things you could do with Python – learn Intermediate Python with this course. They look complicated at first glance, but they are quite simple.
    In our example code, we only used one argument, but we could have used multiple if we wanted:
    """
    doExponent_lambda2 = lambda a, b: a ** b
    print(f"doExponent_lambda2 = lambda a, b: a ** b    Lambda function: {doExponent_lambda2(4, 2)=}")
    """
    16
    In essence, the lambda keyword permits us to create small, restricted, anonymous functions in one line. They behave as a regular function declared with a def keyword, except these functions do not have a name.
    """
#24 The ‘swapcase’ Method
	
    stringA = "SoMe RaNDoM sTriNg"
    print(f'#24 {stringA=}{stringA.swapcase()=}')
    """
    sOmE rAndOm StRInG
    The swapcase() method is applied to a string object to allow us to change the upper case letters to lower case and vice versa in a single line of code. There are not many use cases for the swapcase() method, but it is nice to know.
    """
#25 The ‘isalnum’ Method

    passwordA = "ABCabc123"
    print(f'#25 alphaNumeric?:{passwordA=},  {passwordA.isalnum()=}, {passwordA.isnumeric()=}, {passwordA.isdecimal()=}')
    
    """
    True
    Let's say we're creating a program that requires users to input a password, but it must have a combination of numbers and letters. We can do this in one line of code by calling the isalnum() on the string instance.
    The method checks if all the characters are part of the alphabet (A-Za-z) and numeric (0-9). A space or symbol (!#%$&? etc.) will return False.
    """
#26 Exception Handling

    def get_ratioA(x:int, y:int) -> int:
        #ratio = 0    z = 0 if y == 0 else (x / y) 
        try:
            1/0
        except ZeroDivisionError:
            print('#26 Exception Handling: try: except ZeroDivisionError: else: finally:',end="    ")
        finally:
            return  0 if y == 0 else  (x/y)
    print(f'{get_ratioA(x=400, y=0)=}')
    """
    400.0
    Python programs terminate when they encounter an error.
    Sometimes, we don't want this behavior, like when we have an end-user interacting with our code. How bad would it be if our code terminated prematurely in such an instance?
    There are a few ways of thought on how to deal with the exceptional case. Most Python programmers typically embrace the thought that it's easier to ask for forgiveness than it is to get permission. This means they would rather catch a raised error by providing surrounding context that is capable of handling an exception. The idea behind this thought is that there's no point in wasting time trying to safeguard against all the various exceptional cases.
    But this only holds when there is a mechanism for coping with a problem after it occurs.
    """

#27 Identifying the Differences in Lists

    list_1 = [1, 3, 5, 7, 8]
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solution_1 = list(set(list_2) - set(list_1))
    solution_2 = list(set(list_1) ^ set(list_2))
    solution_3 = list(set(list_1).symmetric_difference(set(list_2)))
    print(f'#27 Finding Differences in {list_1=}, {list_2=}')
    print(f"solution_1 = list(set(list_2) - set(list_1))                        {solution_1=}")
    print(f"solution_2 = list(set(list_1) ^ set(list_2))                        {solution_2=}")
    print(f"solution_3 = list(set(list_1).symmetric_difference(set(list_2)))    {solution_3=}")
    """
    Solution 1: [9, 2, 4, 6]
    Solution 2: [2, 4, 6, 9]
    Solution 3: [2, 4, 6, 9]
    Here are three different methods to compare the difference between two lists in Python. 
    Note: Unless you know for a fact that list_1 is a subset of list_2, then solution 1 is not the same as the other two solutions.
    """
#28 Args & Kwargs
    def some_functionA(*args, **kwargs):
        print(f"#28 def some_functionA(*args, **kwargs):    {args=}, {kwargs=}")
    some_functionA(1, 2, 3,  a=4, b=5, c=6)
    """
    Args: (1, 2, 3)
    Kwargs: {'a': 4, 'b': 5, 'c': 6}
    We use *args and **kwargs as parameters to a function when we are unaware of the number of variables our function should expect. 
    The *args parameter permits us to pass a variable number of parameters to a function when it’s non-keyworded (i.e., the parameters we pass do not require an associated name). On the other hand, the **kwargs parameter enables us to pass an arbitrary number of keyworded parameters to a function.
    In truth, the words *args and **kwargs are not so magical: the true magic is in the asterisks (*). This means we could have used any word after the astericks, but the use of args and kwargs is common practice, and it is enforced among Python developers. 
    """
    
#29Ellipsis
    print(..., "#29")
    """
    Ellipsis
    """
    def some_functionD():
        ...
    # Alternative solution
    def another_functionE():
        pass
    """
    The Ellipsis is a Python object that can be called by providing a sequence of three dots (...) or calling the object itself (Ellipsis).
    Its most notable usage is for accessing and slicing multidimensional arrays in NumPy, for example:
    """
    #import numpy as np
    #arr = np.array([[2,3], [1,2], [9,8]])
    print(f'access/slice matrix: arr[...,0]=    arr[...]=')
    """
    [2 1 9]
    """
    
    print(f'arr[...]')
    
    """
    [[2 3]
     [1 2]
     [9 8]]
    But another usage of Ellipsis is as a placeholder in an unimplemented function. 
    This means you could pass Ellipsis, ..., or pass, and they would all still be valid.
    """
#30 List Comprehension
    even_numbersA = [x for x in range(10) if x % 2 == 0 and x != 0]
    print(f'#30 even_numbersA = [x for x in range(10) if x % 2 == 0 and x != 0]       {even_numbersA=}')
    """
    [2, 4, 6, 8]
    Our final Python trick is list comprehensions, an elegant way to create a list out of another sequence. They allow you to perform sophisticated logic and filtering as we've done in the code above.
    There are other ways to achieve the same goal; for example, we could have used a lambda function as follows:
    """
    even_numbersS = list(filter(lambda x: x % 2 ==0 and x != 0, range(10)))
    print(f'even_numbersS = list(filter(lambda x: x % 2 ==0 and x != 0, range(10)))   {even_numbersS=}')
    """
    [2, 4, 6, 8]
    But several Pythonistas would argue this solution is much less readable than the list comprehension.
    Learn more: <https://www.datacamp.com/tutorial/python-list-comprehension>.   
    """
    
    import calendar as calndr, os,shutil,time, math, random, basicMath as maths, string, turtle       #, tkinter as tk
    #monthA = calndr.TextCalendar(6)
    #monthA.prmonth(2024,5)
    calndr.TextCalendar(6).prmonth(2024,5)
    calndr.prcal(2024,0,0,6,6)
    pie=[]
    ranlist=['David',44,'BDM Pubs',3245.23,'Pi',True,3.14, 'Python']
    print(f'{os.getcwd()=}')
    print(f'{[t for t in calndr.month_name if t.isalpha]},{[s for s in calndr.day_name]}')    #if "a" in x
    sourceDir = r'C:\Users\Brice\source\repos\LearningPy\TestCopilot'
    destDir   = 'I:\C\Source\Resources\TestCoPilot\cloneBkup' + time.strftime("%m-%d-%Y_%H%M%S") #.asctime() => 𝝅
    for src_dir, dirs, files in os.walk(sourceDir):
        dstDir = src_dir.replace(sourceDir,destDir,1)
        if not os.path.exists(dstDir):
            pass #os.makedirs(dstDir)  https://docs.python.org/3/library/math.html#
    print(f"{math.sin(math.pi/2)=}, roundup:{math.ceil(9.8)=}, down:{math.floor(1.2)=}, remvFraction:{math.trunc(123.45)=}.sqrt.16:{math.trunc(math.sqrt(16))},e:{math.e},𝝅:{math.pi}, sum.1(10)={sum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])}, math fsum:{math.trunc(math.fsum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]))}")
    print(f'accurateto11{(math.exp(1e-5) - 1)=}, full acc{math.expm1(1e-5)=},{(pie:=[random.randint(0,5) for poi_ in range(5) if poi_ not in pie]) },{math.trunc(math.fsum([.1 for _ in range(10)]))},{random.random() *100=}')    
    #wordtxt = r'C:\Users\Brice\Downloads\words\words.txt'
    wordtxt = r'C:\Users\Brice\source\Resources\BestXMasMocktails.txt';wds=10
    headsTails={'Heads':0,'Tails':0}; coin=list(headsTails.keys())
    for i in range(10000):
        headsTails[random.choice(coin)]+=1
    print(f'{ranlist=}{random.choice(ranlist)},{random.shuffle(ranlist)},{ranlist=},{random.choice((ranlist))},{headsTails["Heads"]=},{headsTails["Tails"]=}')
    print(f'Use 46M Englist words: pick {wds=} random',end=', ')
    with open(wordtxt,'rt') as wordf:
        words1= wordf.readlines()
    words=[w.rstrip() for w in words1];print("-"*10,end=", ")
    for w1 in random.sample(words,wds):
        print(f'{w1}',end=", ")
    print('-'*10);#print()  TKINTER \/  \/  \/  \/  \/

    root = tk.Tk()
    app = Window(root)
    root.wm_title("Tkinter window")
    root.configure(background='pink')
    def click():
        print('You just clicked me',end=',    ')

    #root=tk.Tk()
    btn=tk.Button(root,text='Hello everyone!',command=click)
    btn.pack()
    
    print(f"{'*'*10}{maths.times2(4.5)=},{maths.times3(3)=},{maths.square(3)=},{maths.powery(3,2)=}")
    #os.system("testTkinter.py")  todo!
    #C:\Users\Brice\AppData\Local\Programs\Python\Python312
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()_~'
    size = 5
    def randompassword():
        return ''.join(random.choice(chars) for _ in range(size,size*4))
    print(f'{[randompassword() for _ in range(10)]}')
    
    asize=80
    tsize=45
    for _ in range(8):
        turtle.forward(asize)
        turtle.left(tsize)
    else:
        turtle.bgcolor('red')
    textA = 'Brice'
    textB = 'Text to Binary Convertor'
    print(f'{textB} so {textA}: {" ".join(format(ord(xC), "b")for xC in textA)}')
    import idlelib
    #from idlelib.TreeWidget import ScrolledCanvas, FileTreeItem,TreeNode
    #idlelib.tree.Widget.s
    root.title('File Browser')
    #sc = ScrolledCanvas(root,bg='white',highlightthickness=0,takefocus=1)
    #sc.frame.pack(expand=1,fill='both',side='left')
    #itemA= FileTreeItem(os.getcwd())
    #nodeA = TreeNode(sc.canvas,None,itemA)
    #nodeA.expand()
    root.mainloop()        #    print("*"*10)
    from tkinter import filedialog as filedg
    dirname = filedg.askdirectory()
    print(dirname)
    