-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, split AS lifespan FROM metal_bands WHERE lifespan NOT IS NULL;