try:
    import paramiko
except :
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

# 本地工程项目目录
PROJECT_DIR = "D:/FH/H5_Game/program/server/"
# 服务器项目目录
REMOTE_DIR = "/home/H5InnerNet/H5_DM_RELEASE/"

# 是否上传可执行文件
IS_UPLOAD_EXE = True

# 是否需要重启
NEED_REBOOT = False

# 需要上传的服务器
SERVER_DIR.append("H5_DM_chat_hub/")
# SERVER_DIR.append("H5_DM_chat/")
# SERVER_DIR.append("H5_DM_friend/")
# SERVER_DIR.append("H5_DM_project/")
# SERVER_DIR.append("H5_DM_rank/")


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


def build_project():
    subprocess.run(
        f'TortoiseProc.exe /command:update /path:"{PROJECT_DIR}" /closeonend:3')
    for server_name in SERVER_DIR:
        server_path = PROJECT_DIR + server_name
        subprocess.run(server_path + "build_linux.bat",
                       cwd=server_path, input=bytes("1", "utf8"))
    print("Building Complete")


def upload_file_to_linux():
    print("OpenSSH...正在传输文件")

    transport = paramiko.Transport(sock=(IP, PORT))
    transport.connect(username=USER, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, PORT, USER, PASSWORD)

    for sd in SERVER_DIR:
        program_server_name = sd[:-1]

        if IS_UPLOAD_EXE or NEED_REBOOT:
            ssh.exec_command("pkill -2 " + program_server_name)
            print("pkill -2 " + program_server_name)
            time.sleep(1)

        upload_path = PROJECT_DIR + sd + "release/"
        remote_path = REMOTE_DIR + sd

        except_list = ["app.toml"]
        if not IS_UPLOAD_EXE:
            except_list.append(program_server_name)

        all_file_list = get_all_file_path_name(upload_path, except_list)
        put_temp = list()
        dir_temp = set()

        for f in all_file_list:
            rf = f.replace(upload_path, remote_path)
            put_temp.append((f, rf))
            dir_temp.add(os.path.split(rf)[0])

        for v in dir_temp:
            ssh.exec_command('mkdir -p ' + v)
        time.sleep(1)
        for v in put_temp:
            sftp.put(v[0], v[1])
        time.sleep(1)
        ssh.exec_command('chmod +x ' + REMOTE_DIR + sd + program_server_name)
        if NEED_REBOOT:
            ssh.exec_command(f"cd {REMOTE_DIR}{sd}; ./{program_server_name} &")

    SH_FILE_NAME = "H5GameStart.sh"
    try:
        sftp.put(PROJECT_DIR + SH_FILE_NAME, REMOTE_DIR + SH_FILE_NAME)
        time.sleep(1)
    except Exception as e:
        print(e)
    ssh.exec_command('chmod +x ' + REMOTE_DIR + SH_FILE_NAME)

    ssh.close()
    sftp.close()
    print("CloseSSH...")


build_project()
upload_file_to_linux()

os.system('pause')