def do_twice (f, valor):
    f ()
    f()

def print_spam():
    print ('isa')

do_twice(print_spam, valor)

