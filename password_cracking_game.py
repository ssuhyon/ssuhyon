import random

def generate_password():
    return "".join([str(random.randint(0, 9)) for _ in range(4)])

def check_guess(password, guess):
    correct_digits = sum(1 for p, g in zip(password, guess) if p == g)
    total_matches = sum(min(password.count(d), guess.count(d)) for d in set(guess))
    return correct_digits, total_matches

def hacking_game():
    password = generate_password()
    attempts = 10
    
    print("\n=== 해킹 미니게임 ===")
    print("[!] 4자리 숫자 비밀번호를 크랙하라! (기회: 10번)")
    
    for attempt in range(1, attempts + 1):
        guess = input(f"[{attempt}/{attempts}] 입력: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("[-] 4자리 숫자로 입력하라!")
            continue
        
        correct, total = check_guess(password, guess)
        
        if correct == 4:
            print("[+] 해킹 성공! 비밀번호: ", password)
            return
        else:
            print(f"[*] 정확한 숫자 개수: {total}, 정확한 위치: {correct}")
    
    print("[!] 해킹 실패... 비밀번호는: ", password)

if __name__ == "__main__":
    hacking_game()