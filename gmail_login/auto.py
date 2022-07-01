screenshot_path = r"./screenshot"

# def common_text():
# store the newly added lines in file2 on file3
f3 = open('D:\\TenXer\\gmail_login\\screenshot\\third.txt', "+a")
with open("D:\\TenXer\\gmail_login\\screenshot\\second.text", "r") as f1:
    with open('f2:D:\\TenXer\\gmail_login\\screenshot\\first.text', "r") as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            print("read", line1, line2)
            if not line1 and not line2:
                break
            if line2 is not None:
                if line1 == line2:
                    continue
                else:
                    print("line", line2)
                    f3.write(line2)

f3.close()

# common_text()
