import markov362m as mk

#This is the coding part for HW5, 9.3.10, a zoologist, Dr. Gurkensaft
madRat = mk.MarkovChain(title = "Crazy Dumb Rat")
madRat.add_state("1")
madRat.add_state("2")
madRat.add_state("3")
madRat.add_state("4")
madRat.add_state("5")
madRat.add_state("S")
madRat.add_state("F")

madRat.add_transition("1","2",1.0/2)
madRat.add_transition("1","3",1.0/2)
madRat.add_transition("3","1",1.0/3)
madRat.add_transition("3","4",1.0/3)
madRat.add_transition("3","S",1.0/3)
madRat.add_transition("2","1",1.0/3)
madRat.add_transition("2","4",1.0/3)
madRat.add_transition("2","F",1.0/3)
madRat.add_transition("4","2",1.0/3)
madRat.add_transition("4","3",1.0/3)
madRat.add_transition("4","5",1.0/3)
madRat.add_transition("5","4",1.0/2)
madRat.add_transition("5","F",1.0/2)
madRat.add_transition("S","S",1.0)
madRat.add_transition("F","F",1.0)

madRat.compute()
print(madRat.info_P())
print(madRat.F @ madRat.R)

