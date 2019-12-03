import markov362m as mk

#This is the coding part of HW4

m11 = mk.MarkovChain(title = "7.4.11")
m11.add_state("2,0")
m11.add_state("0,2")
m11.add_state("0,1.5")
m11.add_state("1,1")
m11.add_state("1,0.5")

p = 0.1
m11.add_transition("2,0","0,2", probability = p**2)
m11.add_transition("2,0","1,1", probability = 2*p*(1-p))
m11.add_transition("2,0","2,0", probability = (1-p)**2)
m11.add_transition("0,2","0,1.5", probability = 1)
m11.add_transition("0,1.5","1,1", probability = 1)
m11.add_transition("1,1","0,1.5", probability = p)
m11.add_transition("1,1","1,0.5", probability = 1-p)
m11.add_transition("1,0.5","1,1", probability = p)
m11.add_transition("1,0.5","2,0", probability = 1-p)

m11.compute()
print(m11.info())
print(m11.info_P())

m12 = mk.MarkovChain(title = "7.4.12")
m12.add_transition("Inspired","a", probability = 0.5)
m12.add_transition("Inspired","b", probability = 0.5)
m12.add_transition("a","Inspired", probability = 1/3)
m12.add_transition("a","Writer", probability = 2/3)
m12.add_transition("Writer","b", probability = 1)
m12.add_transition("b","Inspired", probability = 2/3)
m12.add_transition("b","Writer", probability = 1/3)

m12.compute()
print(m12.info())
print(m12.info_P())

m13 = mk.MarkovChain(title = "7.4.13")
m13.add_transition("2,2","1,2,R", probability = 1/2)
m13.add_transition("2,2","2,1,B", probability = 1/2)
m13.add_transition("1,2,R","1,1,B", probability = 2/3)
m13.add_transition("1,2,R","0,2,R", probability = 1/3)
m13.add_transition("1,1,B","1,1,B", probability = 1/2)
m13.add_transition("1,1,B","0,1,R", probability = 1/2)
m13.add_transition("0,1,R","0,0", probability = 1)
m13.add_transition("0,2,R","0,1,B", probability = 1)
m13.add_transition("0,1,B","0,1,B", probability = 1)
m13.add_transition("2,1,B","2,1,B", probability = 1/3)
m13.add_transition("2,1,B","1,1,R", probability = 2/3)
m13.add_transition("1,1,R","0,1,R", probability = 1/2)
m13.add_transition("1,1,R","1,0,B", probability = 1/2)
m13.add_transition("1,0,B","0,0", probability = 1)
m13.add_transition("0,0","0,0", probability = 1)

m13.compute()
print(m13.info())
print(m13.info_P())
# print(m13.P @ m13.P @ m13.P @ m13.P @ m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P @m13.P )

'''
output:
Basic info for: "7.4.11"
------------------------

 - states (5): ['2,0', '0,2', '0,1.5', '1,1', '1,0.5']

 - transitions (9): (2,0 -> 0,2, 0.01) , (2,0 -> 1,1, 0.18) , (2,0 -> 2,0, 0.81) , (0,2 -> 0,1.5, 1.0) , (0,1.5 -> 1,1, 1.0) , (1,1 -> 0,1.5, 0.1) , (1,1 -> 1,0.5, 0.9) , (1,0.5 -> 1,1, 0.1) , (1,0.5 -> 2,0, 0.9)

P-matrix info for: "7.4.11"
---------------------------
 - transition matrix:
[[0.81 0.01 0.   0.18 0.  ]
 [0.   0.   1.   0.   0.  ]
 [0.   0.   0.   1.   0.  ]
 [0.   0.   0.1  0.   0.9 ]
 [0.9  0.   0.   0.1  0.  ]]

 - order of states:{0: '2,0', 1: '0,2', 2: '0,1.5', 3: '1,1', 4: '1,0.5'}

Basic info for: "7.4.12"
------------------------

 - states (4): ['Inspired', 'a', 'b', 'Writer']

 - transitions (7): (Inspired -> a, 0.5) , (Inspired -> b, 0.5) , (a -> Inspired, 0.33333334) , (a -> Writer, 0.6666667) , (b -> Inspired, 0.6666667) , (b -> Writer, 0.33333334) , (Writer -> b, 1.0)

P-matrix info for: "7.4.12"
---------------------------
 - transition matrix:
[[0.    0.5   0.5   0.   ]
 [0.333 0.    0.    0.667]
 [0.667 0.    0.    0.333]
 [0.    0.    1.    0.   ]]

 - order of states:{0: 'Inspired', 1: 'a', 2: 'b', 3: 'Writer'}

Basic info for: "7.4.13"
------------------------

 - states (10): ['2,2', '1,2,R', '2,1,B', '1,1,B', '0,2,R', '0,1,R', '0,0', '0,1,B', '1,1,R', '1,0,B']

 - transitions (15): (2,2 -> 1,2,R, 0.5) , (2,2 -> 2,1,B, 0.5) , (1,2,R -> 1,1,B, 0.6666667) , (1,2,R -> 0,2,R, 0.33333334) , (2,1,B -> 2,1,B, 0.33333334) , (2,1,B -> 1,1,R, 0.6666667) , (1,1,B -> 1,1,B, 0.5) , (1,1,B -> 0,1,R, 0.5) , (0,2,R -> 0,1,B, 1.0) , (0,1,R -> 0,0, 1.0) , (0,0 -> 0,0, 1.0) , (0,1,B -> 0,1,B, 1.0) , (1,1,R -> 0,1,R, 0.5) , (1,1,R -> 1,0,B, 0.5) , (1,0,B -> 0,0, 1.0)

P-matrix info for: "7.4.13"
---------------------------
 - transition matrix:
[[0.    0.5   0.5   0.    0.    0.    0.    0.    0.    0.   ]
 [0.    0.    0.    0.667 0.333 0.    0.    0.    0.    0.   ]
 [0.    0.    0.333 0.    0.    0.    0.    0.    0.667 0.   ]
 [0.    0.    0.    0.5   0.    0.5   0.    0.    0.    0.   ]
 [0.    0.    0.    0.    0.    0.    0.    1.    0.    0.   ]
 [0.    0.    0.    0.    0.    0.    1.    0.    0.    0.   ]
 [0.    0.    0.    0.    0.    0.    1.    0.    0.    0.   ]
 [0.    0.    0.    0.    0.    0.    0.    1.    0.    0.   ]
 [0.    0.    0.    0.    0.    0.5   0.    0.    0.    0.5  ]
 [0.    0.    0.    0.    0.    0.    1.    0.    0.    0.   ]]

 - order of states:{0: '2,2', 1: '1,2,R', 2: '2,1,B', 3: '1,1,B', 4: '0,2,R', 5: '0,1,R', 6: '0,0', 7: '0,1,B', 8: '1,1,R', 9: '1,0,B'}

'''
