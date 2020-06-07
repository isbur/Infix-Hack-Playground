import inspect
import sys
import traceback
from functools import partial


def dprit():
    traceback.print_stack(file=sys.stdout)
    print("#"*5)


class Infix:

    def __init__(self, operator_function):
        #dprit()
        self.operator_function = operator_function

    def __ror__(self, lefthand_operand):
        #dprit()
        return Infix(
            partial(
                self.operator_function_thin_wrapper, lefthand_operand=lefthand_operand
            )
        )
 #       return Infix(
 #           partial( self.lefthand_operand_handler, other=other )
 #       )

 #   def lefthand_operand_handler(self, righthand_operand, other):
 #       dprit()
 #       return self.function(other, x)

    def __or__(self, righthand_operand):
        #dprit()
        #print(inspect.getfullargspec(self.operator_function))
        return self.operator_function(
            righthand_operand=righthand_operand
        )

    def operator_function_thin_wrapper( 
        self, 
        lefthand_operand, 
        righthand_operand
    ):
        #dprit()
        return self.operator_function(
            lefthand_operand, 
            righthand_operand
        )


def mult(x, y):
    #dprit()
    return x*y
x=Infix(mult)

print (2 |x| 4)
#dprit()
