m = int(input('number of change : '))

def money (m):
    if m <= 0:
        return 'lacks'
    elif m - int(m) != 0:
        M = m - int(m)
        return 'there is no such coin — ' + str(M)
    else:
        money1 = m // 50
        money2 = m % 50 // 10
        money3 = m % 50 % 10 // 5
        money4 = m % 50 % 10 % 5
        return 'number of change: '+ '50коп.—' + str(money1) + ', 10коп.—' + str(money2) + ', 5коп.—' + str(money3)  + ', 1коп.—' + str(money4)

print (money(m))


