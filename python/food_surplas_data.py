import pandas as pd
df = pd.read_csv(r"D:\food_surplas_project\data\us_food_surplus_2024_sector_metrics.csv")
print(df[["sector", "metric", "value", "unit"]].to_string())
print(df.duplicated().sum())
print(df["sector"].unique())
# 
sector_surplus = df[df["metric"] == "surplus_food_generated"]
s_p = sector_surplus.sort_values(by="value", ascending=False)
print(s_p[["sector", "value", "unit"]])
trend_df = pd.read_csv(r"D:\food_surplas_project\data\us_food_surplus_2016_2024_trend.csv")
print(trend_df[["year", "value_million_US_short_tons"]].sort_values(by="value_million_US_short_tons", ascending=False))
start_value = trend_df["value_million_US_short_tons"].iloc[0]
end_value = trend_df["value_million_US_short_tons"].iloc[-1]
print(round(end_value - start_value, 2))
import matplotlib.pyplot as plt
trend_df.plot(
    x="year",
    y="value_million_US_short_tons",
    kind="line",
    marker="o",
    legend =False
)
plt.title("Estimated U.S. Food Surplus, 2016–2024")
plt.xlabel("Year")
plt.ylabel("Million U.S. short tons")
plt.show()
df.to_csv("us_food_surplus_2024_sector_metrics_practice.csv", index=False)