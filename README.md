# Understanding-and-Modifying-File-Permissions-with-Python
This project demonstrates how to understand and modify file permissions (e.g., `rwxrwxr-x`) in Unix-based systems using Python.


| Segment      | Description                       |
|--------------|-----------------------------------|
| `-`          | File type (e.g., `-` = file, `d` = directory) |
| `rwx` (owner)| Owner has read, write, execute    |
| `rwx` (group)| Group has read, write, execute    |
| `r-x` (other)| Others have read and execute only |

This mode is equivalent to numeric value `775`.

---

## 🖼️ Permissions Flowchart

![Permissions Flowchart](https://github.com/Aziz-AlTH/Understanding-and-Modifying-File-Permissions-with-Python/blob/main/Image2%20.png?raw=true)

---

## 🧪 Python Script: `change_perm.py`

This script changes the permission of a target file to `rwxrwxr-x` (775).
```
```python
import os

filename = "my_script.py"  # Replace with your target file

if os.path.exists(filename):
    os.chmod(filename, 0o775)
    print(f"✅ Changed permissions of '{filename}' to rwxrwxr-x (775)")
else:
    print(f"❌ File '{filename}' not found.")
```


🚀 How to Use
1-Create a file named my_script.py or any other file you want to modify.

2-Save the Python script above as change_perm.py.

3-Run the script using:

python3 change_perm.py

4-Check the permissions using:

ls -l my_script.py

📊 Permission Value Table

| Symbol | Binary | Octal | Meaning             |
| ------ | ------ | ----- | ------------------- |
| rwx    | 111    | 7     | Read + Write + Exec |
| rw-    | 110    | 6     | Read + Write        |
| r--    | 100    | 4     | Read only           |
| r-x    | 101    | 5     | Read + Execute      |


## ✍️ Created by: Abdulaziz Awad Al-Thabeti







