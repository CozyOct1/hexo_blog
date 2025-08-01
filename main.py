import subprocess
import time
import os

def check_and_deploy():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Checking for updates from remote repository...")
    try:
        # Update remote references
        subprocess.run(["git", "remote", "update"], check=True, cwd="/workspace/hexo_blog")

        # Check if local branch is behind remote
        result = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True, check=True, cwd="/workspace/hexo_blog")
        if "Your branch is behind" in result.stdout:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Updates found. Pulling changes...")
            subprocess.run(["git", "pull"], check=True, cwd="/workspace/hexo_blog")
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Generating Hexo site...")
            subprocess.run(["hexo", "generate"], check=True, cwd="/workspace/hexo_blog")
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Deploying Hexo site...")
            subprocess.run(["hexo", "deploy"], check=True, cwd="/workspace/hexo_blog")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] No updates from remote repository.")
    except subprocess.CalledProcessError as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error executing command: {e}")
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Command output: {e.stdout}\n{e.stderr}")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] An unexpected error occurred: {e}")

def main():
    INTERVAL = 300  # 5 minutes in seconds
    while True:
        check_and_deploy()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Waiting for {INTERVAL} seconds before next check...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
