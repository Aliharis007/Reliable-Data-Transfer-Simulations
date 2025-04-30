import time
from network_simulator import simulate_network
from config import TIMEOUT, WINDOW_SIZE

def sr_send(data):
    base, next_seq = 0, 0
    window, acked, timers = {}, {}, {}

    while base < len(data):
        while next_seq < base + WINDOW_SIZE and next_seq < len(data):
            pkt = {'seq': next_seq, 'data': data[next_seq]}
            print(f"Sending: {pkt}")
            result = simulate_network(pkt)
            if result and result['data'] != 'CORRUPTED':
                print(f"ACK received for seq {next_seq}")
                acked[next_seq] = True
            else:
                acked[next_seq] = False
            window[next_seq] = pkt
            timers[next_seq] = time.time()
            next_seq += 1

        time.sleep(1)
        current_time = time.time()

        for seq in list(window):
            if not acked[seq] and current_time - timers[seq] > TIMEOUT:
                print(f"Timeout at seq {seq}, resending")
                pkt = {'seq': seq, 'data': data[seq]}
                print(f"Resending: {pkt}")
                result = simulate_network(pkt)
                if result and result['data'] != 'CORRUPTED':
                    print(f"ACK received for seq {seq}")
                    acked[seq] = True
                timers[seq] = time.time()

        while base in acked and acked[base]:
            del window[base]
            del acked[base]
            del timers[base]
            base += 1
