class Payment:
    def __init__(self, payment_id, amount, date):
        self.payment_id = payment_id
        self.amount = amount
        self.date = date

    def process_payment(self):
        print(f"Payment ID {self.payment_id} sebesar {self.amount} berhasil diproses pada tanggal {self.date}.")

    def generate_receipt(self):
        print(f"Receipt for Payment ID {self.payment_id}:")
        print(f"Amount: {self.amount}")
        print(f"Date: {self.date}")

    def cancel_payment(self):
        print(f"Payment ID {self.payment_id} telah dibatalkan.")


payment1 = Payment("P001", 100000, "2024-04-25")


payment1.process_payment()


payment1.generate_receipt()


payment1.cancel_payment()
