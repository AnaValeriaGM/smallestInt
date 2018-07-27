def solution(A):
    lst = A;
    newLst =[];
    #print (lst);
    N = list(range(1,100000));
    lst= sorted(lst);
    for x in lst:
        if x > 0:
           newLst.append(x);
    
    
    ran = len(newLst)+1;
    
    noRep = list(set(newLst));
    
           
    for i in range(ran):
        if N[i] not in noRep:
            res=(N[i]);
            break;
    return (res);

pass
