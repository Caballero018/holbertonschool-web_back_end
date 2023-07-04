-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (INT(formed) - INT(split)) FROM metal_bands;