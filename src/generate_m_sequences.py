"""
Module to compute and display number of steps 
for all sequences given a range of m.
"""

from generate_sequence import sequence
import time

def m_sequences(m,n):
    """

    Parameters
    ----------
    m : base value for a sequence Cm. eg: m= 1 to 10000
        
    n :	max. number of terms per sequence Cm.
        

    Returns
    -------
	c_dict		: contains each m as key and its
				  sequence list as values.

	steps_dict	: contains each m as key and number of 
				  steps as values.

	eg: m=1
	c_dict[m]=[1,4,2,1]
	steps_dict[m]=4 --> in step 4 we get a 1 again

    """

    c_dict={}
    steps_dict={}
    steps=1

    for i in range(1,m+1):
    	c_dict[i],steps_dict[i]=sequence(i,n)


    return c_dict,steps_dict


if __name__ == '__main__':
	start=time.time()
	c_dict,steps_dict=m_sequences(m=10000,n=10000)
	end=time.time()

	# Priniting as a Table
	print(f'm	|	steps')
	for m,steps in steps_dict.items():
		print(f'm={m}	|	steps={steps}')

	"""
	Total time taken (in seconds) to calculate number of 
	steps for m sequences 
	"""
	print(f'Time taken={end-start}s')
	