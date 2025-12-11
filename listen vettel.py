import fastf1
session = fastf1.get_session(2019, 'Gilles Villanueve', 'R')
session.load(telemetry=False, laps=False, weather=False)
vettel = session.get_driver('VET')

print(f"Pronto {vettel['FirstName']}?")
