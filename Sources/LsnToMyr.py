import tkinter as tk
from tkinter import ttk 
import math

NFT_MATIC = 40
MATIC_USD = 0.86
USD_MYR = 4.49

# https://min-api.cryptocompare.com/data/price?fsym=MATIC&tsyms=USD
# https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=MATIC,MYR
# https://min-api.cryptocompare.com/data/price?fsym=MYR&tsyms=USD

class MainApplication(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.maticPerNft = tk.DoubleVar()
        self.usdPerMatic = tk.DoubleVar()
        self.myrPerUsd = tk.DoubleVar()
        self.maticPerNft.set(NFT_MATIC)
        self.usdPerMatic.set(MATIC_USD)
        self.myrPerUsd.set(USD_MYR)

        self.myr = tk.DoubleVar()
        self.lsn = tk.DoubleVar()
        self.cost = tk.DoubleVar()
        self.matic = tk.DoubleVar()
        self.myr_calc = self.myr.trace_add("write", self.calculate)
        self.lsn_calc = self.lsn.trace_add("write", self.calculate)
        self.matic_calc = self.matic.trace_add("write", self.calculate)

        ttk.Label(self, text="MATIC per NFT: ").grid(row=0, column=0, padx=(0, 16), sticky=tk.E)
        ttk.Label(self, text="USD per MATIC: ").grid(row=1, column=0, padx=(0, 16), sticky=tk.E)
        ttk.Label(self, text="MYR per USD: ").grid(row=2, column=0, padx=(0, 16), sticky=tk.E)
        ttk.Entry(self, textvariable=self.maticPerNft, state=tk.DISABLED).grid(row=0, column=1)
        ttk.Entry(self, textvariable=self.usdPerMatic, state=tk.DISABLED).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.myrPerUsd, state=tk.DISABLED).grid(row=2, column=1)

        ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=2, sticky="we", pady=(8, 8))

        self.lbl_myr = ttk.Label(self, text="MYR: ")
        self.lbl_myr.grid(row=4, column=0, padx=(0, 16), sticky=tk.E)
        self.lbl_lsn = ttk.Label(self, text="LSN: ")
        self.lbl_lsn.grid(row=6, column=0, padx=(0, 16), sticky=tk.E)
        self.lbl_cost = ttk.Label(self, text="MATIC cost: ")
        self.lbl_cost.grid(row=7, column=0, padx=(0, 16), sticky=tk.E)
        self.lbl_matic = ttk.Label(self, text="MATIC: ")
        self.lbl_matic.grid(row=9, column=0, padx=(0, 16), sticky=tk.E)
        ttk.Entry(self, textvariable=self.myr).grid(row=4, column=1)
        ttk.Label(self, text="=").grid(row=5, column=1)
        ttk.Entry(self, textvariable=self.lsn).grid(row=6, column=1)
        ttk.Entry(self, textvariable=self.cost, state=tk.DISABLED).grid(row=7, column=1)
        ttk.Label(self, text="+").grid(row=8, column=1)
        ttk.Entry(self, textvariable=self.matic).grid(row=9, column=1)

    def calculate(self, *args):
        try:
            myr = self.myr.get()
        except tk.TclError as e:
            myr = 0
        try:
            lsn = self.lsn.get()
        except tk.TclError as e:
            lsn = 0
        try:
            matic = self.matic.get()
        except tk.TclError as e:
            matic = 0

        self.myr.trace_remove("write", self.myr_calc)
        self.lsn.trace_remove("write", self.lsn_calc)
        self.matic.trace_remove("write", self.matic_calc)
            
        if (args[0] == str(self.myr)):
            self.lbl_myr.config(text="Payment (MYR): ")
            self.lbl_lsn.config(text="Can buy (LSN): ")
            self.lbl_matic.config(text="MATIC Left: ")
            usd = myr / USD_MYR # USD that can be exchanged
            matic = usd / MATIC_USD # MATIC that can be exchanged
            lsn = math.floor(matic / NFT_MATIC) - (1 if lsn > 0 else 0) # LSN that can be exchanged, 1 LSN to prevent loss
            matic -= (lsn * NFT_MATIC)
            self.matic.set(matic)
            self.lsn.set(lsn)
        elif(args[0] == str(self.lsn) or args[0] == str(self.matic)):
            self.lbl_myr.config(text="Will cost (MYR): ")
            self.lbl_lsn.config(text="Will buy (LSN): ")
            self.lbl_matic.config(text="and (MATIC): ")
            myr = (lsn * NFT_MATIC + matic) * MATIC_USD * USD_MYR
            self.myr.set(myr)

        self.cost.set(lsn * NFT_MATIC)
        self.myr_calc = self.myr.trace_add("write", self.calculate)
        self.lsn_calc = self.lsn.trace_add("write", self.calculate)
        self.matic_calc = self.matic.trace_add("write", self.calculate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MYR to LSN converter")
    MainApplication(root, padding=10).pack(side="top", fill="both", expand=True)
    root.mainloop()
