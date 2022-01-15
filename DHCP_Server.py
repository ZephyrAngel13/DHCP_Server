import socket

#constante DHCP
DHCP_DISCOVER = 1
DHCP_OFFER = 2
DHCP_REQUEST = 3
DHCP_DECLINE = 4
DHCP_ACK = 5
DHCP_NAK = 6

#tipuri de variabile
INT = '_int'
HEX = '_hex'
IP = '_ip'
MAC = '_mac'
STR = '_str'


DHCP_FIELDS = [
    {'id': 'op', 'name': 'message_type', 'length': 1, 'type': INT},
    {'id': 'htype', 'name': 'hardware_type', 'length': 1, 'type': INT},
    {'id': 'hlen', 'name': 'hardware_address_length', 'length': 1, 'type': INT},
    {'id': 'hops', 'name': 'hops', 'length': 1, 'type': INT},
    {'id': 'xid', 'name': 'transaction_id', 'length': 4, 'type': HEX},
    {'id': 'secs', 'name': 'seconds_elapsed', 'length': 2, 'type': INT},
    {'id': 'flags', 'name': 'boot_flags', 'length': 2, 'type': HEX},
    {'id': 'ciaddr', 'name': 'client_ip', 'length': 4, 'type': IP},
    {'id': 'yiaddr', 'name': 'your_ip', 'length': 4, 'type': IP},
    {'id': 'siaddr', 'name': 'next_server_ip', 'length': 4, 'type': IP},
    {'id': 'giaddr', 'name': 'relay_agent_ip', 'length': 4, 'type': IP},
    {'id': 'chaddr', 'name': 'client_mac', 'length': 16, 'type': MAC},
    {'id': 'sname', 'name': 'server_hostname', 'length': 64, 'type': STR},
    {'id': 'filename', 'name': 'boot_filename', 'length': 128, 'type': STR},
    {'id': 'magic', 'name': 'magic_cookie', 'length': 4, 'type': HEX},
]