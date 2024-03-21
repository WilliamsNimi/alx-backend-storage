-- This is a script that lists all bands with Glam Rock style
Select band_name CASE WHEN split is NULL THEN 2022 - formed ELSE split - formed END as lifespan from metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
