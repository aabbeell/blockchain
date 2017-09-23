import blockchain
import time

chain = blockchain.Blockchain()

for i in range(1, 10):
    chain.generate_next_block("block " + str(i))

chain.receive_new_block(blockchain.block.Block(blockchain.block.BlockParams(chain.blocks + 1, chain.latest_block().hash, int(time.time()), "new block")))

for i in range(chain.blocks + 1):
    print(chain.blockchain_store[i].hash + ' : ' + chain.blockchain_store[i].data)
