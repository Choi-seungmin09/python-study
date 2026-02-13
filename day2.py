cpu = 81
if cpu > 80:
    print("경고! CPU 과부하")
else:
    print("정상 상태")

status = "running"

if status == "running":
    print("서버 정상 작동 중")
elif status == "stopped":
    print("서버 중지됨")
else:
    print("상태 확인 필요")

servers = ["running", "stopped", "running","error"]

for s in servers:
    if s == "running":
        print("정상")
    else:
        print("점검 필요")
        