

def sequence(m,n):
    """

    Parameters
    ----------
    m : base value for a sequence Cm.
        
    n :	max. number of terms per sequence Cm.
        

    Returns
    -------
	c 	  : sequence Cm as a list.
	steps :	number of steps to reach 1 in the sequence
    """

    c=[m] # maintains sequence Cm as a list
    steps=0

    for i in range(1,n):
        """
    	Conditions to compute next term in the sequence 
    	based of whether last term was even or odd.
    	"""
        if (c[i-1]) % 2==0:
        	val=c[i-1]/2
        else:
        	val=3*c[i-1] + 1

        c.append(val)
        
        # compute steps till 1 occurs and breaks
        if val==1:
        	steps=i+1
        	break

    return c,steps

if __name__ == '__main__':
	c,steps=sequence(10000,10000)
	print(c,steps)




