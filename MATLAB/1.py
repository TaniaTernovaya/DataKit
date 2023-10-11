import pandas as pd
from tqdm import tqdm

# Создайте пример DataFrame (замените его вашей реальной таблицей)
data = {
    "REF": [1, 2, 3, 4, 5],
    "Code1": [111, 222, 333, 444, 555],
    "Code2": [555, 666, 111, 777, 333],
    "Code3": [999, 888, 777, 666, 555],
}

df = pd.DataFrame(data)

# Создайте словарь для хранения информации о совпадениях
matches = {}

# Итерируйтесь по элементам all_docks
for item in tqdm(data, desc="Finding duplicates", unit="item"):
    duplicate_rows = df[df.isin([item]).any(axis=1)]

    if len(duplicate_rows) > 1:
        for index, row in duplicate_rows.iterrows():
            columns_with_item = row.index[row == item].tolist()

            for col in columns_with_item:
                ref_value = row["REF"]
                col_index = int(col[4:])
                match_key = (ref_value, col_index)

                if match_key not in matches:
                    matches[match_key] = []

                matches[match_key].append((ref_value, col_index))

# Обновите DataFrame на основе информации о совпадениях
for (ref_value, col_index), match_list in matches.items():
    tmp = ", ".join(f"{ref}-{index}HH'm" for ref, index in match_list)
    df[f"REF{col_index}"] = df[f"REF{col_index}"].astype(object)
    df.loc[df["REF"] == ref_value, f"REF{col_index}"] = tmp

# Вывести результат
print(df)
