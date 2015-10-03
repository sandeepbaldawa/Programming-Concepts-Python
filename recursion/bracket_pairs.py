# possible bracket pairs for given N
# N == 2 => ()() and (())
def bracket_pairs(l, r, curr):
    if l == 0 and r == 0:
        print "====== ACTUAL PRINTING ======", curr
    if l > 0:
        print "ENTERING LEFT ===>",l, r, curr
        bracket_pairs(l-1, r , curr + "(")
        print "EXITING LEFT ===>",l, r, curr
    if r > 0 and r > l:
        print "ENTERING RIGHT ===>",l, r, curr
        bracket_pairs(l, r-1, curr + ")")
        print "EXITING RIGHT ===>",l, r, curr


bracket_pairs(2,2,"")
