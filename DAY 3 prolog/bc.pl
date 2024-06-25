% Define facts
fact(sunny).
fact(weekend).

% Define rules
rule(go_for_hike) :- fact(sunny), fact(weekend).
rule(read_book) :- fact(raining), fact(weekend).
rule(stay_home) :- fact(raining), fact(weekend).
rule(play_board_games) :- fact(snowing), fact(weekend).

% Backward chaining mechanism
% Querying the system to see if a goal can be satisfied based on rules and facts

% Define a general predicate to infer a goal based on rules
can_do(Action) :- rule(Action).

% Define a predicate to check if a fact is true
can_do(Fact) :- fact(Fact).

% Example queries to test backward chaining:
% ?- can_do(go_for_hike).
% ?- can_do(read_book).
% ?- can_do(stay_home).
% ?- can_do(play_board_games).

% Running queries and displaying results
run_backward_chaining :-
    (can_do(go_for_hike) -> write('You can go for a hike.'), nl; write('You cannot go for a hike.'), nl),
    (can_do(read_book) -> write('You can read a book.'), nl; write('You cannot read a book.'), nl),
    (can_do(stay_home) -> write('You can stay home.'), nl; write('You cannot stay home.'), nl),
    (can_do(play_board_games) -> write('You can play board games.'), nl; write('You cannot play board games.'), nl).

% Example query to run backward chaining:
% ?- run_backward_chaining.
