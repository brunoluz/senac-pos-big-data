CREATE TABLE "senac-tpabd-projeto-final-glue-db"."gaming_anxiety_filtered"
WITH (format = 'Parquet', write_compression = 'SNAPPY')
AS
SELECT "GADE",
"Game",
"platform",
"Hours",
"Narcissism",
"Gender",
"Work",
"Degree",
"GAD_T",
"SPIN_T",
"SWL_T"
FROM "senac-tpabd-projeto-final-glue-db"."gaming_anxiety";