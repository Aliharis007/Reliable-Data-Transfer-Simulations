from rdt3 import rdt_send
from gbn import gbn_send
from sr import sr_send
from fsm import generate_rdt3_fsm, generate_gbn_fsm, generate_sr_fsm

data = ["pkt1", "pkt2", "pkt3"]

print("\n---------- RDT 3.0 ----------\n")
rdt_send(data)

print("\n---------- Go-Back-N ----------\n")
gbn_send(data)

print("\n---------- Selective Repeat ----------\n")
sr_send(data)

generate_rdt3_fsm()
generate_gbn_fsm()
generate_sr_fsm()
