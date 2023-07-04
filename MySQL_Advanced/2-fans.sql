-- Script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, SUM(nb_fans) FROM metal_bands WHERE nb_fans > 1 ORDER BY nb_fans DESC GROUP BY origin;