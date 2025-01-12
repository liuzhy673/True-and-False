import fitz  # PyMuPDF

# 打开 PDF 文件
doc = fitz.open('D:\\Desktop\\Final_Report_READ_ME.pdf')

# 获取总页数
total_pages = len(doc)

# 删除最后三页
for page_num in range(total_pages - 1, total_pages - 4, -1):
    doc.delete_page(page_num)

# 保存修改后的 PDF 文件
doc.save('D:\\Desktop\\Final_Report_READ_ME_1.pdf')
doc.close()
