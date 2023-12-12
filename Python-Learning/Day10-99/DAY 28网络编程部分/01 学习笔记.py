"""
结合课本《计算机网络》
=========================================  今日大纲 =========================================
局域网：
    arp协议： 地址解析协议
    广播技术 单播技术
    路由器，网关，网段。
    交换机只能识别： MAC地址

IP地址：
        IPV4：四位点分十进制  192.168.1.1       0.0.0.0---255.255.255.255
        公网地址： 购买私人
        内网地址：  保留字段，
                192.168.0.0 - 192.168.255.255        内网地址，永远不会和自己的冲突。
                172.16.0.0 -  172.31.255.255
                10.0.0.0   -  10.255.255.255
       特殊的 IP地址： 127.0.0.1   本地回环地址
       子网掩码：用来判断两台机器在不在一个局域网内，也是一个IP地址
                利用子网掩码和IP地址进行与操作。  网关地址相同，那么就在一个局域网内
                192.168.1.xx  扩展 == >   192.168.3.xx  在一个局域网内吗

ipconfig/ifconfig

        IP v6： 冒分16进制
                0:0:0:0:0:0  -----  FFFFFF:FFFFFF:FFFFFF:FFFFFF:FFFFFF:FFFFFF:192.168.X.X

端口：确定应用程序

概念的整理：
        局域网：
                交换机
                    在同一个局域网内的终端有交换机进行通信，交换机能识别MAC地址，  广播，组播，单播
                    单播--MAC地址，在网卡上
        局域网之间通信
            路由器：提供网关IP，同一局域网内主机共享一个网关IP
                    不能访问局域网内，内网地址的IP，因为不在一个
            子网掩码：判断主机是否在同一个网段内
IP地址，IPv4，IP v6
MAC地址： arp协议，即地址解析协议（通过解析IP寻找MAC)
端口port:  65535  进制数这里的问题。  确定应用程序。

C/S架构 ： 进程通信，理解客户端服务端的具体特点。
        B/S架构：
        统一PC端入口：   趋向于B/S架构。
对等通信P2P ；
"""
