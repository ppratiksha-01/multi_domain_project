import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_monthly_temperature(monthly_avg, save_path, show=False):
    plt.figure(figsize=(8, 4))
    monthly_avg.plot(kind="line", marker="o")
    plt.title("Average Monthly Temperature")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_weather_summary(summary_counts, save_path, show=False):
    plt.figure(figsize=(8, 4))
    summary_counts.plot(kind="bar")
    plt.title("Weather Condition Frequency")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_wind_vs_temperature(wind, temp, save_path, show=False):
    plt.figure(figsize=(6, 4))
    plt.scatter(wind, temp, alpha=0.4)
    plt.xlabel("Wind Speed (km/h)")
    plt.ylabel("Temperature (°C)")
    plt.title("Wind Speed vs Temperature")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()

def plot_temperature_trend(dates, temperatures, save_path, show=False):
    plt.figure(figsize=(10, 4))
    plt.plot(dates, temperatures)
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_humidity_distribution(humidity, save_path, show=False):
    plt.figure(figsize=(6, 4))
    plt.hist(humidity, bins=20)
    plt.title("Humidity Distribution")
    plt.xlabel("Humidity")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_pressure_vs_temperature(pressure, temperature, save_path, show=False):
    plt.figure(figsize=(6, 4))
    plt.scatter(pressure, temperature, alpha=0.4)
    plt.title("Pressure vs Temperature")
    plt.xlabel("Pressure")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_correlation_heatmap(df_numeric, save_path, show=False):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_numeric.corr(), cmap="coolwarm", annot=True)
    plt.title("Weather Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()
