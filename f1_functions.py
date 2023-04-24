import pandas as pd
import fastf1 as ff1

def get_lap_times(df, year, circuit, race_type):
    '''
    Get the lap times with telemetry for a given race.
    '''

    try:
        race = ff1.get_session(year, circuit, race_type)
        laps = race.load_laps(with_telemetry=True)

        # Add columns for the year and the circuit
        laps['Year'] = year
        laps['Circuit'] = circuit

        # Concatenate all the laps
        df = pd.concat([df, laps], ignore_index=True)

    except Exception as e:
        print(f"Error retrieving lap times for {year}, {circuit}: {e}")

    return df
