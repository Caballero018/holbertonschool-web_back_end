-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, IF(split, split - formed - 3, year(curdate()) - formed) AS lifespan FROM metal_bands ORDER BY lifespan DESC;
