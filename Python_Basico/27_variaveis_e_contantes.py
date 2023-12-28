# CONSTANTES = VARIAVEIS QUE NAO MUDA
# MUSTAS CODICOES NO MESMO IF (RUIM)
#       <- CONTAGEN DE COMPLXIDADE(RUIM)

velocidade = 61 # VELOCIDADE ATUAL DO CARRO
local_carro =  100 # LOCAL EM QUE O CARRO ESTA NA ESTRADA 

RADAR_1 = 60 #VELOCIDADE MAXIMA DO RADAR 1
LOCAL_1 = 100 #LOCAL ONDE O RADAR 1 ESTA
RADAR_RANGE = 1 #A DISTANCIA ONDE O RADAR PEGA




if velocidade > RADAR_1:
    print('Velocidade Carro passou do radar_1')

if (local_carro >= (LOCAL_1 - RADAR_RANGE)\
     and local_carro <= (LOCAL_1 + RADAR_RANGE)\
        and velocidade > RADAR_1):
    print('Carro Multado em radar_1')
