import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_daily_cases(dates, confirmed, save_path, show=False):
    plt.figure(figsize=(10, 4))
    plt.plot(dates, confirmed)
    plt.title("Daily Confirmed COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_deaths_vs_recovered(dates, deaths, recovered, save_path, show=False):
    plt.figure(figsize=(10, 4))
    plt.plot(dates, deaths, label="Deaths")
    plt.plot(dates, recovered, label="Recovered")
    plt.legend()
    plt.title("Deaths vs Recovered")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_correlation_heatmap(df_numeric, save_path, show=False):
    plt.figure(figsize=(15, 9))
    sns.heatmap(df_numeric.corr(), cmap="coolwarm", annot=True)
    plt.title("COVID-19 Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()

def plot_active_cases(dates, active, save_path, show=False):
    plt.figure(figsize=(10, 4))
    plt.plot(dates, active)
    plt.title("Active COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Active Cases")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_mortality_rate(dates, mortality_rate, save_path, show=False):
    plt.figure(figsize=(10, 4))
    plt.plot(dates, mortality_rate)
    plt.title("COVID-19 Mortality Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mortality Rate")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_daily_new_cases(dates, new_cases, save_path, show=False):
    plt.figure(figsize=(10, 4))
    plt.plot(dates, new_cases)
    plt.title("Daily New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()
