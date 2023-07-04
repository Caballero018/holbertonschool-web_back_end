-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, formed, split FROM metal_bands WHERE split IS NOT NULL;