# This code will demonstrate basic print functionsfunction

print("Hello World\n")

# Seprateor function= used to add seprator between two literals in a print statement stated as 'sep'

print("Hello World "," First Python Code",sep='|')

# End Function = used to add codes lines in the end stated as end

print("This is a first statement",end="\n")

# Flush function = used to force immediate output on console

print("Loading...",end="\r",flush=True)

# File function = used to determine where the statement will be printed
import sys

print("Hello Statement\n",file=sys.stdout)

