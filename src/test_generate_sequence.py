"""
Unit test for sequence generators.
"""
import unittest

from generate_sequence import sequence
from generate_m_sequences import m_sequences



class TestGenerateSequences(unittest.TestCase):
    def test_sequence(self):
        """ Testing sequence generator for a single m """

        c,steps=sequence(m=1,n=10)
        print(c,steps)
        
        self.assertEqual(c,[1,4,2,1])
        
        self.assertEqual(steps,4)

    def test_m_sequences(self):
        """ 
        Testing sequence generator for all sequences m=1 to M 
        Each sequence has maximum n terms. 
        However, the sequence will stop if it encounters a 1 and
        returns the number of steps needed to reach this state.
        """
        c_dict,steps_dict=m_sequences(m=10000,n=10000)

        self.assertEqual(c_dict[4],[4,2,1])

        self.assertEqual(steps_dict[4],3)

        self.assertEqual(steps_dict[1],4)

        # checking sequence and steps for the last term
        self.assertEqual(c_dict[10000][-3:],[4,2,1])

        self.assertEqual(steps_dict[10000],30)


if __name__ == '__main__':
    unittest.main()