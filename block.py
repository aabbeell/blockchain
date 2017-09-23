import hashlib
import time

GENESIS_INDEX = 0
GENESIS_PREVIOUS_HASH = 'borosabelxxthexxmutherfucker'
GENESIS_TIMESTAMP = 0000000000
GENESIS_DATA = 'abel-genesis'
GENESIS_NOUNCE = 0


class BlockParams():

    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data

    def __str__(self):
        return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

    @classmethod
    def genesis_params(cls):
        return cls(GENESIS_INDEX, GENESIS_PREVIOUS_HASH, GENESIS_TIMESTAMP, GENESIS_DATA)


class Block():

    def __init__(self, params, nounce=0):
        self.index = params.index
        self.previous_hash = params.previous_hash
        self.timestamp = params.timestamp
        self.data = params.data
        self.nounce = nounce
        self.hash = self.calc_nounce()

    def params(self):
        return str(self.index) + self.data + str(self.timestamp) + str(self.nounce) + self.previous_hash

    @classmethod
    def genesis_block(cls):
        params = BlockParams.genesis_params()
        return cls(params)

    def calc_hash(self):
        return hashlib.sha256((str(self.params())).encode()).hexdigest()

    def calc_nounce(self):
        while (self.calc_hash()[:4] != "0000"):
            self.nounce = self.nounce + 1
        return self.calc_hash()

    def has_valid_index(self, previous_block):
        return self.index == previous_block.index + 1

    def has_valid_previous_hash(self, previous_block):
        return self.previous_hash == previous_block.hash

    def has_valid_hash(self):
        return (self.calc_hash() == self.hash) and (self.hash[:3] == "000")


# genesis = Block.genesis_block()
# block1 = Block(BlockParams(1, genesis.hash, time.time(), "block 1"))
# block2 = Block(BlockParams(2, block1.hash, time.time(), "block 2"))

# print(genesis.hash)

# print(block1.hash)
# print(block1.has_valid_previous_hash(genesis))
# print(block1.has_valid_index(genesis))

# print(block2.hash)
# print(block2.has_valid_previous_hash(block1))
# print(block2.has_valid_index(block1))
