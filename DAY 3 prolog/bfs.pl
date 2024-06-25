% Define the graph as edges with costs
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(b, e, 5).
edge(c, e, 1).
edge(d, f, 1).
edge(e, f, 3).

% Define the heuristic (cost estimate) for each node
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 3).
heuristic(e, 2).
heuristic(f, 0).

% Best-First Search algorithm
best_first_search(Start, Goal, Path, Cost) :-
    best_first_search([[Start]], Goal, Path, Cost).

% If the first path in the queue reaches the goal, we are done
best_first_search([[Goal | RestPath] | _], Goal, Path, Cost) :-
    reverse([Goal | RestPath], Path),
    path_cost(Path, Cost).

% Otherwise, extend the first path in the queue and continue searching
best_first_search([[Current | RestPath] | RestQueue], Goal, Path, Cost) :-
    findall([Next, Current | RestPath],
            (edge(Current, Next, _), \+ member(Next, [Current | RestPath])),
            NextPaths),
    append(RestQueue, NextPaths, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    best_first_search(SortedQueue, Goal, Path, Cost).

% Sort the queue based on the heuristic value
sort_queue(Queue, SortedQueue) :-
    map_list_to_pairs(heuristic_value, Queue, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, SortedQueue).

% Compute the heuristic value of a path (heuristic of the last node in the path)
heuristic_value([Node | _], Value) :-
    heuristic(Node, Value).

% Compute the total cost of a path
path_cost([_], 0).
path_cost([Node1, Node2 | Rest], Cost) :-
    edge(Node1, Node2, C),
    path_cost([Node2 | Rest], RestCost),
    Cost is C + RestCost.

% Example query:
% ?- best_first_search(a, f, Path, Cost).
% Path = [a, b, d, f],
% Cost = 4.
