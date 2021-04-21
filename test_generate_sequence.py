"""
Unit test for sequence generators.
"""


from src.generate_sequence import sequence
from src.generate_m_sequences import m_sequences

def test_sequence():
    """ Testing sequence generator for a single m """

    c,steps=sequence(m=1,n=10)
    print(c,steps)
    
    assert c==[1,4,2,1]
    
    assert steps==4

def test_m_sequences():
    """ 
    Testing sequence generator for all sequences m=1 to M 
    Each sequence has maximum n terms. 
    However, the sequence will stop if it encounters a 1 and
    returns the number of steps needed to reach this state.
    """
    c_dict,steps_dict=m_sequences(m=10000,n=10000)

    assert c_dict[4]==[4,2,1]

    assert steps_dict[4]==3

    assert steps_dict[1]==4

    # checking sequence and steps for the last term
    assert c_dict[10000][-3:]==[4,2,1]

    assert steps_dict[10000]==30

	