import pandas as pd

def process_invoices():
    df = pd.read_excel("invoicesToPay.xlsx")
    approved = df[df["ApprovalStatus"] == "Approved"]
    approved.to_csv("temp_approved_invoices.csv", index=False)
    print(f"[Code1] Found {len(approved)} approved invoices.")

if __name__ == "__main__":
    process_invoices()