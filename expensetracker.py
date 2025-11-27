import os, json
from datetime import datetime

FILE = "expenses.json"

# Load & save
def load(): return json.load(open(FILE)) if os.path.exists(FILE) else []
def save(exp): json.dump(exp, open(FILE, "w"), indent=4)

# Add expense
def add(exp):
    name = input("Expense name: ")
    cat = input("Category: ").title()
    amt = float(input("Amount: "))
    exp.append({"name": name, "category": cat, "amount": amt, "date": datetime.now().strftime("%Y-%m-%d")})
    save(exp); print(f"Added {name} - ₹{amt} ({cat})")

# View all + total
def view(exp):
    if not exp: print("No expenses."); return
    total = 0
    for i, e in enumerate(exp,1): print(f"{i}. {e['name']} - ₹{e['amount']} ({e['category']}, {e['date']})"); total+=e['amount']
    print(f"Total Expenses: ₹{total}")

# Total by category
def total_cat(exp):
    cat_tot = {}
    for e in exp: cat_tot[e['category']] = cat_tot.get(e['category'],0)+e['amount']
    for c,t in cat_tot.items(): print(f"{c}: ₹{t}")
    print(f"Grand Total: ₹{sum(cat_tot.values())}")

# Delete expense
def delete(exp):
    if not exp: print("No expenses."); return
    view(exp)
    i = int(input("Enter number to delete: "))-1
    if 0<=i<len(exp): removed = exp.pop(i); save(exp); print(f"Deleted {removed['name']} - ₹{removed['amount']}")

# Main
def main():
    exp = load()
    while True:
        print("\n1.Add 2.View 3.Category Total 4.Delete 5.Exit")
        ch = input("Choose: ")
        if ch=="1": add(exp)
        elif ch=="2": view(exp)
        elif ch=="3": total_cat(exp)
        elif ch=="4": delete(exp)
        elif ch=="5": break
        else: print("Invalid choice")

if __name__=="__main__": main()
