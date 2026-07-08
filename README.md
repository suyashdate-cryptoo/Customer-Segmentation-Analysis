# 🛍️ Customer Segmentation Analysis using K-Means Clustering

> **An end-to-end Machine Learning project that segments mall customers into meaningful groups using K-Means Clustering, enabling data-driven marketing and business decision-making.**

---

# 📌 Project Overview

Understanding customer behavior is one of the most valuable assets for any business. Rather than treating every customer the same, companies can use **customer segmentation** to create personalized marketing campaigns, improve customer satisfaction, and maximize revenue.

In this project, I built a complete customer segmentation pipeline using **K-Means Clustering**, an unsupervised machine learning algorithm, to identify hidden patterns among customers based on demographic and purchasing characteristics.

The project covers the complete data science workflow—from data preprocessing and exploratory analysis to clustering, visualization, and business interpretation.

---

# 🎯 Project Objectives

* Analyze customer demographics and spending behavior
* Discover hidden customer groups using Machine Learning
* Determine the optimal number of clusters using the Elbow Method
* Visualize customer segments for easy interpretation
* Generate actionable business recommendations for targeted marketing

---

# 📊 Dataset

**Dataset:** Mall Customers Dataset

### Features

| Feature                | Description                                        |
| ---------------------- | -------------------------------------------------- |
| CustomerID             | Unique customer identifier                         |
| Gender                 | Male/Female                                        |
| Age                    | Customer age                                       |
| Annual Income (k$)     | Annual income in thousand dollars                  |
| Spending Score (1–100) | Score assigned based on customer spending behavior |

---

# 🚀 Project Workflow

### 1️⃣ Data Loading

* Imported dataset using Pandas
* Examined dataset structure and data types

### 2️⃣ Data Cleaning

* Checked for missing values
* Removed duplicate records
* Verified data consistency

### 3️⃣ Exploratory Data Analysis (EDA)

* Statistical summary
* Distribution analysis
* Customer demographics
* Spending behavior analysis

### 4️⃣ Data Visualization

* Histograms
* Count plots
* Box plots
* Pair plots
* Scatter plots

### 5️⃣ Outlier Detection

* Boxplot analysis
* Identification of unusual observations

### 6️⃣ Correlation Analysis

* Correlation Heatmap
* Relationship between numerical features

### 7️⃣ Feature Selection

Selected the most relevant variables for clustering:

* Age
* Annual Income
* Spending Score

### 8️⃣ Feature Scaling

Applied **StandardScaler** to normalize feature values before clustering.

### 9️⃣ Finding Optimal Clusters

Implemented the **Elbow Method** to determine the ideal number of clusters.

### 🔟 K-Means Clustering

* Built the clustering model
* Assigned cluster labels
* Evaluated segmentation quality

### 1️⃣1️⃣ Cluster Visualization

Visualized customer groups using scatter plots with color-coded clusters and centroids.

### 1️⃣2️⃣ Business Insights

Interpreted each customer segment and proposed marketing strategies based on customer behavior.

---

# 📈 Key Visualizations

The project includes:

* 📊 Distribution of Customer Age
* 💰 Annual Income Distribution
* 🛒 Spending Score Distribution
* 📦 Boxplots for Outlier Detection
* 🔥 Correlation Heatmap
* 📉 Elbow Method Graph
* 🎯 K-Means Cluster Visualization
* 📍 Cluster Centroids

---

# 🧠 Machine Learning Algorithm

### K-Means Clustering

K-Means is an **unsupervised machine learning algorithm** that partitions data into *K* distinct clusters by minimizing the distance between data points and their respective cluster centroids.

This project uses:

* Euclidean Distance
* Standardized Features
* Random State for reproducibility
* Elbow Method for selecting the optimal number of clusters

---

# 💼 Business Insights

The clustering process identified **five distinct customer segments**, each representing different purchasing patterns.

Examples include:

* 💎 High Income – High Spending (Premium Customers)
* 💰 High Income – Low Spending (Potential Customers)
* 🎯 Average Income – Average Spending (Regular Customers)
* 🛍️ Low Income – High Spending (Value Seekers)
* 📉 Low Income – Low Spending (Low Engagement Customers)

These insights can help businesses:

* Personalize marketing campaigns
* Improve customer retention
* Increase sales through targeted promotions
* Optimize loyalty programs
* Better allocate marketing budgets

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# 📂 Project Structure

```text
Customer-Segmentation-Analysis/
│
├── data/
│   └── Mall_Customers.csv
│
├── notebooks/
│   └── Customer_Segmentation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   └── visualization.py
│
├── images/
│   ├── age_distribution.png
│   ├── income_distribution.png
│   ├── spending_score.png
│   ├── elbow_method.png
│   ├── correlation_heatmap.png
│   └── customer_clusters.png
│
├── reports/
│   └── Project_Report.pdf
│
├── requirements.txt
└── README.md
```

---

# ▶️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/Customer-Segmentation-Analysis.git
```

### Navigate to the Project

```bash
cd Customer-Segmentation-Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Notebook

```bash
jupyter notebook
```

Open:

```
notebooks/Customer_Segmentation.ipynb
```

---

# 📌 Project Highlights

✅ End-to-End Data Science Project

✅ Data Cleaning & Preprocessing

✅ Exploratory Data Analysis (EDA)

✅ Feature Engineering

✅ Data Visualization

✅ Feature Scaling

✅ Elbow Method

✅ K-Means Clustering

✅ Business-Oriented Insights

✅ Professional GitHub Repository Structure

---

# 🔮 Future Enhancements

* PCA for dimensionality reduction
* Interactive dashboards using Power BI or Tableau
* Cluster quality evaluation using Silhouette Score
* Deployment with Streamlit
* Comparison with DBSCAN and Hierarchical Clustering
* Customer recommendation system

---

# 👩‍💻 Author

**Shweta Kokate**

Artificial Intelligence & Data Science Engineering Student

Passionate about **Data Science, Machine Learning, Artificial Intelligence, and Data Analytics**, with a strong interest in building real-world projects that transform raw data into actionable business insights.

⭐ If you found this project useful, consider giving it a star on GitHub!
