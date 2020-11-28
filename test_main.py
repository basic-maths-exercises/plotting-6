import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        xv = np.linspace(-2*np.pi,2*np.pi,1000)
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==1000, "The number of points in your graph is incorrect" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(xv[i]-this_x[i])<1e-7, "One or more of your x values are not correct" )
            self.assertTrue( np.abs(np.sin(xv[i])-this_y[i])<1e-7, "One or more of your y values are not correct" )
