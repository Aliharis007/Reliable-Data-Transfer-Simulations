# 🚀 Reliable Data Transfer Protocols – FSM Based Simulations

This repository contains Python-based simulations of **Transport Layer** protocols using **Finite State Machines (FSMs)**. It's designed to demonstrate how reliable data transfer works in computer networks through three main protocols:

- ✅ **RDT 3.0** (Stop-and-Wait with corruption & loss handling)
- 🔁 **Go-Back-N (GBN)** (Sliding window with cumulative ACKs)
- 🎯 **Selective Repeat (SR)** (Sliding window with individual ACKs & out-of-order support)

These simulations also include FSM diagrams generated using **Graphviz** for clear visualization of state transitions.

---

## 🧠 Protocols Overview

| Protocol         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **RDT 3.0**       | Handles packet corruption and loss using timeouts and ACK/NAK               |
| **Go-Back-N**     | Uses a sender window; resends all packets after a lost one                 |
| **Selective Repeat** | Sends individual ACKs; only resends lost packets; buffers out-of-order ones |

---

## 📊 FSM Visualization with `graphviz`

All protocols generate FSM diagrams using `graphviz`. These diagrams help you visually understand how sender/receiver states evolve based on inputs (like ACKs, NAKs, timeouts, etc).

### 🔧 Installation Instructions

You'll need **two things**:

#### 1️⃣ Install Graphviz system package:

##### 🪟 Windows:
- Download from: [https://graphviz.org/download/](https://graphviz.org/download/)
- Add the installation path to your **System PATH** (e.g., `C:\Program Files\Graphviz\bin`)

##### 🍎 macOS:
```bash
brew install graphviz
```

##### 🐧 Linux:
```bash
sudo apt install graphviz
```

#### 2️⃣ Install the Python wrapper:

```bash
pip install graphviz
```

> ⚠️ You need **both** the system tool and the Python module for FSM diagrams to generate properly.

---

## 📁 Project Structure

```
📦 Reliable-Data-Transfer-Simulations
 ┣ 📜 rdt3.py           # RDT 3.0 protocol simulation
 ┣ 📜 gbn.py            # Go-Back-N protocol simulation
 ┣ 📜 sr.py             # Selective Repeat protocol simulation
 ┣ 📜 fsm_drawer.py     # Contains FSM generation logic using graphviz
 ┣ 📜 README.md         # Project overview and usage
 ┗ 📜 requirements.txt  # Dependencies (Python only)
```

---

## 🏁 How to Run the Simulations

Make sure Python is installed (v3.7+ recommended), then run any protocol like:

```bash
python rdt3.py       # For RDT 3.0
python gbn.py        # For Go-Back-N
python sr.py         # For Selective Repeat
```

Each file simulates sender-receiver communication **and** generates an FSM diagram like `rdt3_fsm.png` or `gbn_fsm.png`.

---

## ✏️ Customization

Open any protocol script and tweak variables like:

```python
PACKET_LOSS_PROB = 0.2
WINDOW_SIZE = 4
TIMEOUT = 3
```

---

## ✅ Dependencies

```txt
graphviz
```

You can install them using:

```bash
pip install -r requirements.txt
```

---


If this project helped you understand FSMs and protocols better, drop a ⭐ on the repo!
```

---

Let me know if you want me to auto-generate the `requirements.txt` for you too (super short in this case)!
