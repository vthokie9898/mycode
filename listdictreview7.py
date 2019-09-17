#!/usr/bin/env python3

def main():

    my_var = []
    your_var = {}

    my_var += ['fluffy', 'kaya', 'max']
    my_var.append('butch')
    my_var.extend('tom')
    #print(my_var)
    #print(my_var[0::2])
    count = 1
    for kitty in my_var:
        print(kitty)
        your_var.update({kitty: count})
        count += 1

    #your_var.update({'dog': 'cujo'})
    #your_var['lizards'] = ['larry', 'spot', 'beardy']
    print(your_var)
    #print(your_var['lizards'][1])

    #del your_var['dog']
    #print(your_var)
main()
