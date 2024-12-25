import requests
import re
from tqdm import tqdm
import os


class statue_re_pattern:
    # 正则表达式模式
    pattern_200 = r'^2\d{2}$'
    pattern_300 = r'^3\d{2}$'
    pattern_400 = r'^4\d{2}$'
    pattern_500 = r'^5\d{2}$'



def scan_web(target_url, dir_txt):
    with open(dir_txt, "r") as f:
        dirs = f.readlines()


    # 使用 tqdm 创建进度条
    with tqdm(total=len(dirs), desc="扫描进度", unit="项") as pbar:
        
        for dir in dirs:
            dir = dir.strip()
            full_url = f"{target_url}{dir}"
            try:
                resp = requests.get(full_url, allow_redirects=False,timeout=5)
                if re.match(statue_re_pattern.pattern_200, str(resp.status_code)):
                    # 使用 tqdm 的 write 方法输出结果，不影响进度条的位置
                    tqdm.write(f"[{resp.status_code}] 发现目录: {full_url}")
            except requests.RequestException as e:
                tqdm.write(f"[错误] 请求失败: {full_url} 错误: {e}")
                break
            
            # 更新进度条
            pbar.update(1)

if __name__ == "__main__":
    target_url = "http://127.0.0.1/dvwa"
    dir_txt = './top3000.txt'
    scan_web(target_url, dir_txt)

    