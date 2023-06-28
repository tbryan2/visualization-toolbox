from typing import List, Dict, Optional, Tuple
import pandas as pd
import fastf1 as ff1


class F1Session:
    '''
    Class to load and preprocess F1 session data.
    '''

    def __init__(self, data: List[Dict[str, str]]):
        self.data = data
        self.index = 0

    @staticmethod
    def _add_year_circuit(df: pd.DataFrame, year: str, event_name: str) -> pd.DataFrame:
        df['Year'] = year
        df['EventName'] = event_name
        return df

    def get_lap_times(self, year: str, circuit: str, session_type: str) -> Optional[pd.DataFrame]:
        '''
        Get the lap times with telemetry for a given race.
        '''
        try:
            session, event_name = self.load_session(
                year, circuit, session_type)
            laps = session.laps
            return self._add_year_circuit(laps, year, event_name)

        except KeyError as error:
            print(f"Error retrieving lap times for {year}, {circuit}: {error}")
            return None

    def get_session_results(self, year: str, circuit: str, session_type: str) -> Optional[pd.DataFrame]:
        '''
        Get the results of the session.
        '''`
        try:
            session, event_name = self.load_session(
                year, circuit, session_type)
            results = session.results
            return self._add_year_circuit(results, year, event_name)

        except KeyError as error:
            print(
                f"Error retrieving session results for {year}, {circuit}: {error}")
            return None

    def load_session(self, year: str, circuit: str, session_type: str) -> Tuple:
        '''
        Load the F1 session and return the session and event name.
        '''
        session = ff1.get_session(year, circuit, session_type)
        session.load()
        return session, session.event.EventName

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        session_data = self.data[self.index]
        year = session_data['year']
        circuit = session_data['circuit']
        session_type = session_data['session_type']
        self.index += 1

        lap_times = self.get_lap_times(year, circuit, session_type)
        session_results = self.get_session_results(year, circuit, session_type)

        if lap_times is None or session_results is None:
            return None

        return {"lap_times": lap_times, "session_results": session_results}
