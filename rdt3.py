import time
from network_simulator import simulate_network
from config import TIMEOUT

def rdt_send(data):
    seq = 0
    for item in data:
        while True:
            pkt = {'seq': seq, 'data': item}
            print(f"Sending: {pkt}")
            result = simulate_network(pkt)

            start = time.time()
            while time.time() - start < TIMEOUT:
                if result and result['data'] != 'CORRUPTED':
                    print(f"ACK received for seq {seq}")
                    seq ^= 1
                    break
                time.sleep(0.5)
            else:
                print("Timeout. Retrying...")
                continue
            break