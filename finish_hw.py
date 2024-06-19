import pandas as pd
import random

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})


def one_hot_encode(df, column):
    unique_values = df[column].unique()
    for unique_value in unique_values:
        df[f"{column}_{unique_value}"] = df[column].apply(
            lambda x: 1 if x == unique_value else 0
        )
    df.drop(column, axis=1, inplace=True)
    return df


one_hot_encoded_data = one_hot_encode(data, "whoAmI")
print(one_hot_encoded_data)
