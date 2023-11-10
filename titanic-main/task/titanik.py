import pandas as pd


def get_titatic_dataframe() -> pd.DataFrame:
    df = pd.read_csv("/Users/tatanaternovaa/Downloads/titanic-main/task/train.csv")
    return df


def get_filled():
    df = get_titatic_dataframe()

    titles = df["Name"].str.extract(" ([A-Za-z]+)\.")
    df["Title"] = titles
    print(titles)
    median_mr = df[df["Name"].str.contains("Mr.")]["Age"].median()
    median_mrs = df[df["Name"].str.contains("Mrs.")]["Age"].median()
    median_miss = df[df["Name"].str.contains("Miss.")]["Age"].median()

    missing_mr = df[df["Name"].str.contains("Mr.")]["Age"].isnull().sum()
    missing_mrs = df[df["Name"].str.contains("Mrs.")]["Age"].isnull().sum()
    missing_miss = df[df["Name"].str.contains("Miss.")]["Age"].isnull().sum()

    median_mr = round(median_mr)
    median_mrs = round(median_mrs)
    median_miss = round(median_miss)

    result = [
        ("Mr.", missing_mr, median_mr),
        ("Mrs.", missing_mrs, median_mrs),
        ("Miss.", missing_miss, median_miss),
    ]

    return result


print(get_filled())
