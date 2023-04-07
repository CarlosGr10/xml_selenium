import os

def way():
    folder_contend = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/xml")
    print(folder_contend[0])

if __name__ == "__main__":
    way()