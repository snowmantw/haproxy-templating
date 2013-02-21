
global
    maxconn 102400
    user haproxy
    group haproxy
    log /dev/log local0 
    log /dev/log local0 info
 
defaults
	log global


frontend httpmode 0.0.0.0:5288
    maxconn 102400
    timeout client 7d
    mode http
    option httplog
    default_backend xws_backend
    acl is_websocket hdr(Upgrade) -i websocket 
    acl is_websocket hdr_beg(Host) -i ws
    use_backend xws_backend if is_websocket

frontend ej 0.0.0.0:5222
    timeout client 7d
    maxconn 102400
    option tcplog
    default_backend xmpp_backend

backend xmpp_backend
    balance roundrobin
    mode tcp
    timeout server 7d
    timeout connect 7d
    $nodes_tcp

backend xws_backend
    balance roundrobin
    mode http
    timeout server 7d
    timeout connect 7d
    $nodes_ws
