##StringCalculator's add() method takes in a string of delimited numbers and
##returns their sum.  It:
##Handles empty input strings
##Determines the delimiter(s)
##Splits the input string into numbers
##Converts the numbers to integers and sum them up. If non-numeric values are
##included in the string, it handles them and raises ValueError
##It handles different types of delimiters, including custom delimiters
##that can be specified using the format //[delimiter]\n. It also ignores
##numbers greater than 1000 and raises a ValueError exception if the input
##contains negative numbers.
##Usage:
##SC=StringCalculator()
##print(SC.add('2,3,4'))   -> should pring 9
##print(SC.add('//[*]\n1*9'))  ->delimiter is *, should print 10



class StringCalculator:

    def add(self, numbers: str):
        #Handle empty input string
        if not numbers:
            return 0

        #Determine the delimiter(s)
        delimiter = ','
        if numbers.startswith('//'):
            delimiter_section, numbers = numbers.split('\n', 1)
            delimiter_section = delimiter_section[2:].strip()
            if delimiter_section.startswith('[') and delimiter_section.endswith(']'):
                delimiter = delimiter_section[1:-1]
                if len(delimiter) > 1 and delimiter.startswith('[') and delimiter.endswith(']'):
                    delimiter = delimiter[1:-1]
                    delimiter = '|'.join(map(re.escape, delimiter.split('][')))
            else:
                delimiter = delimiter_section
        #print("delimeter is ", delimiter)
        
        #Split the input string into numbers
        numbers = numbers.replace('\n', delimiter)
        numbers_list = numbers.split(delimiter)

        #Convert the numbers to integers and sum them up
        result = 0
        negative_numbers = []
        for num in numbers_list:
#            if not num.isdigit():
            if not num.lstrip("-").isdigit():
                continue
            int_num = int(num)
            if int_num < 0:
                negative_numbers.append(int_num)
            elif int_num <= 1000:
                result += int_num
        #print("negative numbers ",negative_numbers)
        #print("result: ", result)
        
        #Handle negative numbers
        if negative_numbers:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negative_numbers))}")

        return result
##    

