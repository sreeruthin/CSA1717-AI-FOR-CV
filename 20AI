% Facts: Planets Database (Name, Type, Distance from Sun in million km)
planet(mercury, terrestrial, 57).
planet(venus, terrestrial, 108).
planet(earth, terrestrial, 150).
planet(mars, terrestrial, 228).
planet(jupiter, gas_giant, 778).
planet(saturn, gas_giant, 1430).
planet(uranus, ice_giant, 2870).
planet(neptune, ice_giant, 4500).

% Find planets by type
find_by_type(Type, Planet) :- planet(Planet, Type, _).

% Find distance of a planet from the Sun
find_distance(Planet, Distance) :- planet(Planet, _, Distance).

% List all planets
list_planets :- planet(P, T, D), write(P-T-D), nl, fail; true.

% Find planets within a distance range
within_distance(Max, Planet) :- planet(Planet, _, D), D =< Max.
 
