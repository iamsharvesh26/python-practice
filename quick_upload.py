# quick_upload.py
import subprocess
from datetime import datetime

print("🚀 GitHub Quick Upload")
print("=" * 30)

# Show what changed
print("\n📁 Checking for changes...")
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print(result.stdout)

# Ask for confirmation
choice = input("\n📤 Upload these changes to GitHub? (y/n): ")

if choice.lower() == 'y':
    # Get commit message
    default_msg = f"Practice update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    custom_msg = input(f"Commit message [{default_msg}]: ").strip()
    commit_msg = custom_msg if custom_msg else default_msg
    
    print(f"\n📝 Committing: '{commit_msg}'")
    
    # Execute git commands
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Staged changes")
        
        # Commit
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print("✅ Committed locally")
        
        # Push to GitHub
        subprocess.run(["git", "push"], check=True)
        print("✅ Pushed to GitHub!")
        
        print("\n🎉 All done! Check your repo at:")
        print("https://github.com/iamsharvesh26/python-practice")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
else:
    print("❌ Upload cancelled")
