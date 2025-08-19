import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from commands import check_balance, deposit, withdraw, transfer
from accounts import accounts   # dictionary of accounts

# -----------------------------
# Main window
# -----------------------------
root = tk.Tk()
root.title("ATM Simulator")
root.geometry("400x600")

# -----------------------------
# Welcome message
# -----------------------------
welcome_label = tk.Label(root, text="Welcome to the ATM Simulator", font=("Times New Roman", 16))
welcome_label.pack(pady=20)

# -----------------------------
# Account Number Entry
# -----------------------------
message_label = tk.Label(root, text="Enter your account number:", font=("Helvetica", 14))
message_label.pack(pady=10)

account_number_entry = tk.Entry(root, font=("Helvetica", 14))
account_number_entry.pack(pady=10)

# -----------------------------
# Amount Entry (for deposit/withdraw/transfer)
# -----------------------------
amount_label = tk.Label(root, text="Enter amount:", font=("Helvetica", 14))
amount_label.pack(pady=10)

amount_entry = tk.Entry(root, font=("Helvetica", 14))
amount_entry.pack(pady=10)

# -----------------------------
# Helper to get account number + amount safely
# -----------------------------
def get_account_number():
    return account_number_entry.get().strip()

def get_amount():
    try:
        return float(amount_entry.get().strip())
    except ValueError:
        messagebox.showwarning("ATM Simulator", "Please enter a valid amount.")
        return None

# -----------------------------
# Button Functions
# -----------------------------
def do_check_balance():
    acc_number = get_account_number()
    if acc_number:
        check_balance(accounts, acc_number)

def do_deposit():
    acc_number = get_account_number()
    amount = get_amount()
    if acc_number and amount is not None:
        deposit(accounts, acc_number, amount)

def do_withdraw():
    acc_number = get_account_number()
    amount = get_amount()
    if acc_number and amount is not None:
        withdraw(accounts, acc_number, amount)

def do_transfer():
    from_acc = get_account_number()
    to_acc = simpledialog.askstring("Transfer", "Enter target account number:")
    amount = get_amount()
    if from_acc and to_acc and amount is not None:
        transfer(accounts, from_acc, to_acc, amount)

# -----------------------------
# Buttons
# -----------------------------
check_balance_button = tk.Button(root, text="Check Balance", command=do_check_balance, font=("Helvetica", 14))
check_balance_button.pack(pady=10)

deposit_button = tk.Button(root, text="Deposit", command=do_deposit, font=("Helvetica", 14))
deposit_button.pack(pady=10)

withdraw_button = tk.Button(root, text="Withdraw", command=do_withdraw, font=("Helvetica", 14))
withdraw_button.pack(pady=10)

transfer_button = tk.Button(root, text="Transfer", command=do_transfer, font=("Helvetica", 14))
transfer_button.pack(pady=10)

# -----------------------------
# Run the GUI
# -----------------------------
root.mainloop()
