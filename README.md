# 📊 E-Commerce Customers Analysis

![Python](https://img.shields.io/badge/Python-Data%20Science-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Linear%20Regression-f7931e?style=for-the-badge&logo=scikitlearn)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

## 📌 Project Overview

This project analyzes customer behavior data from an e-commerce company to understand **which digital channel contributes more to customer spending**: the **mobile app** or the **website**.

At first glance, it may seem logical that the company should invest more in the **website**. However, the data suggests the opposite: **time spent on the app has a much stronger relationship with yearly customer spending than time spent on the website**.

## 🎯 Business Goal

The main objective of this project is to support a business decision:

> **Should the company invest more in improving the mobile app or the website to maximize revenue?**

By using exploratory data analysis and a **Linear Regression model**, we identify which customer activity variables have the strongest impact on **Yearly Amount Spent**.

## ❓ Research Question

The key question behind this analysis is:

- Does the **mobile app** drive more revenue than the **website**?
- Which customer behavior metrics are the most important predictors of spending?
- Where should the company invest to improve profitability?

## 🧾 Dataset Features

The dataset includes the following variables:

- `Avg. Session Length`
- `Time on App`
- `Time on Website`
- `Length of Membership`
- `Yearly Amount Spent`

These features are used to predict customer spending and evaluate the influence of app and website usage.

## ⚙️ Methods Used

This project was built using common Data Science tools and workflows:

- **Python**
- **Pandas** and **NumPy** for data handling
- **Matplotlib** and **Seaborn** for visualization
- **Scikit-learn** for machine learning
- **Linear Regression** for prediction and interpretation

## 📈 Key Result

The Linear Regression model produced the following coefficients:

| Feature | Coefficient |
|---|---:|
| Length of Membership | 61.279097 |
| Time on App | 38.590159 |
| Avg. Session Length | 25.981550 |
| Time on Website | 0.190405 |

## 🧠 Interpretation

The results show that:

- **Length of Membership** has the strongest positive impact on yearly spending.
- **Time on App** is a strong predictor of customer spending.
- **Time on Website** has almost no meaningful impact.
- **Avg. Session Length** also contributes positively, but less than app usage.

This means that although many might assume the **website** deserves more attention, the data indicates that the **mobile app is far more important for revenue growth**.

## 💼 Business Recommendation

Based on the model results, the company should consider:

- investing more in the **mobile app**
- improving the **app user experience**
- adding more app-focused features
- increasing customer retention and engagement inside the app

The website still matters, but according to this analysis, **optimizing the app is likely to generate a better return on investment**.

## 🗂️ Project Structure

```text
E-Commerce-Customers/
├── .venv/
├── data/
├── notebooks/
├── src/
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## ▶️ How to Run

1. Clone this repository.
2. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ## for powershell Terminal
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   ## for cmd Terminal
   ```cmd
   .venv\Scripts\activate.bat
   ```
5. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
6. Open the notebook or run the analysis script in VS Code.

## 📊 Conclusion

This project shows how data can challenge intuition.

Even though it may seem obvious that the **website** should be the company’s main investment focus, the analysis suggests otherwise. The **mobile app** has a much stronger connection to customer spending, making it the more promising area for future improvement and investment.

## 👨‍💻 Author

**Yasser Moussa**  
Aspiring Data Scientist | Python | Machine Learning | Data Analysis
