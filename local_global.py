Explain the difference between local and global variables in a Python function.

Local Variable:
  A local variable is declared inside a function (or block).
  It is only accessible within that function — once the function ends, the variable is destroyed.
  It does not affect or interact with variables of the same name outside the function.
Global Variable:
    A global variable is defined outside any function.
    It can be accessed inside functions (read-only by default).
    If you want to modify it inside a function, you must declare it using the global keyword.
    
Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
    x = 'Hello'
def greet():
    x = 'Hi'
    print(f'Local value {x}')

print(f'global value {x}')
greet()

Output:

global value Hello
Local value Hi
