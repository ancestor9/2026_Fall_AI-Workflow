import pandas as pd

def load_payment_details():
    methods = pd.read_excel("Paymentsmethod.xlsx")
    terms = pd.read_excel("paymentTerms.xlsx")
    methods.to_csv("temp_methods.csv", index=False)
    terms.to_csv("temp_terms.csv", index=False)
    print("[Code2] Payment methods and terms loaded successfully.")

if __name__ == "__main__":
    load_payment_details()