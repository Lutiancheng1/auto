import os
import time
import shutil

SOURCE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tokens")
DEST_DIR = os.path.expanduser("~/cli-proxy/auths")

def main():
    print(f"[*] 启动自动导入脚本...")
    print(f"[*] 源目录: {SOURCE_DIR}")
    print(f"[*] 目标目录: {DEST_DIR}")
    
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    
    while True:
        try:
            count = 0
            for filename in os.listdir(SOURCE_DIR):
                if filename.endswith(".json") and filename.startswith("token_"):
                    src_path = os.path.join(SOURCE_DIR, filename)
                    dest_path = os.path.join(DEST_DIR, filename)
                    
                    # 如果目标目录中不存在该文件，则复制过去
                    if not os.path.exists(dest_path):
                        shutil.copy2(src_path, dest_path)
                        print(f"[{time.strftime('%H:%M:%S')}] ✅ 自动导入成功: {filename}")
                        count += 1
                        
            if count > 0:
                print(f"[*] 本次共导入 {count} 个新账号凭证。")
        except Exception as e:
            print(f"[Error] 自动导入时发生错误: {e}")
            
        time.sleep(30) # 每 30 秒检查一次

if __name__ == "__main__":
    main()
