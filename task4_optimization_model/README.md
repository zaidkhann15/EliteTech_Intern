# 🧠 Task 4 – Optimization Model using Linear Programming (PuLP)

## 📌 Project Overview
This task solves a real-world **business optimization problem** using **Linear Programming (LP)**.  
The goal is to **maximize profit** while respecting the limitations of resources such as time and material.

We use **Python + PuLP** to:
✅ Define decision variables  
✅ Create an objective function (maximize profit)  
✅ Apply constraints (available machine hours & materials)  
✅ Solve and interpret results  

---

## 🏭 Problem Statement

**A factory produces 2 products: Product A and Product B**

| Detail | Product A | Product B |
|--------|-----------|-----------|
| Profit per unit | $40 | $30 |
| Machine hours per unit | 2 hrs | 1 hr |
| Materials per unit | 1 unit | 1.5 units |

**Available Resources:**
- Total machine hours available = 100 hrs  
- Total materials available = 90 units  

**Goal:**  
Maximize profit → `40x + 30y`  
where:
- `x` = Units of Product A  
- `y` = Units of Product B  
- Subject to resource limits & `x, y ≥ 0`

---

## 📁 Folder Structure

task4_optimization_model/
│
├── product_mix_optimization.ipynb # Jupyter Notebook with full solution
├── requirements.txt # All libraries needed
├── README.md # Documentation
└── data/ (optional if using dataset)


---

## ⚙️ Installation & Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
2. **Install Requirements**
   pip install -r requirements.txt
3. **Run Notebook**
   jupyter notebook


## Output & Key Insights
  1. Optimal values of x and y are printed
  2. Maximum profit calculated using PuLP
  3. Constraints are checked to ensure feasibility
  4. Visualizations (optional) show resource usage and profit contribution


## Deliverable

## ✔ A Jupyter Notebook demonstrating:

  1. Problem explanation
  2. Objective function
  3. Constraints
  4. Python code using PuLP
  5. Results and insights



Developed By:
Zaid Khan
EliteTech Internship – Task 3: Optimization Model – Completed