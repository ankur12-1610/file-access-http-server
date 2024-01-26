# Headout: Optimize HTTP Server
> A simple HTTP server who works wonders

#### Note: I have created two versions of the problem statement, one is the basic using readlines (refer [#73f886f](https://github.com/ankur12-1610/file-access-http-server/commit/73f886f4e38e9078b5a8679b65dda3c4a7c55b54)) and the latest one is optimized using linecache and storing upper_bound for every line (refer [#d476ab7](https://github.com/ankur12-1610/file-access-http-server/commit/d476ab70bf94082ac72e9b6ce0299513d2281a53)))

### Endpoints:
- `/data` is the endpoint
- Parameters passed in the url: `/data?n=1&m=20` or `data?n=1`

Dataset:
> `tmp/data/1.txt` exists in the dataset
```
Hi
Headout
```

Sample Input1: `/data?n=1&m=1`

Sample Output1:
```
Hi
```

Sample Input2: `/data?n=1`

Sample Output2:
```
Hi
Headout
```

## Running the API
- To run locally: `python3 app.py`
- Building the Docker image: `docker build -t file-access-http-server . && docker run -dp 8080:8080 --memory="1500m" --cpus 2.0 file-access-http-server`

## Generating test data:
- Run `file_generate.py`, adjust the size of files and no of files in the code