CREATE TABLE `senac-dados-turismo.senac_dados_turismo_conjunto_dados.TURISMO_CONSOLIDADO` IF NOT EXISTS
(
  continente STRING,
  cod_continente INT64,
  pais STRING,
  cod_pais INT64,
  uf STRING,
  cod_uf INT64,
  via STRING,
  cod_via INT64,
  ano INT64,
  mes STRING,
  chegadas INT64
);