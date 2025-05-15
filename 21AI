% Base Case: Move a single disk
hanoi(1, Source, Destination, _) :-
    format('Move disk 1 from ~w to ~w~n', [Source, Destination]).

% Recursive Case: Move N disks
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1, 
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),  % Move N-1 disks to auxiliary
    format('Move disk ~w from ~w to ~w~n', [N, Source, Destination]),
    hanoi(M, Auxiliary, Destination, Source).  % Move N-1 disks to destination
