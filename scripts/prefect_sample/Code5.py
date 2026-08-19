import pandas as pd

def finalize_payments():
    df = pd.read_csv("final_payment_schedule.csv")
    total_amount = df["Amount"].sum()
    print(f"[Code5] Final Payment Schedule Ready! Total Amount: ${total_amount:,.2f}")
    df.to_excel("Final_Payment_Report.xlsx", index=False)
    print("[Code5] Report saved as Final_Payment_Report.xlsx")

if __name__ == "__main__":
    finalize_payments()