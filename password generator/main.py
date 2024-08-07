import string
import os
import sys
from random import choice

class Main:
    def __init__(self):
        self.main()
        
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("""
          ▄▀▄     ▄▀▄
         ▄█░░▀▀▀▀▀░░█▄
     ▄▄  █░░░░░░░░░░░█  ▄▄
    █▄▄█ █░░█░░┬░░█░░█ █▄▄█
╔════════════════════════════════════════╗
║ ♚ Project : ℙ𝕒𝕤𝕤𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣™             ║
║ ♚ Author  : Lusmaysh                   ║
║ ♚ Github  : github.com/Lusmaysh        ║
║ ♚ Version : v1.0.0                     ║
╚════════════════════════════════════════╝""")
        
    def get_valid_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def main(self):
        self.banner()
        char = self.get_valid_input("[+] Number of characters: ")
        line = self.get_valid_input("[+] Number of lines: ")

        print("═" * 42)
        for x in range(line):
            result = "".join(choice(string.ascii_letters + string.digits + "-_.{}*&^%$#@!") for _ in range(char))
            print(f"[{x + 1}] {result}")

if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        sys.exit()
