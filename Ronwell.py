class Solution:
    """
    returns positive missing value
    """

    def __init__(self, List=[]):

        self.List = List

    def Missingvalue(self):

        self.List.sort ()

        if self.List[-1] == len ( self.List ):
            print ( len ( self.List ) + 1 )
        elif self.List[-1] < 0:
            print ( 1 )
        else:
            for i in range ( len ( self.List ) ):
                if self.List[i] == i + 1:
                    continue
                else:
                    print ( i + 1 )
                    break

if __name__ == '__main__':

    SolutionObject = Solution ( [3, 7, 4, 2] )
    Missingvalue = SolutionObject.Missingvalue ()