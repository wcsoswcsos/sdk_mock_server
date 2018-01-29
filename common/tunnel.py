from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ssh_address_or_host=('172.18.12.3'),
    local_bind_address=('172.18.12.3',10000),
    remote_bind_address=('172.18.12.3')
)