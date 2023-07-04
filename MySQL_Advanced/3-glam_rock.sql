-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, DATEDIFF(year, formed, split) AS lifespan FROM metal_bands;