# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.concat(
#     pd.read_excel(r"C:\Users\USR\Downloads\\Test_Yakymenko.xlsx", sheet_name=None),
#     ignore_index=True,
# )
# numeric_columns = df[["Metric Store", "Metric population"]]
# correlation_matrix = numeric_columns.corr()
# plt.figure(figsize=(7, 3))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.xticks(rotation=45)
# plt.show()


def prepare_data(data):
    x_data = data.sort()
    return x_data


print(prepare_data([2, 34, 5, 6, 7, 8, 1, -90, 23]))
