# 🧱 Baby Blockchain

A minimal blockchain implementation in Python using Flask, designed to demonstrate the core concepts behind blockchain technology — no coins, no wallets, just logic.

---

## 🔧 Features

- Proof-of-Work mining algorithm
- Simple transaction creation and queuing
- Block creation and chaining
- RESTful API using Flask

---

## 🚀 Getting Started

### 📆 Requirements

- Python 3.7+
- Flask

### 🛠️ Installation

```bash
pip install flask
```

### ▶️ Run the App

```bash
python blockchain.py
```

By default, the Flask server will start at:  
`http://localhost:5000`

---

## 🔗 API Endpoints

### ⛏ `/mine`

**Method**: `GET`  
Triggers the mining of a new block and rewards the miner.

```bash
curl http://localhost:5000/mine
```

---

### 💸 `/transactions/new`

**Method**: `POST`  
Creates a new transaction to be added to the next mined block.

**Request body** (JSON):

```json
{
  "sender": "your-address",
  "recipient": "someone-else",
  "amount": 5
}
```

**Example with `curl`**:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"sender":"a", "recipient":"b", "amount":5}' \
http://localhost:5000/transactions/new
```

---

### 📜 `/chain`

**Method**: `GET`  
Returns the full blockchain.

```bash
curl http://localhost:5000/chain
```

---

## ⚙️ How It Works

- Each block contains:
  - An index
  - A timestamp
  - A list of transactions
  - A proof from the Proof-of-Work algorithm
  - The hash of the previous block

- New transactions are stored in memory until the next block is mined.

- Mining a block:
  - Runs a simple Proof-of-Work algorithm
  - Adds a reward transaction (sender = `"0"`)
  - Appends the new block to the chain

---

## 🧠 Concepts Demonstrated

- Blockchain data structure
- SHA-256 hashing
- Basic Proof of Work
- Immutability and linking via hashes
- Stateless RESTful API design

---

## 📁 Project Structure

| File           | Purpose                                 |
|----------------|------------------------------------------|
| `blockchain.py` | Main application and blockchain logic   |
| `README.md`     | This guide                              |

---

## 🏁 Next Steps (for exploration)

- Add peer-to-peer networking and consensus mechanism
- Add block validation and chain conflict resolution
- Build a simple frontend interface

---

Built for learning 🧠 — feel free to fork, explore, and expand!
