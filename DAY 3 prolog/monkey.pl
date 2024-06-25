% Initial state of the problem
initial_state([
    at(floor),
    at(box, floor),
    at(banana, ceiling),
    on(box, floor),
    has_not(banana)
]).

% Define actions that the monkey can perform
action(grab) :-
    state_at(at(floor)),
    state_at(at(box, floor)),
    state_at(at(banana, ceiling)),
    state_at(on(box, floor)),
    state_at(has_not(banana)).

action(climb) :-
    state_at(at(floor)),
    state_at(at(box, floor)),
    state_at(at(banana, ceiling)),
    state_at(on(box, floor)),
    state_at(has_not(banana)).

action(push) :-
    state_at(at(floor)),
    state_at(at(box, floor)),
    state_at(at(banana, ceiling)),
    state_at(on(box, floor)),
    state_at(has_not(banana)).

% Define state transitions based on actions
% grab action
result(State, grab, Result) :-
    select(at(floor, State), State, State1),
    select(at(box, floor, State1), State1, State2),
    select(at(banana, ceiling, State2), State2, State3),
    select(on(box, floor, State3), State3, State4),
    select(has_not(banana, State4), State4, Result),
    assertz(state_at(has(banana))).

% climb action
result(State, climb, Result) :-
    select(at(floor, State), State, State1),
    select(at(box, floor, State1), State1, State2),
    select(at(banana, ceiling, State2), State2, State3),
    select(on(box, floor, State3), State3, State4),
    select(has_not(banana, State4), State4, Result).

% push action
result(State, push, Result) :-
    select(at(floor, State), State, State1),
    select(at(box, floor, State1), State1, State2),
    select(at(banana, ceiling, State2), State2, State3),
    select(on(box, floor, State3), State3, State4),
    select(has_not(banana, State4), State4, Result).

% Define goal state
goal_state([
    at(floor),
    at(box, floor),
    at(banana, ceiling),
    on(box, floor),
    has(banana)
]).

% Plan function to find a sequence of actions to reach the goal
plan(State, Actions, VisitedStates) :-
    goal_state(Goal),
    plan(State, Goal, Actions, VisitedStates).

% Base case for plan
plan(State, Goal, [], _) :-
    subset(Goal, State).

% Recursive case for plan
plan(State, Goal, [Action | Actions], VisitedStates) :-
    action(Action),
    result(State, Action, NextState),
    \+ member(NextState, VisitedStates),
    plan(NextState, Goal, Actions, [NextState | VisitedStates]).

% Helper predicate to check subset of elements
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).
