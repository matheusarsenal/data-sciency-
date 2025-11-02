import os
import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt

# 🔧 Cria a pasta de cache se não existir
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')

# 🎯 Carrega a sessão de corrida (R = Race)
session = fastf1.get_session(2024, 'Monaco Grand Prix', 'R')
session.load()

# 🟦 Seleciona as voltas mais rápidas de Norris e Piastri
norris_fastest = session.laps.pick_driver('NOR').pick_fastest()
piastri_fastest = session.laps.pick_driver('PIA').pick_fastest()

# ⚙️ Obtém os dados de telemetria (com distância percorrida)
norris_tel = norris_fastest.get_car_data().add_distance()
piastri_tel = piastri_fastest.get_car_data().add_distance()

# 🎨 Configuração de estilo dos gráficos
plotting.setup_mpl()
plt.style.use('seaborn-v0_8-darkgrid')

# 📊 Cria o gráfico comparando RPM e Marcha
fig, ax1 = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

# --- Gráfico 1: RPM (rotações por minuto)
ax1[0].plot(norris_tel['Distance'], norris_tel['RPM'], color='orange', label='Norris')
ax1[0].plot(piastri_tel['Distance'], piastri_tel['RPM'], color='cyan', label='Piastri')
ax1[0].set_ylabel('RPM (rotações por minuto)')
ax1[0].legend()
ax1[0].set_title('Comparativo de Trocas de Marcha - Norris vs Piastri (Monaco 2024)')

# --- Gráfico 2: Marchas
ax1[1].plot(norris_tel['Distance'], norris_tel['nGear'], color='orange', label='Norris')
ax1[1].plot(piastri_tel['Distance'], piastri_tel['nGear'], color='cyan', label='Piastri')
ax1[1].set_ylabel('Marcha Engatada')
ax1[1].set_xlabel('Distância (m)')
ax1[1].legend()

plt.tight_layout()
plt.show()
