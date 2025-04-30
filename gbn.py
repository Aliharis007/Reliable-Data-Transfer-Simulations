import time
from network_simulator import simulate_network
from config import TIMEOUT, WINDOW_SIZE

def gbn_send(data):
    base, next_seq = 0, 0
    window = {}
    timers = {}

    while base < len(data):
        while next_seq < base + WINDOW_SIZE and next_seq < len(data):
            pkt = {'seq': next_seq, 'data': data[next_seq]}
            print(f"Sending: {pkt}")
            result = simulate_network(pkt)
            window[next_seq] = result
            timers[next_seq] = time.time()
            next_seq += 1

        time.sleep(1)
        current_time = time.time()

        for seq in list(window):
            if seq == base and window[seq] and window[seq]['data'] != 'CORRUPTED':
                print(f"ACK received for seq {seq}")
                del window[seq]
                del timers[seq]
                base += 1
            elif seq == base and current_time - timers[seq] > TIMEOUT:
                print(f"Timeout at seq {seq}, resending window from {base}")
                for i in range(base, next_seq):
                    pkt = {'seq': i, 'data': data[i]}
                    print(f"Resending: {pkt}")
                    result = simulate_network(pkt)
                    window[i] = result
                    timers[i] = time.time()
                break
