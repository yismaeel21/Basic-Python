#
# hw10pr1.py
#
# name: Yusuf Ismaeel
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False


    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew



    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def isBefore(self,d2):
        """A function that tests if the given date is before another date"""
        if self.year != d2.year:
            return self.year< d2.year
        if self.month != d2.month:
            return self.month<d2.month
        return self.day < d2.day
#
# be sure to add code for the Date class ABOVE--inside the class definition
#
    def isAfter(self,d2):
        """A function that tests if a given date is after another date"""
        if self.year != d2.year:
            return self.year> d2.year
        if self.month != d2.month:
            return self.month>d2.month
        return self.day > d2.day

    def tomorrow(self):
        """A function that gives you what day is right after a given date"""
        FDays = 28 + self.isLeapYear()
        DIM = [0,31,FDays,31,30,31,30,31,31,30,31,30,31]
        self.day+= 1
        if self.day > DIM[self.month]:
            self.day =1
            self.month+=1
            if self.month>12:
                self.year+=1
                self.month = 1

    def yesterday(self):
        """A function that gives you the date that is right before the given date"""
        FDays = 28 + self.isLeapYear()
        DIM = [0,31,FDays,31,30,31,30,31,31,30,31,30,31]
        self.day-= 1
        if self.day<1:
            self.month-=1
            if self.month<1:
                self.month = 12
                self.year-=1
            self.day = DIM[self.month]

    def addNDays(self,N):
        """A function that adds N days to a given date"""
        for x in range(N):
            self.tomorrow()

    def subNDays(self,N):
        """A function that removes N days from a given date"""
        for x in range(N):
            self.yesterday()

    def diff(self,d2):
        """A function that returns the difference between two dates"""
        self = self.copy()
        d2 = d2.copy()
        count = 0
        while self.isBefore(d2):
            self.tomorrow()
            count -=1
        while self.isAfter(d2):
            self.yesterday()
            count+=1
        return count

    def dow(self):
        DoW = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return DoW[((6+self.diff(Date(10,10,2010))%7+7)%7)]



d = Date(11, 13, 2018)    # Today?
d2 = Date(12, 21, 2018)   # winter break
ny = Date(1, 1, 2018)   # new year
nd = Date(1, 1, 2020)   # new decade
nc = Date(1, 1, 2100)   # new century
graduation = Date(5, 15, 2022)   # alter to suit!
vacation = Date(5, 17, 2019)     # ditto ~ summer break!
sm1 = Date(10, 28, 1929)    # stock market crash
sn2 = Date(10, 19, 1987)    # another s.m. crash: Mondays in Oct. are risky...
