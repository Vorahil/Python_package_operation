def print_file_info(file_name):#读取文件内容
    f=None
    try:
        f=open(file_name,"r",encoding="UTF-8")
        content = f.read()
        print("The content of the file is :")
        print(content)
        for line in f:
            print(line)
    except Exception as e:
        print(f"You are wrong,because{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):#追加信息
    f=open(file_name,"a",encoding="UTF-8")
    f.write(str(data))
    f.write("\n")
    f.close()

if __name__=="__main__":
    print_file_info("D:/001.txt")
    append_to_file("D:/001.txt",135)

    append_to_file("D:/001.txt", 135)

    append_to_file("D:/001.txt", 135)
    print_file_info("D:/001.txt")