import psutil


system = ["System", "services.exe", "svchost.exe",
          "csrss.exe", "fontdrvhost.exe", "conhost.exe", None]

for proc in psutil.process_iter():
    try:
        parent = proc.parent().name()
    except AttributeError:
        parent = None
    if parent not in system and proc.name() not in system:
        print(proc)
        try:
            print(proc.exe())
        except psutil.AccessDenied:
            print("Access denied to executable location.")
