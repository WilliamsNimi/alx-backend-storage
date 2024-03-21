-- This is a script that lists all bands with Glam Rock style
SELECT band_name CASE WHEN split IS NULL THEN 2022 - formed ELSE split - formed END AS lifespan from metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
