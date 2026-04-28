import os
import time

target = "192.168.1.1" # 换成你路由器的IP
print(f"开始监控到 {target} 的延迟...")
while True:
    start = time.time()
    response = os.system(f"ping -n 1 {target} > nul" if os.name == "nt" else f"ping -c 1 {target} > /dev/null")
    end = time.time()
    if response == 0:
        print(f"延迟: {int((end - start) * 1000)}ms")
    else:
        print("请求超时！")
    time.sleep(1)
