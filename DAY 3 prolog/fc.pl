% Define initial facts
fact(sunny).
fact(weekend).

% Define rules
rule(go_for_hike) :- fact(sunny), fact(weekend).
rule(read_book) :- fact(raining), fact(weekend).
rule(stay_home) :- fact(raining), fact(weekend).
rule(play_board_games) :- fact(snowing), fact(weekend).

% Forward chaining mechanism
forward_chaining :-
    rule(Action),
    \+ fact(Action), % If the action is not already a fact
    assert(fact(Action)), % Assert the action as a new fact
    write('New fact deduced: '), write(Action), nl,
    fail. % Force backtracking to find all possible actions
forward_chaining.

% Query to start forward chaining and show all deduced facts
run_forward_chaining :-
    retractall(fact(_)), % Clear all existing facts
    assert(fact(sunny)), % Add initial facts
    assert(fact(weekend)),
    forward_chaining,
    list_facts.

% List all deduced facts
list_facts :-
    fact(F),
    write('Fact: '), write(F), nl,
    fail.
list_facts.

% Example query to start forward chaining:
% ?- run_forward_chaining.
