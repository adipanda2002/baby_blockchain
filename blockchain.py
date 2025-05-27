class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # create a new block and add it to the chain
    def new_block(self):
        pass

    # create a new transaction and add it to the list of transactions
    def new_transaction(self, sender_address, recipient_address, amount):
        self.current_transactions.append({
            'sender': sender_address,
            'recipient': recipient_address,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    # hash a block
    @staticmethod
    def hash(block):
        pass

    # get the last block in the chain
    @property
    def last_block(self):
        pass