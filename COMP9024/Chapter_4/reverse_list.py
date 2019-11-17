def reverse(S, start, stop):
    """ Reverse elements in S list, from S[start] to S[stop-1] """

    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start+1, stop-1)
        
