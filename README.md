# 🚀 Reliable Data Transfer Protocols – FSM Based Simulations

This repository contains Python-based simulations of **Transport Layer** protocols using **Finite State Machines (FSMs)**. It's designed to demonstrate how reliable data transfer works in computer networks through three main protocols:

- ✅ **RDT 3.0** (Stop-and-Wait with corruption & loss handling)
- 🔁 **Go-Back-N (GBN)** (Sliding window with cumulative ACKs)
- 🎯 **Selective Repeat (SR)** (Sliding window with individual ACKs & out-of-order support)

These simulations were built as part of a **Computer Networks assignment** to deeply understand protocol mechanics, packet sequencing, acknowledgments, timeouts, and retransmissions.

---

## 🧠 Protocols Overview

| Protocol         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **RDT 3.0**       | Handles packet corruption and loss using timeouts and ACK/NAK               |
| **Go-Back-N**     | Uses a sender window; resends all packets after a lost one                 |
| **Selective Repeat** | Sends individual ACKs; only resends lost packets; buffers out-of-order ones |

---

## 🖼️ Visualization Support

We used a custom **RDT visualization library** to visually represent the sender-receiver communication and understand how packets, ACKs, and retransmissions flow in real time.

### 🔧 Installation for `rdt-visualization`:

Make sure you install the helper library like this:

```bash
pip install rdt-visualization
```

This is optional, but it’ll let you view animated packet flow and windows live in your terminal or a graphical view.

---

## 📁 Project Structure

```
📦 Reliable-Data-Transfer-Simulations
 ┣ 📜 rdt3.py           # RDT 3.0 protocol simulation
 ┣ 📜 gbn.py            # Go-Back-N protocol simulation
 ┣ 📜 sr.py             # Selective Repeat protocol simulation
 ┣ 📜 utils.py          # Common utility functions
 ┣ 📜 README.md         # Project overview and usage
 ┗ 📜 requirements.txt  # Dependencies (if needed)
```

---

## 🏁 How to Run the Simulations

Make sure Python is installed (v3.7+ recommended), then run any protocol like:

```bash
python rdt3.py       # For RDT 3.0
python gbn.py        # For Go-Back-N
python sr.py         # For Selective Repeat
```

Each file starts a basic sender-receiver simulation, shows logging of events, and if `rdt-visualization` is installed, you'll get a beautiful live view.

---

## ⚙️ Customization

You can tweak parameters like:

- Packet loss probability
- Timeout durations
- Window sizes (in GBN/SR)
- Data stream length

Just open the `.py` files and look near the top for variables like:

```python
WINDOW_SIZE = 4
PACKET_LOSS_PROB = 0.1
TIMEOUT = 3
```

Modify & rerun to test under different conditions 🚀

The goal was to simulate and understand the **FSM behavior** and **reliability** of these core transport-layer protocols.
