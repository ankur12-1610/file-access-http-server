from flask import Flask
from flask import request
import linecache

app = Flask(__name__)

# return all chunk
def allFile(n):
    try:
        # check if file exists for particular n
        fptr = open("tmp/data/"+n+".txt")
        content = fptr.readlines()
        fptr.close()
        res = "".join(content)
        return res, 200
    except:
        return "Bad Request", 404

# return specific line of the file
def specificLine(n, m):
    try:
        # check if file exists for particular n
        m = int(m)
        fileName = f"tmp/data/{n}.txt"
        fptr = open(fileName)
        # res = linecache.getline(fileName, m, module_globals=None)
        # return res
        content = fptr.readlines()
        fptr.close()
        # print(content)
        maxi = len(content)

        # check if the give index is accessible
        if m>maxi or m<=0:
            return f"Line number {m} exceeds the number of lines in the file, maximum lines are {maxi}", 404
        
        # 1 based indexing
        return content[m-1], 200
    except:
        return "Bad Request", 404

@app.route('/data', methods=['GET'])
def accessData():
    n = request.args.get('n')
    m = request.args.get('m')

    # if only n is provided
    if not m:
        return allFile(n)
    
    # check if given argument is numeric or not
    if not m.isnumeric():
        return "Return valid m, it must be a number within valid range", 404

    return specificLine(n, m)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
