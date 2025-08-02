import os

filename = "my_script.py"

# تحقق من وجود الملف قبل تغيير صلاحياته
if os.path.exists(filename):
    os.chmod(filename, 0o775)
    print(f"✅ Changed permissions of '{filename}' to rwxrwxr-x (775)")
else:
    print(f"❌ File '{filename}' not found.")

