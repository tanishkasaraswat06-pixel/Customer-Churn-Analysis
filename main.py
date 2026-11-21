
# Customer Churn Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load customer dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Display first 5 rows
print("\nFIRST 5 CUSTOMER RECORDS:")
print(df.head())

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# STEP 5: DATA INSPECTION

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print(df.duplicated().sum())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== CHURN DISTRIBUTION ==========")
print(df["Churn"].value_counts())


# STEP 6: DATA CLEANING

# Remove extra spaces from TotalCharges
df["TotalCharges"] = df["TotalCharges"].str.strip()

# Convert TotalCharges into numeric format
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Check missing values after conversion
print("\nMISSING VALUES AFTER CONVERSION:")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# Fill missing TotalCharges with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Check data types again
print("\nUPDATED DATA TYPES:")
print(df.dtypes)

print("\nDATA CLEANING COMPLETED!")

# STEP 7: CUSTOMER CHURN VISUALIZATION

# Count customers in each churn category
churn_counts = df["Churn"].value_counts()

# Create chart
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Churn",
    hue="Churn",
    palette=["#2E86DE", "#E74C3C"],
    legend=False
)

# Add chart title and labels
plt.title("Customer Churn Distribution", fontsize=16)
plt.xlabel("Customer Churn")
plt.ylabel("Number of Customers")

# Display the chart
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.show()

print("\nChurn distribution chart created successfully!")

# STEP 8: FACTORS AFFECTING CUSTOMER CHURN

# Contract type vs churn
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn",
    palette=["#2E86DE", "#E74C3C"]
)

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig("contract_churn.png")
plt.show()

# STEP 9: CUSTOMER TENURE ANALYSIS

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="tenure",
    hue="Churn",
    bins=30,
    multiple="stack",
    palette=["#2E86DE", "#E74C3C"]
)

plt.title("Customer Tenure vs Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("tenure_churn.png")
plt.show()

# STEP 10: MONTHLY CHARGES ANALYSIS

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges",
    hue="Churn",
    palette=["#2E86DE", "#E74C3C"],
    legend=False
)

plt.title("Monthly Charges vs Customer Churn")
plt.xlabel("Customer Churn")
plt.ylabel("Monthly Charges")

plt.tight_layout()
plt.savefig("monthly_charges_churn.png")
plt.show()

# STEP 11: CHURN RATE ANALYSIS

# Calculate overall churn percentage
churn_percentage = (
    df["Churn"].value_counts(normalize=True) * 100
)

print("\n========== OVERALL CHURN RATE ==========")
print(churn_percentage)

# Calculate churn rate by contract type
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print("\n========== CHURN RATE BY CONTRACT ==========")
print(contract_churn)

# Calculate churn rate by contract type (Yes only)
print("\n========== CONTRACT-WISE CHURN PERCENTAGE ==========")
print(contract_churn["Yes"])

# STEP 12: CONTRACT-WISE CHURN RATE VISUALIZATION

plt.figure(figsize=(9, 5))

sns.barplot(
    x=contract_churn.index,
    y=contract_churn["Yes"],
    hue=contract_churn.index,
    palette="Set2",
    legend=False
)

plt.title("Churn Rate by Contract Type", fontsize=16)
plt.xlabel("Contract Type")
plt.ylabel("Churn Percentage (%)")

plt.ylim(0, 50)

plt.tight_layout()
plt.savefig("contract_churn_percentage.png")
plt.show()

print("\nContract churn percentage chart created!")

# STEP 13: PAYMENT METHOD ANALYSIS

plt.figure(figsize=(11, 5))

sns.countplot(
    data=df,
    x="PaymentMethod",
    hue="Churn",
    palette=["#2E86DE", "#E74C3C"]
)

plt.title("Customer Churn by Payment Method", fontsize=15)
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("payment_method_churn.png")
plt.show()

print("\nPayment method analysis completed!")

# STEP 14: INTERNET SERVICE ANALYSIS

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="InternetService",
    hue="Churn",
    palette=["#2E86DE", "#E74C3C"]
)

plt.title("Customer Churn by Internet Service", fontsize=15)
plt.xlabel("Internet Service Type")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("internet_service_churn.png")
plt.show()

print("\nInternet service analysis completed!")

# STEP 15: CHURN RATE BY PAYMENT METHOD

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

print("\n========== CHURN RATE BY PAYMENT METHOD ==========")
print(payment_churn["Yes"].sort_values(ascending=False))


# STEP 16: CHURN RATE BY INTERNET SERVICE

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100

print("\n========== CHURN RATE BY INTERNET SERVICE ==========")
print(internet_churn["Yes"].sort_values(ascending=False))

# STEP 17: FINAL BUSINESS INSIGHTS

print("\n========== CUSTOMER CHURN INSIGHTS ==========")

print("1. Overall customer churn rate:",
      round((df["Churn"] == "Yes").mean() * 100, 2), "%")

print("\n2. Highest churn contract:")
print(contract_churn["Yes"].idxmax())

print("\n3. Highest churn payment method:")
print(payment_churn["Yes"].idxmax())

print("\n4. Highest churn internet service:")
print(internet_churn["Yes"].idxmax())

print("\n========== BUSINESS RECOMMENDATIONS ==========")

print("1. Offer discounts to month-to-month customers.")
print("2. Improve customer support during early subscription.")
print("3. Review pricing plans for high-paying customers.")
print("4. Encourage automatic payment methods.")
print("5. Improve customer retention strategies.")

print("\nCUSTOMER CHURN ANALYSIS COMPLETED!")

# STEP 18: SAVE CLEANED DATASET

df.to_csv("data/cleaned_customer_churn.csv", index=False)

print("Cleaned dataset saved successfully!")


