use_module(library(clpfd)).

list_sum([], 0).
list_sum([X|List], Sum) :-
    list_sum(List, Sum1),
    Sum = X + Sum1.

list_product([Item], Item).
list_product([Item1, Item2|Tail], Total) :-
    list_product([Item1*Item2|Tail], Total).


list_length_invariant(A, B, C) :-
    length(A, Len_A), 
    length(B, Len_B), 
    length(C, Len_C), 
    Len_A =< Len_B, Len_A =< Len_C.

list_sum_invariant(A, B, C) :-
    list_sum(A, Sum_A), list_sum(B, Sum_B), list_sum(C, Sum_C),
    Sum_A =:= Sum_B, Sum_B =:= Sum_C.

takeout(X, [X|R],R).
takeout(X, [F |R], [F|S]) :- takeout(X,R,S).

perm([X|Y],Z) :- perm(Y,W), takeout(X,Z,W).
perm([], []).

list_subseq([], [], []).
list_subseq([L|Ls], [L|As], Bs) :-
    list_subseq(Ls, As, Bs).

list_subseq([L|Ls], As, [L|Bs]) :-
    list_subseq(Ls, As, Bs).

find_good_subseq(L, As, OneThird, A_len) :-
    list_subseq(L, As, Bs),
    length(As, A_len),
    list_sum(As, A_sum),
    OneThird =:= A_sum,
    list_sum(Bs, B_sum),
    2*OneThird =:= B_sum.
    

solve(L, QE_A, Target_A_Len) :-
    list_sum(L, L_sum),
    OneThird is L_sum / 3,
    find_good_subseq(L, As, OneThird, Target_A_Len),
    list_product(As, A_product),
    MyResult is A_product,
    print(QE_A),
    QE_A = [MyResult]. 

find_all_solutions(L, Best, Target_A_Len) :-
    findall(X, solve(L, X, Target_A_Len), Bag),
    min_member(Best, Bag).



do_toy_problem(QE_A) :-
    TheToy=[1,2,3,4,5,7,8,9,10,11],
    find_all_solutions(TheToy, QE_A, 2).

do_the_real_problem(QE_A) :-
    MyList=[1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113],
    reverse(MyList, MyList2),
    find_all_solutions(MyList2, QE_A, 7).
