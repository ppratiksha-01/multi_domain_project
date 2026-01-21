import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def plot_subject_averages(subject_avg, save_path, show=False):
    plt.figure(figsize=(8, 4))
    subject_avg.plot(kind="bar")
    plt.title("Average Score by Subject")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_pass_fail(result_counts, save_path, show=False):
    plt.figure(figsize=(6, 4))
    result_counts.plot(kind="bar")
    plt.title("Pass vs Fail Distribution")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_attendance_vs_score(attendance, scores, save_path, show=False):
    plt.figure(figsize=(6, 4))
    plt.scatter(attendance, scores)
    plt.xlabel("Attendance (%)")
    plt.ylabel("Total Score")
    plt.title("Attendance vs Score")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()

def plot_score_distribution(scores, save_path, show=False):
    plt.figure(figsize=(8, 4))
    plt.hist(scores, bins=20)
    plt.title("Overall Score Distribution")
    plt.xlabel("Overall Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_gender_vs_score(gender, scores, save_path, show=False):
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=gender, y=scores)
    plt.title("Gender-wise Performance")
    plt.xlabel("Gender")
    plt.ylabel("Overall Score")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_study_hours_vs_score(study_hours, scores, save_path, show=False):
    plt.figure(figsize=(8, 4))
    plt.scatter(study_hours, scores, alpha=0.5)
    plt.title("Study Hours vs Overall Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Overall Score")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_correlation_heatmap(df_numeric, save_path, show=False):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_numeric.corr(), cmap="coolwarm", annot=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()
