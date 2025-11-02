import os
import fastf1
import pandas as pd
from matplotlib import pyplot as plt
from fastf1 import plotting


os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')


session = fastf1.get_session(2025, 'Azerbaijan Grand Prix', 'Q')
session.load()


laps = session.laps


best_laps = laps.groupby('Driver')['LapTime'].min().reset_index()


best_laps = best_laps.merge(session.results[['Abbreviation', 'FullName']],
                            left_on='Driver', right_index=True, how='left')


best_laps = best_laps.sort_values(by='LapTime')


best_laps['Seconds'] = best_laps['LapTime'].dt.total_seconds()
best_laps['LapTimeStr'] = best_laps['LapTime'].dt.total_seconds().apply(lambda x: f"{x//60:.0f}:{x%60:05.3f}")


print("Melhores voltas – GP de arzebaijão 2025 (Qualificação)\n")
print(best_laps[['Abbreviation', 'FullName', 'LapTimeStr']].to_string(index=False))


plotting.setup_mpl()

plt.figure(figsize=(10, 6))
bars = plt.barh(best_laps['Abbreviation'], best_laps['Seconds'], color='orange')
plt.gca().invert_yaxis()


for bar, tempo in zip(bars, best_laps['LapTimeStr']):
    plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
             tempo, va='center', fontsize=9)


plt.title('Melhores Voltas - Qualificação (aezebaijão 2025)')
plt.xlabel('Tempo de Volta (segundos)')
plt.ylabel('Piloto')
plt.tight_layout()
plt.show()
plt.show(block=True)

