import xml.etree.ElementTree as ET

# 读取 XML 文件
tree = ET.parse('books.xml')
root = tree.getroot()

# 遍历 XML 树
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text

    print(f"Title: {title}, Author: {author}, Year: {year}")
