import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt

# Ativa cache para não baixar os mesmos dados várias vezes
fastf1.Cache.enable_cache('cache')

# Carrega uma sessão — exemplo: corrida de 2024, GP da Itália
session = fastf1.get_session(2024, 'Italian Grand Prix', 'R')
session.load()

# Seleciona dois pilotos para comparar voltas
ver = session.laps.pick_driver('VER').pick_fastest()
ham = session.laps.pick_driver('HAM').pick_fastest()

# Obtém telemetria
ver_tel = ver.get_car_data().add_distance()
ham_tel = ham.get_car_data().add_distance()

# Cria gráfico comparando velocidade
plt.plot(ver_tel['Distance'], ver_tel['Speed'], label='Verstappen')
plt.plot(ham_tel['Distance'], ham_tel['Speed'], label='Hamilton')
plt.xlabel('Distância (m)')
plt.ylabel('Velocidade (km/h)')
plt.legend()
plt.show()
