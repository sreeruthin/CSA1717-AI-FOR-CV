% Base case: sum of numbers from 1 to 0 is 0
sum_n(0, 0).

% Recursive case: sum of numbers from 1 to N
sum_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_n(N1, Sum1),
    Sum is Sum1 + N.
