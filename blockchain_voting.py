import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # vote data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(len(self.chain), time.time(), data, self.get_latest_block().hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True

# ---------------- Voting System -----------------

class VotingSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.votes = {"Alice": 0, "Bob": 0, "Charlie": 0}

    def cast_vote(self, voter_id, candidate):
        if candidate not in self.votes:
            print("Invalid candidate!")
            return
        data = {"voter_id": voter_id, "candidate": candidate}
        self.blockchain.add_block(data)
        self.votes[candidate] += 1
        print(f"Vote casted for {candidate} by Voter-{voter_id}")

    def results(self):
        print("\nElection Results:")
        for candidate, count in self.votes.items():
            print(f"{candidate}: {count} votes")

# ---------------- Run Example -----------------
voting = VotingSystem()

# Cast votes
voting.cast_vote(1, "Alice")
voting.cast_vote(2, "Bob")
voting.cast_vote(3, "Alice")
voting.cast_vote(4, "Charlie")

# Display results
voting.results()

# Validate blockchain
print("\nIs Blockchain Valid?", voting.blockchain.is_chain_valid())
