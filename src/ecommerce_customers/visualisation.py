import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
sns.set_palette("coolwarm")

def plot_all(ecom):
    sns.pairplot(ecom)

    sns.jointplot(x="Avg. Session Length", y="Yearly Amount Spent", data=ecom)

    sns.jointplot(x="Time on Website", y="Yearly Amount Spent", data=ecom)

    sns.jointplot(x="Time on App", y="Yearly Amount Spent", data=ecom)

    sns.jointplot(x="Length of Membership", y="Yearly Amount Spent", data=ecom)

    sns.lmplot(x="Length of Membership", y="Yearly Amount Spent", data=ecom)

    plt.show()