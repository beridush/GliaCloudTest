import os

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

name_dict = {}

def main():
    for url in urls:
        name = os.path.basename(url)
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    for t in sorted(name_dict.items(), key = lambda x: x[0])[:3]:
        print(t[0], t[1])


if __name__ == '__main__':
    main()