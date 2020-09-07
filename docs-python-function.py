from colors import color

print(color.BLUE + "Print the documents (syntax, description etc.) of Python built-in function(s)." + color.END)

print(color.YELLOW + "Python Docstring:\n"
"A docstring is a string literal that occurs as the first statement in a module, "
                     "function, class, or method definition.\n"
                     "Such a docstring becomes the __doc__ special attribute of that object.\n"
                     "All modules should normally have docstrings,"
                     "and all functions and classes exported by a module"
                     "should also have docstrings.\n"
                     "Public methods (including the __init__ constructor) should also have docstrings." + color.END)

print(abs.__doc__)
print(abs.__name__)
