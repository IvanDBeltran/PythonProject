from os import mkdir

contents = ["Yeah, this is a piece of content",
            "Yup, this is another piece of content",
            "wow, I am also a piece of content"]

filenames = ["content1.txt", "content2.txt", "content3.txt"]



for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)
    file.close()