import math
################################################################################
## Class Triangle
################################################################################

class Triangle( object ):
    
    def __init__( self, sideA, sideB, sideC):
        """
        Initialize an object of type Triangle.
        """
        
        self.__sideA = sideA
        self.__sideB = sideB
        self.__sideC = sideC
        self.__valid = False
        self.triangle_sides = (sideA, sideB, sideC)

    def __validate( self ):
        #
        # Check the three sides to determine if a Triangle is valid
           
            if math.fsum(self.triangle_sides) <= 180:
                print "This triange is valid"
            else:
                pass
    
    def __repr__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        print self.__sideA
        print self.__sideB
        print self.__sideC


    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        print self.triangle_sides
        return

    def is_valid( self ):
        """
        Return a Boolean (is the Triangle valid?).
        """
        
        if math.fsum(self.triangle_sides) <= 180:
                print True
        else:
            pass

    def is_equilateral( self ):
        """
        Return a Boolean (is the Triangle an equilateral triangle?)
        """
        if self.__sideA == self.__sideB == self.__sideC:
            return 'equilateral'

    def is_isosceles( self ):
        """
        Return a Boolean (is the Triangle an isosceles triangle?)
        """
        if(self.__sideA == self.__sideB) or (self.__sideB == self.__sideC):
            return 'isoceles'

    def is_scalene( self ):
        """
        Return a Boolean (is the Triangle a scalene triangle?)
        """
        if self.__sideA != self.__sideB != self.__sideC:
            return 'scalene'

    def sides( self ):
        """
        Return a tuple containing the Triangle's three sides.
        """
        return [self.__sideA, self.__sideB, self.__sideC]
    
    def angles( self ):
        """
        Return a tuple containing the Triangle's three angles (in degrees) 
        """
    
        angle_a = ((self.__sideB**2) + (self.__sideC**2) - (self.__sideA**2))/ (2 * (self.__sideB * self.__sideC))
        ans1 = math.acos(angle_a)
    	
    	angle_b = (self.__sideA**2 + self.__sideC**2 - self.__sideB**2)/ (2 * (self.__sideA * self.__sideC))
        ans2 = math.acos(angle_b)

    	angle_c = (self.__sideA**2 + self.__sideB**2 - self.__sideC**2)/ (2 * (self.__sideA * self.__sideB))
    	ans3 = math.acos(angle_c)

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """
        return math.fsum(self.triangle_sides)
        
    def area( self ):
        """
        Return a float representing the Triangle's area.
        """
        
        return 0.5*(self.__sideA*self.__sideB)
        
    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """

        return self.triangle_sides*2