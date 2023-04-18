import os
dir = "grokking modern system design interview for engineers managers"
files = os.listdir(dir)
for f in files:
    d = os.path.join(dir, f)
    if not os.path.isdir(d):
        continue
    #print(d)
    src_html=os.path.join(d, f + ".html")
    if not os.path.isfile(src_html):
        print(f'error {src_html} not a file')
        continue
    print(f"{f}\\{f}.html")
    #print(src_html)
    # number,name=f.split("-")
    # print(number)
    # number=int(number)
    # if(number>=100):
    #     continue
    # number+=100
    # dst_html=os.path.join(d,f"{number}-{name}.html")
    # os.rename(src_html,dst_html)
    # dst_d=os.path.join(dir,f"{number}-{name}")
    # os.rename(d,dst_d)
    #break
    #name, ext = os.path.splitext(f)
    # if ext != ".vtt":
    #     continue
    # dst_file = os.path.join(dir, f"{name}.srt")
    # print(src_file, "=>", dst_file)
    # os.system(f'ffmpeg -i "{src_file}" "{dst_file}"')