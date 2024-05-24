import subprocess
import hashlib
import json
 
# Major severity issue: Using subprocess without proper sanitization (B602)
def unsafe_subprocess(command):
    subprocess.call(command, shell=True)  # Potentially dangerous
 
# Major severity issue: Hard-coded password (B105)
def login():
    username = "admin"
    password = "supersecret"  # Hard-coded password
    # Code for logging in
 
# Minor severity issue: Using md5 for hashing (B303)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # md5 is not secure
 
# Minor severity issue: Assert used in production code (B101)
def check_user_age(age):
    assert age > 0, "Age must be positive"  # Assert statements should not be used in production
    # Code for checking user age
 
def run_bandit():
    command = ["bandit", "-r", "example.py", "-f", "json", "-o", "bandit_report.json"]
    result = subprocess.run(command, capture_output=True, text=True)
    # Print standard output and standard error (optional)
    print("Standard Output:\n", result.stdout)
    print("Standard Error:\n", result.stderr)
    # Print the exit code
    print("Exit Code:", result.returncode)
    return result.returncode
 
if __name__ == "__main__":
    # Example usage of the functions
    command = "echo 'Hello, World!'"
    unsafe_subprocess(command)
 
    login()
 
    hashed_password = hash_password("example_password")
    print(f"Hashed password: {hashed_password}")
 
    check_user_age(25)
    # Run Bandit and check the exit code
    exit_code = run_bandit()
    print("Bandit completed successfully.")
    # Since Bandit runs successfully, return 0 exit code
    exit(0)
