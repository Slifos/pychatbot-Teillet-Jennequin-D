import os

dirPath = r"speeches"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
nom = ['Chirac' , 'Giscard dEstaing' , 'Hollande' , 'Macron' , 'Mitterand', 'Sarkozy']
for i in range(len(result)):
    for j in range(len(result[0]))