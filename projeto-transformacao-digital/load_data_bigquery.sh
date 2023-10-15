#!/bin/bash
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2010
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2011
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2012
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2013
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2014
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2015
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2016
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2017
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2018
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2019
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2020
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2021
bq rm -f -t senac_dados_turismo_conjunto_dados.dados_2022
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2010 gs,//senac-dados-turismo/chegadas_2010.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2011 gs,//senac-dados-turismo/chegadas_2011.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2012 gs,//senac-dados-turismo/chegadas_2012.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2013 gs,//senac-dados-turismo/chegadas_2013.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2014 gs,//senac-dados-turismo/chegadas_2014.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2015 gs,//senac-dados-turismo/chegadas_2015.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2016 gs,//senac-dados-turismo/chegadas_2016.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2017 gs,//senac-dados-turismo/chegadas_2017.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2018 gs,//senac-dados-turismo/chegadas_2018.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2019 gs,//senac-dados-turismo/chegadas_2019.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2020 gs,//senac-dados-turismo/chegadas_2020.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2021 gs,//senac-dados-turismo/chegadas_2021.csv 
bq load --autodetect --field_delimiter=";" senac_dados_turismo_conjunto_dados.dados_2022 gs,//senac-dados-turismo/chegadas_2022.csv 