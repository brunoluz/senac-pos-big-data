create table `senac-dados-turismo.senac_dados_turismo_conjunto_dados.turismo_consolidado` as 
select Continente as continente, Ordem_continente as cod_continente, Pa__s as pais, Ordem_pa__s as cod_pais, UF as uf, Ordem_UF as cod_uf, Via_de_acesso as via, Ordem_via_de_acesso as cod_via, ano, M__s as mes, Ordem_m__s, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2010`
union all
SELECT Continente as continente, Ordem_continente as cod_continente, Pa__s as pais, Ordem_pa__s as cod_pais, UF as uf, Ordem_UF as cod_uf, Via_de_acesso as via, Ordem_via_de_acesso as cod_via, ano, M__s as mes, Ordem_m__s, Chegadas as chegadas 
FROM `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2011`
union all
SELECT Continente as continente, Ordem_continente as cod_continente, Pa__s as pais, Ordem_pa__s as cod_pais, UF as uf, Ordem_UF as cod_uf, Via_de_acesso as via, Ordem_via_de_acesso as cod_via, ano, M__s as mes, Ordem_m__s, Chegadas as chegadas 
FROM `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2012`
union all
SELECT Continente as continente, Ordem_continente as cod_continente, Pa__s as pais, Ordem_pa__s as cod_pais, UF as uf, Ordem_UF as cod_uf, Via_de_acesso as via, Ordem_via_de_acesso as cod_via, ano, M__s as mes, Ordem_m__s, Chegadas as chegadas 
FROM `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2013`
union all
SELECT Continente as continente, Ordem_continente as cod_continente, Pa__s as pais, Ordem_pa__s as cod_pais, UF as uf, Ordem_UF as cod_uf, Via_de_acesso as via, Ordem_via_de_acesso as cod_via, ano, M__s as mes, Ordem_m__s, Chegadas as chegadas 
FROM `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2014`
union all
SELECT Continente as continente, Ordem_continente as cod_continente, Pa__s as pais, Ordem_pa__s as cod_pais, UF as uf, Ordem_UF as cod_uf, Via_de_acesso as via, Ordem_via_de_acesso as cod_via, ano, M__s as mes, Ordem_m__s, Chegadas as chegadas 
FROM `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2015`
union all
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2016`
union all 
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2017`
union all 
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2018`
union all
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2019`
union all
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2020`
union all 
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2021`
union all
select Continente as continente, cod_continente, Pa__s as pais, cod_pais, UF as uf, cod_uf, Via as via, cod_via, ano, M__s as mes, cod_mes, Chegadas as chegadas
from `senac-dados-turismo.senac_dados_turismo_conjunto_dados.dados_2022`