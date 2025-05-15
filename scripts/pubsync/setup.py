#!/usr/bin/env python3
"""
Cross-platform installer script for the publication sync system.
This script checks dependencies and sets up the environment for the sync system.
"""

import os
import sys
import subprocess
import platform

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f" {text}")
    print("=" * 60)

def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required.")
        print(f"Current Python version: {platform.python_version()}")
        return False
    print(f"✓ Python {platform.python_version()} detected (compatible).")
    return True

def install_dependencies():
    """Install required Python packages."""
    print("Installing required dependencies...")
    packages = ["bibtexparser", "pyyaml"]
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error installing {package}. Please install manually: pip install {package}")
            return False
    
    return True

def make_scripts_executable():
    """Make scripts executable on Unix-based systems."""
    if os.name != 'nt':  # Not Windows
        print("Making scripts executable...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        try:
            # Make Python script executable
            os.chmod(os.path.join(script_dir, "bibtex_to_cv.py"), 0o755)
            # Make shell script executable
            os.chmod(os.path.join(script_dir, "sync_publications.sh"), 0o755)
            print("✓ Scripts are now executable.")
        except Exception as e:
            print(f"Warning: Could not make scripts executable: {e}")
            print("You may need to run: chmod +x scripts/pubsync/*.py scripts/pubsync/*.sh")
    return True

def check_project_structure():
    """Check if the project structure is correct."""
    print("Checking project structure...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    potential_root = os.path.abspath(os.path.join(script_dir, "../.."))
    
    bibtex_dir = os.path.join(potential_root, "_bibliography")
    data_dir = os.path.join(potential_root, "_data")
    
    if not os.path.isdir(bibtex_dir):
        print(f"Warning: _bibliography directory not found at {bibtex_dir}")
        print("The sync script may not be able to find your BibTeX files.")
    else:
        print(f"✓ _bibliography directory found.")
        
    if not os.path.isdir(data_dir):
        print(f"Warning: _data directory not found at {data_dir}")
        print("The sync script may not be able to find your CV YAML file.")
    else:
        print(f"✓ _data directory found.")
    
    return True

def create_shortcut():
    """Create a desktop shortcut on Windows."""
    if os.name == 'nt':  # Windows
        try:
            print("Would you like to create a desktop shortcut? (y/n)")
            choice = input("> ").strip().lower()
            if choice != 'y':
                return True
                
            import winshell
            from win32com.client import Dispatch
            
            script_dir = os.path.dirname(os.path.abspath(__file__))
            batch_path = os.path.join(script_dir, "sync_publications.bat")
            
            desktop = winshell.desktop()
            shortcut_path = os.path.join(desktop, "Sync Publications.lnk")
            
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = batch_path
            shortcut.WorkingDirectory = script_dir
            shortcut.IconLocation = sys.executable
            shortcut.save()
            
            print(f"✓ Shortcut created on desktop: 'Sync Publications'")
        except Exception as e:
            print(f"Could not create shortcut: {e}")
            print("You can still run the script directly.")
    
    return True

def main():
    """Main installer function."""
    print_header("Publication Sync System Installer")
    
    print("This script will set up the publication sync system on your computer.")
    print("The system synchronizes publications from BibTeX to your CV file.\n")
    
    if not check_python_version():
        return False
        
    if not install_dependencies():
        return False
        
    if not make_scripts_executable():
        return False
        
    if not check_project_structure():
        return False
    
    try:
        create_shortcut()
    except ImportError:
        print("Note: Windows shortcut creation requires pywin32 and winshell packages.")
        print("If you want a desktop shortcut, install them with:")
        print("  pip install pywin32 winshell")
        
    print_header("Installation Complete")
    print("You can now run the sync script using:")
    
    if os.name == 'nt':  # Windows
        print("  - Double-click on sync_publications.bat")
        print("  - Or run: python bibtex_to_cv.py")
    else:  # Unix (Mac/Linux)
        print("  - Run: ./sync_publications.sh")
        print("  - Or run: python3 bibtex_to_cv.py")
    
    print("\nWould you like to run the sync script now? (y/n)")
    choice = input("> ").strip().lower()
    
    if choice == 'y':
        print("\nRunning sync script...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "bibtex_to_cv.py")
        
        if os.name == 'nt':  # Windows
            subprocess.call([sys.executable, script_path])
        else:  # Unix
            subprocess.call([script_path])
    
    print("\nThank you for installing the Publication Sync System!")
    return True

if __name__ == "__main__":
    success = main()
    
    # Keep terminal window open on Windows if run by double-clicking
    if os.name == 'nt' and not sys.stdin.isatty():
        print("\nPress Enter to exit...")
        input()
    
    sys.exit(0 if success else 1)
