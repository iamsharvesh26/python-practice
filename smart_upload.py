# smart_upload.py
import subprocess
import os
from datetime import datetime
import sys

def run_command(cmd):
    """Helper to run commands and show output"""
    print(f"▶  Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr and "warning" not in result.stderr.lower():
        print(f"⚠  {result.stderr}")
    return result.returncode

def main():
    print("🤖 Smart GitHub Upload")
    print("=" * 40)
    
    # Check if we're in git repo
    if not os.path.exists(".git"):
        print("❌ Not a git repository!")
        print("Run: git clone https://github.com/yourusername/python-practice.git")
        return
    
    # Show git status
    print("\n📊 Current Status:")
    run_command("git status --short")
    
    # Ask for action
    print("\n🔧 Choose action:")
    print("1. Upload all changes")
    print("2. Upload specific files")
    print("3. Just commit (don't push)")
    print("4. Cancel")
    
    choice = input("\nSelect (1-4): ")
    
    if choice == '4':
        print("👋 Cancelled")
        return
    
    # Get commit message
    today = datetime.now().strftime("%Y-%m-%d")
    default_msg = f"Python practice {today}"
    msg = input(f"\n📝 Commit message [{default_msg}]: ").strip()
    msg = msg if msg else default_msg
    
    if choice == '1':
        # Upload all
        run_command("git add .")
        run_command(f'git commit -m "{msg}"')
        run_command("git push")
        
    elif choice == '2':
        # Show files to choose from
        print("\n📄 Changed files:")
        run_command("git status --porcelain")
        files = input("\nEnter filenames (space separated): ")
        if files:
            run_command(f"git add {files}")
            run_command(f'git commit -m "{msg}"')
            run_command("git push")
            
    elif choice == '3':
        # Just commit locally
        run_command("git add .")
        run_command(f'git commit -m "{msg}"')
        print("💾 Saved locally (not pushed to GitHub)")
    
    print(f"\n✅ Done! Time: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
