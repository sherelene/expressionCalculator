class ConvertNums:
    @staticmethod
    def start(c):
        """
        This is the start state for our dfa.
        dfa can start with digits or with a period only.
        starting with underscores automatically rejects the numbers
        :return: next state, int of string if string is 0-9 else current char

        """
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        if c in accept_nums:
            dfa = 1
            return dfa, accept_nums[c]
        elif c == ".":
            dfa = 4
            return dfa, '.'
        # -1 is used to check for any
        # invalid symbol
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state1(c):
        """
        This function is for the next state after the start state if start state was a 0-9
        Accepts input 0-9 returns to itself
        Accepts e, E next state 3
        Accepts f, f next state 5 -> accept/end state
        :param c: current character from input string
        :return: next state, int of string if string is 0-9 else current char

        """

        dot = "."
        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        accept_chars = {"e": "e", "E": "E"}
        accept_end = {"f": "f", "F": "F", "d": "d", "D": "D"}
        if c in accept_nums:
            dfa = 1
            return dfa, accept_nums[c]
        elif c == dot:
            dfa = 22
            return dfa, dot
        elif c in accept_chars:
            dfa = 3
            return dfa, accept_chars[c]
        elif c in accept_end:
            dfa = 5
            return dfa, accept_end[c]
        elif c in underscores:
            dfa = 7
            return dfa, underscores[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state22(c):
        """
        This function is if the previous state is a dot. If it was a dot then underscores would be rejected
        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char

        """

        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        accept_chars = {"e": "E"}
        accept_end = {"f": "f", "F": "F", "d": "d", "D": "D"}
        if c in accept_nums:
            dfa = 2
            return dfa, accept_nums[c]
        elif c in accept_chars:
            dfa = 3
            return dfa, accept_chars[c]
        elif c in accept_end:
            dfa = 5
            return dfa, accept_end[c]
        elif c in underscores:
            dfa = -1
            return dfa, underscores[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state2(c):
        """
        This function next state if previous state was a digit
        Accepts input 0-9 and returns to itself
        Accepts e, E next state 3
        Accepts f, F, d, D next state 5 -> accept/end state

        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char
        """
        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        accept_chars = {"e": "e", "E": "E"}
        accept_end = {"f": "f", "F": "F", "d": "d", "D": "D"}
        if c in accept_nums:
            dfa = 2
            return dfa, accept_nums[c]
        elif c in accept_chars:
            dfa = 3
            return dfa, accept_chars[c]
        elif c in accept_end:
            dfa = 5
            return dfa, accept_end[c]
        elif c in underscores:
            dfa = 7
            return dfa, underscores[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state3(c):
        """
        This function is for after an e, E
        Required input (0-9, +,or -) next state 6
        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char

        """
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        accept_operators = {"+": "+", "-": "-"}
        if c in accept_operators:
            dfa = 6
            return dfa, accept_operators[c]
        elif c in accept_nums:
            dfa = 6
            return dfa, accept_nums[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state4(c):
        """
        This function is for the next state after the start state if start state was a .
        Accepts input 0-9 next state 2
        Accepts f, F, d, D next state 5 -> end state
        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char

        """
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        accept_end = {"f": "f", "F": "F", "d": "d", "D": "D"}
        if c in accept_nums:
            dfa = 2
            return dfa, accept_nums[c]
        elif c in accept_end:
            dfa = 5
            return dfa, accept_end[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state5(c):
        """
        Accepts only f, F
        accept/end state
        :param c: current char from input string
        :return: current state, f, F, d, D char
        """
        accept_end = {"f": "f", "F": "F", "d": "d", "D": "D"}
        if c in accept_end:
            dfa = 5
            return dfa, accept_end[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state6(c):
        """
        This function is only called if there is an exponent and after state 3
        Accepts input 0-9 returns to itself
        Accepts f, F, d, D next state 5 -> end state
        :param c: current char
        :return: next state, int of string if string is 0-9 else current char
        """
        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        accept_end = {"f": "f", "F": "F", "d": "d", "D": "D"}
        if c in accept_nums:
            dfa = 6
            return dfa, accept_nums[c]
        elif c in accept_end:
            dfa = 5
            return dfa, accept_end[c]
        elif c in underscores:
            dfa = 8
            return dfa, underscores[c]
        else:
            dfa = -1
        return dfa, -1


    @staticmethod
    def state7(c):
        """
        state only for underscores before decimals
        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char

        """
        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        if c in accept_nums:
            dfa = 1
            return dfa, accept_nums[c]
        elif c in underscores:
            dfa = 7
            return dfa, underscores[c]
        else:
            dfa = -1
            return dfa, -1


    @staticmethod
    def state8(c):
        """
        state for underscores after exponent part
        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char

        """
        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        if c in accept_nums:
            dfa = 6
            return dfa, accept_nums[c]
        elif c in underscores:
            dfa = 8
            return dfa, underscores[c]
        else:
            dfa = -1
            return dfa, -1


    @staticmethod
    def state9(c):
        """
        state only for underscores after decimals
        :param c: current char from input string
        :return: next state, int of string if string is 0-9 else current char

        """
        underscores = {"_": "_"}
        accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9}
        if c in accept_nums:
            dfa = 1
            return dfa, accept_nums[c]
        elif c in underscores:
            dfa = 9
            return dfa, underscores[c]
        else:
            dfa = -1
            return dfa, -1


    def isAccepted(self, String):
        """
         Function for taking one character to the next character by checking if they pass the approved states
        :param String: character
        :return: converted number of input string e.g 1e1 -> 10

        """

        # store length of Stringing
        length = len(String)
        # initialize variables and array for converting to float
        characters = []
        cnt = 0
        e_found = False
        e_index = 0
        dot_index = 0
        dot_found = False
        minus_index = 0
        minus_found = False

        # dfa tells the number associated
        # with the present dfa = state
        dfa = 0

        # Some fail safes if input is a _ or . only
        if String == "_":
            return False
        elif String == ".":
            return False

        # DFA to determine if input is acceptable
        for i in range(length):
            if dfa == 0:
                dfa, num = self.start(String[i])
            elif dfa == 1:
                dfa, num = self.state1(String[i])
            elif dfa == 2:
                dfa, num = self.state2(String[i])
            elif dfa == 3:
                dfa, num = self.state3(String[i])
            elif dfa == 4:
                dfa, num = self.state4(String[i])
            elif dfa == 5:
                dfa, num = self.state5(String[i])
            elif dfa == 6:
                dfa, num = self.state6(String[i])
            elif dfa == 7:
                dfa, num = self.state7(String[i])
            elif dfa == 8:
                dfa, num = self.state8(String[i])
            elif dfa == 9:
                dfa, num = self.state9(String[i])
            elif dfa == 22:
                dfa, num = self.state22(String[i])
            else:
                return False

            # if "_" is the current character, it is ignored
            if "_" == num:
                continue
            # saves index where . is found and adds to character array
            elif "." == num:
                dot_index = cnt
                dot_found = True
                characters.append(num)
            # saves index where e or E is found and adds to character array
            elif "e" == num or "E" == num:
                e_index = cnt
                e_found = True
                characters.append(num)
            # if "+" is the current character, it is ignored
            elif "+" == num:
                continue
            # if negative it means it is an accepted negative which means it is a negative
            # found after the exponent. Store minus_found as True
            elif "-" == num:
                minus_found = True
            # if "f" or "F" is the current character, it is ignored
            elif "f" == num or "F" == num or 'D' == num or 'd' == num:
                continue
            else:  # numbers are added to character array to be converted to a float
                characters.append(num)

            # keeps track of character array indexes
            cnt = cnt + 1

        # accepted states of the dfa
        if dfa == 6 or dfa == 4 or dfa == 5 or dfa == 2 or dfa == 1 or dfa == 22:
            # function to take character array and transform into a float
            number = self.get_num(characters, e_index, e_found, dot_index, dot_found, minus_found)
            return number
        else:
            return 0


    @staticmethod
    def get_num(characters, e_index, e_found, dot_index, dot_found, minus_found):
        """
        Function that does the actual converting of characters to a float
        :param characters: the validated java floating point number input string
        :param e_index: index where e or E can be found
        :param e_found: bool if e or E exist
        :param dot_index: index where "." can be found
        :param dot_found: bool if dot exist
        :param minus_found: bool if there is a negative sign found after e or E
        :return: string number to float number e.g 1e1 -> 10

        """

        # initialize variables for help converting to float
        length = len(characters)
        sum = 0
        whole_num = 0
        decimals = 0
        ind = 0
        power = 0

        # if input was a decimal number
        if dot_found:
            # index for adding numbers before and after the dot
            before_dot = dot_index - 1
            after_dot = -1

            # gets the numbers before the decimals
            for i in range(before_dot, -1, -1):
                # eg 123.45e2 has dot index 3. before_dot = 2
                # subtracts 1 from before_dot with every iteration
                # iterates 1 x 10^2 + 2 x 10^1 + 3 x 10 ^0 = 123
                whole_num = whole_num + (characters[ind] * 10 ** i)
                ind = ind + 1

            # if theres numbers after the decimals and theres an exponent
            if dot_index != length and e_found:
                # starting from after the dot until the exponent
                for j in range(dot_index + 1, e_index):
                    # after_dot is 10 ^-1
                    # so if the number is .123, it will be 1 x 10 ^ -1 = .1
                    decimals = decimals + characters[j] * 10 ** after_dot
                    # then it will be after_dot = -1 - 1 =  2 x 10 ^-2 = . 02
                    after_dot = after_dot - 1

                # since exponent IS found, exp_length is length of exponent eg. e10 is length 2
                # eg 123.45e2 is (8(length)- 6(e_index)) - 2 = 0 therefore exp_length has only 10^0
                # eg 123.45e25 is (9(length)- 6(e_index)) - 2 = 1 therefore exp_length has 10^0 and 10^1
                exp_length = (length - e_index) - 2
                ind = e_index + 1
                for k in range(exp_length, -1, -1):
                    power = power + (characters[ind] * 10 ** k)
                    ind = ind + 1
                if minus_found:
                    # if there is a negative in exponent then make power negative
                    power = -power
                sum = (whole_num + decimals) * 10 ** power

            # if number does not end with a dot eg 123. or 42. and does not have exponent
            elif dot_index != length:
                for j in range(dot_index + 1, length):
                    decimals = decimals + characters[j] * 10 ** after_dot
                    # after dot is 10 ^-1 and iterates to 10^-2, 10^-3, etc
                    after_dot = after_dot - 1
                sum = whole_num + decimals
            else:
                sum = whole_num + decimals

        # if only exponent is found and it is a whole number
        elif e_found:
            ind = 0

            # get number before exponent
            for i in range(e_index - 1, -1, -1):
                # eg 123.45e2 has dot index 3. before_dot = 2
                # subtracts 1 from before_dot with every iteration
                # iterates 1 x 10^2 + 2 x 10^1 + 3 x 10 ^0 = 123
                whole_num = whole_num + characters[ind] * 10 ** i
                ind = ind + 1

            exp_length = (length - e_index) - 2
            ind = e_index + 1
            # since exponent IS found, exp_length is length of exponent eg. e10 is length 2
            # eg 123.45e2 is (8(length)- 6(e_index)) - 2 = 0 therefore exp_length has only 10^0
            # eg 123.45e25 is (9(length)- 6(e_index)) - 2 = 1 therefore exp_length has 10^0 and 10^1
            for k in range(exp_length, -1, -1):
                power = power + (characters[ind] * 10 ** k)
                ind = ind + 1
            if minus_found:
                # if there is a negative in exponent then make power negative
                power = -power
            sum = whole_num * 10 ** power

        # if number is a whole number with no exponents
        # transforms array to number
        # eg 123.45e2 has dot index 3. before_dot = 2
        # subtracts 1 from before_dot with every iteration
        # iterates 1 x 10^2 + 2 x 10^1 + 3 x 10 ^0 = 123
        else:
            for i in range(length - 1, -1, -1):
                sum = sum + characters[ind] * 10 ** i
                ind = ind + 1

        return sum


class Stack(object):
    """
  The structure of a Stack.
  """
    def __init__(self):
        self.__container = list()

    def __is_empty(self):
        """
    Test if the stack is empty or not
    :return: True or False
    """
        return len(self.__container) == 0

    def push(self, element):
        """
    Add a new element to the stack
    :param element: the element you want to add
    :return: None
    """
        self.__container.append(element)

    def top(self):
        """
    Get the top element of the stack
    :return: top element
    """
        if self.__is_empty():
            return None
        return self.__container[-1]

    def pop(self):
        """
    Remove the top element of the stack
    :return: None or the top element of the stack
    """
        return None if self.__is_empty() else self.__container.pop()

    def clear(self):
        """
    We'll make an empty stack
    :return: self
    """
        self.__container.clear()
        return self


class Calculator(object):
    def __init__(self):
        self.__exp = ''

    def __validate(self):
        """
    We have to make sure the expression is legal.
    1. We only accept the `()` to specify the priority of a sub-expression. Notes: `[ {` and `] }` will be
    replaced by `(` and `)` respectively.
    2. Valid characters should be `+`, `-`, `*`, `/`, `(`, `)` and numbers(int, float)
    :return: True or False
    """
        if not isinstance(self.__exp, str):
            print('Error: {}: expression should be a string'.format(self.__exp))
            return False
        # Save the non-space expression
        val_exp = ''
        s = Stack()

        current = '0'
        previous = '0'
        for x in self.__exp:
            # We should ignore the space characters
            current = x
            if x == ' ':
                previous = '-1'
                continue
            else:
                previous = x

            if x == 'f' or x == 'F' or x == 'd' or x == 'D' and self.__is_digit(previous):
                continue

            if self.__is_digit(x) and previous == '-1':
                print('Error: it should not have space between digits')
                return False
            if self.__is_bracket(x) or self.__is_digit(x) or self.__is_operators(x) \
                    or x == '.' or x == 'e' or x == 'E' or x == "_":
                if x == '(':
                    s.push(x)
                elif x == ')':
                    s.pop()
                val_exp += x
            else:
                print('Error: {}: invalid character: {}'.format(self.__exp, x))
                return False
            previous = x

        if s.top():
            print('Error: {}: missing ")", please check your expression'.format(self.__exp))
            return False
        self.__exp = val_exp
        return True

    def __convert2postfix_exp(self):
        """
    Convert the infix expression to a postfix expression
    :return: the converted expression
    """
        # highest priority: ()
        # middle: * /
        # lowest: + -
        previous = '0'
        current = '0'
        converted_exp = ''
        stk = Stack()
        for x in self.__exp:
            current = x
            if self.__is_digit(x) or x == '.' or x == 'e' or x == 'E' or x == '_' or previous == 'e' or previous == 'E':
                converted_exp += x
            elif self.__is_operators(x):
                converted_exp += ' '
                tp = stk.top()
                if tp:
                    if tp == '(':
                        stk.push(x)
                        continue
                    x_pri = self.__get_priority(x)
                    tp_pri = self.__get_priority(tp)
                    if x_pri > tp_pri:
                        stk.push(x)
                    elif x_pri == tp_pri:
                        converted_exp += stk.pop() + ' '
                        stk.push(x)
                    else:
                        while stk.top():
                            if self.__get_priority(stk.top()) != x_pri:
                                converted_exp += stk.pop() + ' '
                            else:
                                break
                        stk.push(x)
                else:
                    stk.push(x)
            elif self.__is_bracket(x):
                converted_exp += ' '
                if x == '(':
                    stk.push(x)
                else:
                    while stk.top() and stk.top() != '(':
                        converted_exp += stk.pop() + ' '
                    stk.pop()
            previous = current
        # pop all the operators
        while stk.top():
            converted_exp += ' ' + stk.pop() + ' '

        return converted_exp

    def __get_result(self, operand_2, operand_1, operator):
        if operator == '+':
            return operand_1 + operand_2
        elif operator == '-':
            return operand_1 - operand_2
        elif operator == '*':
            return operand_1 * operand_2
        elif operator == '/':
            if operand_2 != 0:
                return operand_1 / operand_2
            else:
                print('Error: {}: divisor cannot be zero'.format(self.__exp))
                return None

    def __calc_postfix_exp(self, exp):
        """
    Get the result from a converted postfix expression
    e.g. 6 5 2 3 + 8 * + 3 + *
    :return: result
    """
        assert isinstance(exp, str)
        stk = Stack()
        exp_split = exp.strip().split()
        for x in exp_split:
            if self.__is_operators(x):
                # pop two top numbers in the stack
                r = self.__get_result(stk.pop(), stk.pop(), x)
                if r is None:
                    return None
                else:
                    stk.push(r)
            else:
                # push the converted number to the stack
                stk.push(
                    self.changeNumber(x))  # <----------------___----------- here change number originally stk.push(
                # float(x))
        return stk.pop()

    def changeNumber(self, expr):
        b = ConvertNums()
        expression = b.isAccepted(expr)
        return expression

    def __calc(self):
        """
    Try to get the result of the expression
    :return: None or result
    """
        # Validate
        if self.__validate():
            # Convert, then run the algorithm to get the result
            return self.__calc_postfix_exp(self.__convert2postfix_exp())
        else:
            return None

    def get_result(self, expression):
        """
    Get the result of an expression
    Suppose we have got a valid expression
    :return: None or result
    """
        self.__exp = expression.strip()
        return self.__calc()


    """
  Utilities
  """

    @staticmethod
    def __is_operators(x):
        return x in ['+', '-', '*', '/']

    @staticmethod
    def __is_bracket(x):
        return x in ['(', ')']

    @staticmethod
    def __is_digit(x):
        if x in '0123456789':
            return True

    @staticmethod
    def __get_priority(op):
        if op in ['+', '-']:
            return 0
        elif op in ['*', '/']:
            return 1



def main(input_string):
    c = Calculator()
    result = c.get_result(input_string)
    print('result: ', result)


if __name__ == '__main__':
    again = True

    # infinite loop asking user to enter a number
    # exits when entered q or quit
    print("enter 'q' or 'quit' to exit")
    while again:
        user_input = input('Please enter your floating point literal: ')
        if user_input == 'q' or user_input == "quit":
            again = False
        else:
            main(user_input)


# test (13.0*(1-1.0)+20.0)*5.0+100.0+((21e1f))-1e-1d
# test ((.5+2.50)*(.0__1)/10.f)
# test 15_____31.21___1 * 4 + (3f - 13_1d)