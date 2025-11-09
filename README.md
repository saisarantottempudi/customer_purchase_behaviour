# 🛍️ Customer Purchase Behaviour Analysis

Analyze how customer demographics and preferences influence purchase decisions.  
This project helps a retail business understand **who buys what**, **how much they spend**, and **which products perform best**.

## 📖 What’s Inside
- A complete **Jupyter Notebook** with cleaning, EDA, segmentation, and visuals
- Cleaned CSVs in `data/processed/`
- Slide deck template in `reports/slides/`

## 🧩 Workflow (what we did)
1) Data Loading  
2) Data Cleaning (duplicates, column names, types)  
3) EDA (distributions, correlations, category patterns)  
4) Customer Segmentation (age groups, spend tiers)  
5) Insights & Business Recommendations  
6) Outputs saved for submission

## 📂 Folder Structure

customer_purchase_behaviour/
├─ data/
│  ├─ raw/                # Original dataset from Kaggle
│  └─ processed/          # Cleaned/segmented outputs
├─ notebooks/
│  └─ 01_eda.ipynb        # Main analysis notebook
├─ scripts/
│  └─ setup_venv.sh       # venv bootstrapper
├─ .env.example
├─ requirements.txt
└─ README.md


## ⚙️ Requirements
- Python 3.10+
- Git
- Jupyter Notebook

### Python libraries
pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, python-dotenv

## 🚀 How to Run (No Coding Needed)

### 1) Clone this project
git clone https://github.com/<your-username>/customer_purchase_behaviour.git
cd customer_purchase_behaviour

### 2) Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows (PowerShell)

### 3) Install dependencies
pip install -r requirements.txt

### 4) Put the dataset in place
- Download from Kaggle: https://www.kaggle.com/datasets/mubeenshehzadi/customer-purchase-behaviour
- Save CSV to: data/raw/CustomerPurchaseBehavior.csv

### 5) Configure environment (optional)
cp .env.example .env
# Edit .env if your filename differs
# DATA_PATH=data/raw/CustomerPurchaseBehavior.csv
# RANDOM_STATE=42

### 6) Run the Notebook
jupyter notebook notebooks/01_eda.ipynb
# In Jupyter, go to: Cell → Run All


## 📦 What You Get (Outputs)
- Cleaned data: `data/processed/cleaned_customer_purchase.csv`
- Segmented data: `data/processed/segmented_customer_data.csv`
- Final dataset: `data/processed/final_customer_behaviour_dataset.csv`
- Charts & insights: inside the notebook (and optional `reports/figures/`)
- Slides: `reports/slides/YourName_CustomerBehaviourAnalysis.pptx`

## ✅ Final Submission Tip
Zip the important parts:
zip -r YourName_CustomerBehaviourAnalysis.zip notebooks data/processed reports/slides README.md

## 📊 Example Insights (from this dataset)
- No customers under 18 → target adult demographics
- High spenders exist across ages (~$90 avg)
- Clothing & Footwear drive most revenue
- Positive reviews correlate with higher spend
- Repeat customers spend more (loyalty = profit)

## 💼 Recommendations
1) Focus marketing on adults (18–60)
2) Build loyalty rewards for repeat buyers
3) Encourage reviews after purchase
4) Cross-sell within Clothing & Footwear

## 🧾 Git Basics (Keep it up to date)

# See changes
git status

# Stage all changes
git add .

# Commit with a message
git commit -m "update: improved EDA visuals"

# Push to GitHub
git push

# Pull latest from GitHub
git pull


