import math
def area(n,s):
        '''
        n type: int
            number of sides
        s type: int or float
            the length of each side

        Returns:The area of a regular polygon
        '''
        x=(0.25*n*s*s)/math.tan(math.pi/n)
        return x
def s_perimeter(n,s):
        '''
        n type: int
            number of sides
        s type: int or float
            the length of each side

        Returns:The square of the perimeter of the regular polygon
        '''
        y=(n*s)**2
        return y
    
def polysum(n,s):
    '''
    n type: int
        number of sides
    s type: int or float
        the length of each side 
        
    Returns:the sum of the area and square of the perimeter of the regular polygon,rounded to 4 decimal places
    '''
    if n<3:
        return False
    else:
        result=area(n,s)+s_perimeter(n,s)
        return round(result,4)
    
