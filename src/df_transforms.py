from numpy import nan
from pandas import DataFrame, date_range, to_datetime


def cast_df(df: DataFrame) -> DataFrame:
    df["date"] = to_datetime(df["date"])
    df["pull_up_session"] = df["pull_up_session"].astype(int)
    df["indoor_session"] = df["indoor_session"].astype(int)
    df["outdoor_session"] = df["outdoor_session"].astype(int)
    df["hang_session"] = df["hang_session"].astype(int)
    return df

def add_empty_dates(df: DataFrame) -> DataFrame:
    all_dates = date_range(start=df["date"].min(), end=df["date"].max())
    df = df.set_index("date").reindex(all_dates).rename_axis("date").reset_index()
    for col in ["pull_up_session", "indoor_session", "outdoor_session", "hang_session"]:
        df[col] = df[col].fillna(int(0)).astype(int)
    return df

def get_session_type(indoor_col, outdoor_col):
    if indoor_col > 0:
        return "indoor"
    if outdoor_col > 0:
        return "outdoor"
    return nan

def get_max_v_grade(session_type_col, max_v_grade_col, session_type):
    if session_type_col == session_type:
        return max_v_grade_col
    return nan

def session_type_col(df: DataFrame) -> DataFrame:
    df["session_type"] = df.apply(
        lambda x: get_session_type(x["indoor_session"], x["outdoor_session"]), axis=1
    )
    return df

def max_v_grade_cols(df: DataFrame) -> DataFrame:
    df["max_indoor_v_grade"] = df.apply(
        lambda x: get_max_v_grade(x["session_type"], x["max_v_grade"], "indoor"), axis=1
    )
    df["max_outdoor_v_grade"] = df.apply(
        lambda x: get_max_v_grade(x["session_type"], x["max_v_grade"], "outdoor"), axis=1
    )
    return df
