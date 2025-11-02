import os
import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt


os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')


session = fastf1.get_session(2024, 'Monaco Grand Prix', 'R')
session.load()


norris_fastest = session.laps.pick_driver('NOR').pick_fastest()
piastri_fastest = session.laps.pick_driver('PIA').pick_fastest()


norris_tel = norris_fastest.get_car_data().add_distance()
piastri_tel = piastri_fastest.get_car_data().add_distance()


plotting.setup_mpl()
plt.style.use('seaborn-v0_8-darkgrid')


fig, ax1 = plt.subplots(2, 1, sharex=True, figsize=(10, 8))


ax1[0].plot(norris_tel['Distance'], norris_tel['RPM'], color='orange', label='Norris')
ax1[0].plot(piastri_tel['Distance'], piastri_tel['RPM'], color='cyan', label='Piastri')
ax1[0].set_ylabel('RPM (rotações por minuto)')
ax1[0].legend()
ax1[0].set_title('Comparativo de Trocas de Marcha - Norris vs Piastri (Monaco 2024)')


ax1[1].plot(norris_tel['Distance'], norris_tel['nGear'], color='orange', label='Norris')
ax1[1].plot(piastri_tel['Distance'], piastri_tel['nGear'], color='cyan', label='Piastri')
ax1[1].set_ylabel('Marcha Engatada')
ax1[1].set_xlabel('Distância (m)')
ax1[1].legend()

plt.tight_layout()
plt.show()
