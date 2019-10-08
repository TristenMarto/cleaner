import os
from selenium import webdriver

current = os.getcwd()
browser = webdriver.Chrome

new_name = input("naam voor nieuwe map: ")

homebase = "/Users/tristen.assenmacher/Downloads"
parent = "/Users/tristen.assenmacher/Desktop/Studie/projects"
target = os.path.join(parent, new_name)


print(f"""
je bent in {current}, hebt een pad naar {parent} en hebt als target {target}.
Je nieuwe map heet {new_name}
""")

os.mkdir(target)
os.chdir(target)
current = os.getcwd()
print(f"nu ben je in {current}")