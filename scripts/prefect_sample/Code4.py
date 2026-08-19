import pandas as pd

def merge_data():
    invoices = pd.read_csv("temp_approved_invoices.csv")
    methods = pd.read_csv("temp_methods.csv")
    terms = pd.read_csv("temp_terms.csv")
    
    # 송장 + 지불방식 + 지불조건 병합
    merged = invoices.merge(methods, on="VendorName", how="left")
    merged = merged.merge(terms, on="VendorID", how="left")
    
    merged.to_csv("final_payment_schedule.csv", index=False)
    print(f"[Code4] Successfully merged data. Total records: {len(merged)}")

if __name__ == "__main__":
    merge_data()