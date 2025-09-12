def linha_um ():
    l1 = print('####  ####  ####  ####  ####')


def linha_dois ():
    l2 = print('#	  #	   #      #    #    #')

def linha_tres ():
    l3 = print('###   ###  #      ###   ####')

def linha_quatro ():
    l4 = print('#     ####  ####  #### #    #')

def desenho (l1, l2,l3, l4):
    l1()
    l2()
    l3()
    l2()
    l4()


desenho (linha_um, linha_dois, linha_tres, linha_quatro)