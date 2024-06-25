% Define the facts: fruit and its color
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(grape, green).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(blueberry, blue).

% Querying for fruit colors with backtracking
% To find the color of a specific fruit, you can use:
% ?- fruit_color(Fruit, Color).

% Example Queries:
% ?- fruit_color(apple, Color).
% This will backtrack through all possible colors of an apple.

% ?- fruit_color(Fruit, yellow).
% This will backtrack through all fruits that are yellow.
