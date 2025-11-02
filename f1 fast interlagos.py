import fastf1
import os
import pandas as pd

os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache("cache")


session = fastf1.get_session(2022, "São paulo Grand Prix" ,"Q")
session.load()



laps = session.laps

best_laps = laps.groupby('Driver')['LapTime'].min().reset_index()


best_laps = best_laps.merge(session.results[['DriverNumber', 'Abbreviation', 'FullName']],
                            left_on='Driver', right_index=True, how='left')

best_laps = best_laps.sort_values(by='LapTime')


best_laps['LapTime'] = best_laps['LapTime'].dt.total_seconds().apply(lambda x: f"{x//60:.0f}:{x%60:05.3f}")


print("Melhores voltas – GP do Brasil 2022 (Qualificação)\n")
print(best_laps[['Abbreviation', 'FullName', 'LapTime']].to_string(index=False))



