from flask import Flask
from flask import request
import linecache

app = Flask(__name__)

# data structure to store the upper bounds of all files

# since max no of files are 30, storing max lines for all files
upper_bounds = [0]*10000

# return all chunk
def allFile(n):
    try:
        n = int(n)

        # check if file exists for particular n
        fptr = open(f"tmp/data/{n}.txt")
        content = fptr.readlines()
        fptr.close()

        # set upper_bound if not set
        if upper_bounds[n-1]==0:
            upper_bounds[n-1]=len(content)
        res = "".join(content)
        return res, 200
    except:
        return "Bad Request", 404

# return specific line of the file
def specificLine(n, m):
    try:
        m = int(m)
        n = int(n)

        # check if we have calculated the upper_bound in order to use linecache
        if upper_bounds[n-1]==0:
            fptr = open(f"tmp/data/{n}.txt")
            content = fptr.readlines()
            fptr.close()

            # setting upper_bound
            upper_bounds[n-1]=len(content)

            # check if the give index is accessible
            if m>upper_bounds[n-1] or m<=0:
                return f"Line number {m} exceeds the number of lines in the file, maximum lines are {upper_bounds[n-1]}", 404
            
            # 1 based indexing
            return content[m-1], 200

        # check if the give index is accessible
        if m>upper_bounds[n-1] or m<=0:
            return f"Line number {m} exceeds the number of lines in the file, maximum lines are {upper_bounds[n-1]}", 404

        # already calculated upper_bound, use linecache for optimization
        fileName = f"tmp/data/{n}.txt"
        res = linecache.getline(fileName, m, module_globals=None)
        return res
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
