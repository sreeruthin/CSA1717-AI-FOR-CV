% Facts: Birds that cannot fly
flightless(ostrich).
flightless(penguin).
flightless(kiwi).

% Rule: A bird can fly unless it is flightless
can_fly(Bird) :- \+ flightless(Bird).

% Rule: A bird cannot fly if it is in the flightless list
cannot_fly(Bird) :- flightless(Bird).
