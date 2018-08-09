# q2 Write a function that takes string as input and output 
# to be int/float/string depending if the string can be 
# converted to float or integer type
def convert(in_string = ' '):
    out_value = None
    
    # check if it can be converted to int
    try:
        out_value = int(in_string)
        
    except ValueError:
        # check if it can be converted to float
        try:
            out_value = float(in_string)
            
        except ValueError:
            out_value = in_string
                     
    return out_value

# q3 Reformat this code to be more elegant
# converted to dictionary to increase readability
def pet_info():
    pet = {'category': 'dog', 'name': 'Fido', 'age':10}
    output = pet['name'] + ' the ' + pet['category'] + ' is ' + str(pet['age']) + ' years old.'
    return output

# q4 Implement a method that takes 3 numbers as input 
# and finds the minimum of the three without using the built-
# in min function
def get_minimum(e1, e2, e3):    
    try:
        minimum = e3
        if (e1 < e2 and e1 < e3):
            minimum = e1
        elif(e2 < e3):
            minimum = e2
            
    except TypeError:
        print('ERROR: arguments have to be numbers')
        minimum = None
        
    return minimum

# q5 Reformat this code to be more elegant
# 1. Removed multiple return statements and condensed into one
# 2. Added try except blocks for gracefule exit
# 3. I thought of adding separate fucntions for add, sub, mult, div but I
#    felt that would make the code much longer
def apply_operation(left_operand, right_operand, operator):
    result = None

    try:
        if operator == '+':
            result = left_operand + right_operand
            
        elif operator == '-':
            result = left_operand - right_operand
            
        elif operator == '*':
            result = left_operand * right_operand
            
        elif operator == '/':
            try:
                result = left_operand / right_operand
            except ZeroDivisionError:
                print('ERROR: Right operand cannot be zero')
                
        else:
            print('ERROR: Invalid operator')
            
    except TypeError:
        print('ERROR: Operands have to be numbers')
                    
    return result

# main with sample cases
if __name__== "__main__":
    in_str = '1.1'
    print('q2 output with input str %s' %(in_str)) 
    out = convert(in_str)
    print(out)
    
    print('q3 output')
    pet_str = pet_info()
    print(pet_str)
    
    print('q4 output')
    e1, e2, e3 = 10, 4, 14
    mini = get_minimum(e1, e2, e3)
    print('minimum of %d, %d and %d is %d' %(e1, e2, e3, mini))
    
    print('q5 output')
    l, r = 12, 13
    op = '*'
    result = apply_operation(l, r, op)
    print('%1.f %1.f %s = %1.f' %(l,r,op,result))
    
          
