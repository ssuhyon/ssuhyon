import random
import time
import os
import sys
from termcolor import colored

# 랜덤 단어 리스트
words = ["cyberpunk", "netrunner", "hacker", "glitch", "matrix", "console", "exploit", "firewall", "mainframe", "rootkit"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_game():
    score = 0
    start_time = time.time()
    time_limit = 30  # 30초 제한
    
    while True:
        if time.time() - start_time > time_limit:
            print(colored("\n[!] 타임 오버! 해킹 종료...", "red"))
            break
        
        target_word = random.choice(words)
        print(colored(f"\n[>] 입력하라: {target_word}", "cyan"))
        user_input = input("$ ")
        
        if user_input == target_word:
            print(colored("[+] 정확하다! 시스템 침입 중...", "green"))
            score += 10
        else:
            print(colored("[-] 실패... 다시 시도하라.", "red"))
    
    print(colored(f"\n[*] 최종 점수: {score}", "yellow"))
    print(colored("[*] 네트워크에서 탈출 중...", "magenta"))
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    clear_screen()
    print(colored("\n=== 해커 타자 연습 ===", "blue", attrs=["bold"]))
    print(colored("[!] 네트워크에 접속 중...", "magenta"))
    time.sleep(2)
    typing_game()