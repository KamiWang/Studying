try:
    import paramiko
except:
    import os
    os.system('pip install paramiko')
    import paramiko

import subprocess
import os
import time

SERVER_DIR = list()

IP = "192.168.1.214"
PORT = 22
USER = "H5InnerNet"
PASSWORD = "1234"

# 本地策划配置目录
PROJECT_DIR = "D:/FH/H5_Game/config/"

# 服务器策划配置目录
REMOTE_DIR = "/home/H5InnerNet/H5_DM_RELEASE/"

# 是否需要重启
NEED_REBOOT = False


def get_all_file_path_name(path, excpet):
    all_files = list()
    fname_list = os.listdir(path)
    for fname in fname_list:
        if excpet and (fname in excpet):
            continue
        fpath_name = os.path.join(path, fname)
        if os.path.isdir(fpath_name):
            all_files.extend(get_all_file_path_name(fpath_name, excpet))
        else:
            all_files.append(fpath_name.replace("\\", "/"))
    return all_files


subprocess.run(
    f'TortoiseProc.exe /command:update /path:"{PROJECT_DIR}" /closeonend:3')


transport = paramiko.Transport(sock=(IP, PORT))
transport.connect(username=USER, password=PASSWORD)
sftp = paramiko.SFTPClient.from_transport(transport)

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(IP, PORT, USER, PASSWORD)

# 配置文件
all_file = get_all_file_path_name(PROJECT_DIR + "server/", [])
put_temp = []
for f in all_file:
    rf = f.replace(PROJECT_DIR + "server/",
                   REMOTE_DIR + "H5_DM_project/config/")
    put_temp.append((f, rf))

for v in put_temp:
    sftp.put(v[0], v[1])

# map文件
all_map_file = get_all_file_path_name(PROJECT_DIR + "map/", [])
put_temp = []
for f in all_map_file:
    rf = f.replace(PROJECT_DIR + "map/",
                   REMOTE_DIR + "H5_DM_project/config/map/")
    put_temp.append((f, rf))

for v in put_temp:
    sftp.put(v[0], v[1])


sftp.put(PROJECT_DIR + "server/ConstantConfig.json",
         REMOTE_DIR+"H5_DM_chat/config/ConstantConfig.json")
sftp.put(PROJECT_DIR + "server/ConstantConfig.json",
         REMOTE_DIR+"H5_DM_chat_hub/config/ConstantConfig.json")
sftp.put(PROJECT_DIR + "server/ConstantConfig.json",
         REMOTE_DIR+"H5_DM_friend/config/ConstantConfig.json")
sftp.put(PROJECT_DIR + "server/ConstantConfig.json",
         REMOTE_DIR+"H5_DM_rank/config/ConstantConfig.json")

print("配置更新完成")

if NEED_REBOOT:
    ssh.exec_command("pkill -2 H5_DM_project")
    print("pkill -2 H5_DM_project")
    time.sleep(1)
    ssh.exec_command(f"cd {REMOTE_DIR}H5_DM_project/; ./H5_DM_project &")
    print("重启完成")

os.system('pause')
