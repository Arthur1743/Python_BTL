
names = ["ANH", "HUY", "LONG", "AN"]
name = list(filter(lambda name: name.startswith("A"), names))

# In kết quả
print(f"Tên bắt đầu bằng chữ 'A': {name}")