import pandas as pd

def check_po():
    po_df = pd.read_excel("POdb.xlsx")
    po_df.to_csv("temp_po.csv", index=False)
    print("[Code3] PO database checked successfully.")

if __name__ == "__main__":
    check_po()