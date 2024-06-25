% sum_of_n(N, Sum) is true if Sum is the sum of the first N integers

% Base case: the sum of the first 0 integers is 0
sum_of_n(0, 0).

% Recursive case: the sum of the first N integers is N plus the sum of the first (N-1) integers
sum_of_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_of_n(N1, Sum1),
    Sum is N + Sum1.
