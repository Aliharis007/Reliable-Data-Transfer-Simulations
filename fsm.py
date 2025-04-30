from graphviz import Digraph
import os

os.makedirs("fsm_outputs", exist_ok=True)

def generate_rdt3_fsm():
    dot = Digraph("rdt3")
    dot.attr(rankdir='LR')
    dot.edge('Wait0', 'ACK0', 'send pkt0')
    dot.edge('ACK0', 'Wait1', 'recv ACK0')
    dot.edge('ACK0', 'ACK0', 'timeout/NAK0')
    dot.edge('Wait1', 'ACK1', 'send pkt1')
    dot.edge('ACK1', 'Wait0', 'recv ACK1')
    dot.edge('ACK1', 'ACK1', 'timeout/NAK1')
    dot.render('fsm_outputs/rdt3_fsm', format='png', cleanup=True)


def generate_gbn_fsm():
    dot = Digraph("GBN")
    dot.attr(rankdir='LR')
    dot.edge('Send', 'WaitACK', 'send pkt(s)')
    dot.edge('WaitACK', 'Send', 'recv ACK (base updated)')
    dot.edge('WaitACK', 'WaitACK', 'timeout or partial ACK')
    dot.render('fsm_outputs/gbn_fsm', format='png', cleanup=True)


def generate_sr_fsm():
    dot = Digraph("SR")
    dot.attr(rankdir='LR')
    dot.edge('Send', 'WaitACKs', 'send pkt(s)')
    dot.edge('WaitACKs', 'WaitACKs', 'recv individual ACK or timeout')
    dot.render('fsm_outputs/sr_fsm', format='png', cleanup=True)