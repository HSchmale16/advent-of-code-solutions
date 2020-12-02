use_module(library(clpfd)).

list_sum([], 0).
list_sum([X|List], Sum) :-
    list_sum(List, Sum1),
    Sum = X + Sum1.

list_product([Item], Item).
list_product([Item1, Item2|Tail], Total) :-
    list_product([Item1*Item2|Tail], Total).

list_length([], 0).
list_length([_|T], N) :- N is N1+1, list_length(T, N1).


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

list_subseq_subseq_subseq([], [], [], []).
list_subseq_subseq_subseq([L|Ls], [L|As], Bs, Cs) :-
    list_subseq_subseq_subseq(Ls, As, Bs, Cs).
list_subseq_subseq_subseq([L|Ls], As, [L|Bs], Cs) :-
    list_subseq_subseq_subseq(Ls, As, Bs, Cs).
list_subseq_subseq_subseq([L|Ls], As, Bs, [L|Cs]) :-
    list_subseq_subseq_subseq(Ls, As, Bs, Cs).


solve(L, QE_A) :-
    list_subseq_subseq_subseq(L, A, B, C),
    list_sum_invariant(A, B, C),
    list_length_invariant(A, B, C),
    list_product(A, QE_A)
    .

do_the_real_problem(QE_A) :-
    MyList=[1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113],
    solve(MyList, QE_A).

