import zipfile, shutil, os
src = r"C:\Users\18084\algebra\algebra-1-tutor.skill"
z = zipfile.ZipFile(src)
print("valid zip:", z.testzip() is None)
names = [n.replace("\\", "/") for n in z.namelist()]
print("entries:", len(names))
print("all under algebra-1-tutor/ :", all(n.startswith("algebra-1-tutor/") for n in names))
print("SKILL.md present:", "algebra-1-tutor/SKILL.md" in names)
print("unit files:", sum(1 for n in names if "/units/" in n))
dst = r"C:\Users\18084\algebra\algebra-1-tutor.zip"
shutil.copyfile(src, dst)
print("created:", dst, os.path.getsize(dst), "bytes")
