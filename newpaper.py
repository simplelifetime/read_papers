import pandas as pd

def reset():
    id = []
    name = []
    type = []
    content = []
    df = pd.DataFrame({"id": id, "name": name, "type": type, "content": content})
    df.to_csv("paper.csv", index=False, encoding='utf_8_sig')
    

if __name__ == '__main__':
    name = input("name:")
    type = input("type:")
    content = input("content:")
    df = pd.read_csv("paper.csv")
    newid = len(df.index)
    id = [newid]
    name = [name]
    type = [type]
    content = [content]
    df1 = pd.DataFrame({"id": id, "name": name, "type": type, "content": content})
    df = df.append(df1)
    df.to_csv("paper.csv", index=False, encoding='utf_8_sig')
