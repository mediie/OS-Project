import subprocess
import sys

def main():
    while True:
        print("\n--- Algorithm Menu ---")
        print("1. CPU Scheduling Algorithms")
        print("2. Bankers Algorithm")
        print("3. Page Replacement Algorithms")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            subprocess.run([sys.executable, "CPU_Scheduling.py"])
        elif choice == '2':
            subprocess.run([sys.executable, "Bankers.py"])
        elif choice == '3':
            subprocess.run([sys.executable, "Pagefault.py"])
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
