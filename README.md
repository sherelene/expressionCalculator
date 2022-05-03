# expressionCalculator
Evaluate floating point expressions whose operands and values are floating-point numbers.

This project is an extension of the java floating point calculator repo. The algorithm converts an infix expression into a suffix expression (Postfix expression).
These then get calculated by using a stack. Examples of java floating point literals can be found here on [oracle's website](https://docs.oracle.com/javase/specs/jls/se17/html/jls-3.html#jls-DecimalFloatingPointLiteral).


As is the case with the java floating point calculator repo, some precision is lost and trailing zeroes can be found when using this repo. 

Credits are give to [ofstack](https://ofstack.com/python/18489/python-implements-a-simple-four-step-calculator.html) for their code on how to implement a stack from scratch
as well as the infix and postfix expression. This project calls for no use of librabries so having a class object named Stack was very helpful. Their code that was implemented 
to mine had to be adjusted to include java floating point literals. 
