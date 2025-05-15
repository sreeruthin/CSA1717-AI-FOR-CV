% Facts: Parent-Child Relationships
parent(john, mary).
parent(john, paul).
parent(susan, mary).
parent(susan, paul).
parent(paul, lisa).
parent(paul, tom).

% Gender Facts
male(john). male(paul). male(tom).
female(susan). female(mary). female(lisa).

% Rules for Relationships
father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).
sibling(A, B) :- parent(P, A), parent(P, B), A \= B.
grandparent(G, C) :- parent(G, P), parent(P, C).
