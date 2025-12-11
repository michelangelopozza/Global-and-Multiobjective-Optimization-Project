The selection process is a key step in Evolutionary Algorithms. Selection drives the search process towards specific areas of the search space. The selection process operates on a population of individuals, and produces a population of "parents". These parents are then traditionally used by [[variation operators|Variation]].

The linear genome mapping process in Grammatical Evolution can generate [["invalid"|Representation#invalid-individuals]] individuals. Only valid individuals are selected by default in PonyGE2, however this can be changed with the argument:

    --invalid_selection

or by setting the parameter `INVALID_SELECTION` to `True` in either a parameters file or in the params dictionary.

## Tournament

Tournament selection selects `TOURNAMENT_SIZE` individuals from the overall population, sorts them, and then returns the single individual with the best fitness. Since no individuals are removed from the original population, it is possible that the same individuals may be selected multiple times to appear in multiple tournaments, although the same individual may not appear multiple times _in the same tournament_.

Activate with:

    --selection tournament

or by setting the parameter `SELECTION` to `tournament` in either a parameters file or in the params dictionary.

Tournament size is set by default at 2. This value can be changed with the argument:

    --tournament_size [INT]

or by setting the parameter `TOURNAMENT_SIZE` to `[INT]` in either a parameters file or in the params dictionary, where `[INT]` is an integer which specifies the tournament size.

## Truncation

Truncation selection takes an entire population, sorts it, and returns the best `SELECTION_PROPORTION` of that population.

Activate with:

    --selection truncation

or by setting the parameter `SELECTION` to `truncation` in either a parameters file or in the params dictionary.

Selection proportion is set by default at 0.5 (i.e. return the top 50% of the population). This value can be changed with the argument:

    --selection_proportion [NUM]

or by setting the parameter `SELECTION_PROPORTION` to `[NUM]` in either a parameters file or in the params dictionary, where `[NUM]` is a float between 0 and 1.

*__NOTE__ that unless the specified* `SELECTION_PROPORTION` *is 1.0 (i.e. 100%), truncation selection necessarily returns a selected parent population that is smaller in size than the original population.*

## NSGA2

NSGA2 selection performs a pareto tournament selection on `TOURNAMENT_SIZE` individuals. Pareto selection takes into account both the pareto front of the individuals (to check for dominance) and the crowding comparison of the individuals (to ensure dispersion on the fronts). For more details on the NSGA-II operator see [[[Deb et al., 2002|References]]].

Activate with:

    --selection nsga2_selection

or by setting the parameter `SELECTION` to `nsga2_selection` in either a parameters file or in the params dictionary.

*__NOTE__ that NSGA2 selection can only be used in conjunction with [[multiple objective optimisation|Evaluation#multiple-objective-optimisation]] problems.*

*__NOTE__ that multi-objective optimisation compatible operators require a* `multi_objective = True` *attribute*.
