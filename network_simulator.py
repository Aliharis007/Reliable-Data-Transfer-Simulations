import random
import time
from config import LOSS_PROB, CORRUPT_PROB, DELAY_PROB

def simulate_network(packet):
    if random.random() < LOSS_PROB:
        print("Packet lost.")
        return None
    
    if random.random() < CORRUPT_PROB:
        print("Packet corrupted.")
        packet['data'] = 'CORRUPTED'
    
    if random.random() < DELAY_PROB:
        delay = round(random.uniform(0.5, 1.5), 2)
        print(f"Packet delayed by {delay}s")
        time.sleep(delay)
    
    return packet