some_list = ['foo', 'bar', 'baz']
for index, value in enumerate(some_list):
    print('i: {}, v: {}'.format(index,value))

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
seq3 = ['apple', 'raspberry', 'banana'] 
for a, b, c in zip(seq1, seq2, seq3):
    print('a: {}, b: {}, c: {}'.format(a, b, c, ))
    print('b: {1}, c: {2}, a: {0}'.format(a, b, c, ))