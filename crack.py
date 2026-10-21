
def print_network_scan(**kwargs):
    for key, ports in kwargs.items():
        open_ports = [port for port in ports if port < 1024]
        match len(open_ports):
            case 0:
                state = "Secure"
            case 1 | 2:
                state = "Moderate"
            case _:
                state = "Insecure"
        print(f"{key}: {state} ({open_ports})")





print_network_scan(**{
    "192.168.88.1": [22, 80, 443, 1919],
    "192.172.88.100": [21, 22, 1025],
    "192.168.89.250": [80, 8080, 8383],
    "192.128.168.123": [443, 8443, 280]
})
