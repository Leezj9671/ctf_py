from timedec import UsedTimeDec

startyear = 1980
startmonth = 1
startday = 1
endyear = 2017
endmonth = 12
endday = 31
runyue = [2, 4, 6, 9, 11]

@UsedTimeDec
def main():
    m1 = startmonth
    m2 = endmonth if startyear == endyear else 12
    d1 = startday
    d2 = 31
    gen_list = []
    for y in range(startyear, endyear + 1):
        for m in range(m1, m2 + 1):
            if endyear == y and endmonth == m:
                d2 = endday
            else:
                d2 = 30 if m in runyue else 31
            for d in range(d1, d2 + 1):
                gen_list.append('{}{}{}\n'.format(y, m, d))
                gen_list.append('{}{}{}\n'.format(y % 100, m, d))
                mm = '0' + str(m) if m < 10 else str(m)
                dd = '0' + str(d) if d < 10 else str(d)
                gen_list.append('{}'.format(y) + mm + dd + '\n')
                gen_list.append('{}'.format(y % 100) + mm + dd + '\n')
            d1 = 1
        m1 = 1
        m2 = endmonth if endyear == y+1 else 12

    filename = 'birthdate{}-{}-{}TO{}-{}-{}.txt'.format(startyear, startmonth, startday, endyear, endmonth, endday)

    with open(filename, 'w') as f:
        f.writelines(gen_list)

if __name__ == '__main__':
    main()
    