from colors import color

print(color.BLUE + "Get the Python version you are using" + color.END)


print(color.YELLOW + "# Version info:\n"
"A tuple containing the five components of the version number: "
"major, minor, micro, releaselevel, and serial.\n"
"All values except release level are integers;\n"
"the release level is 'alpha', 'beta', 'candidate', or 'final'."
"\nThe version_info value corresponding to the Python version 2.0 is (2, 0, 0, 'final', 0)."
"\nThe components can also be accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major and so on."
 "\nNote : 'sys' module provides access to some variables used or maintained by the interpreter"
"\nand to functions that interact strongly with the interpreter." + color.END)

import sys
print ("Python version")
print(sys.version)
print ("Version Info")
print(sys.version_info)
