# 데이터 파일 불러오기
def read_data(filename):
    f = open(filename, 'rt')  # rt: read stream
    while True:
        data = f.readline()  # data = 11
        if data:
            res = yield int(data)
            print(f'sum : [{res}]')  # sum : 66 
        else:
            break
    f.close()
    return res

# 데이터 파일을 관리 --> 파일 for문으로 돌면서 yield from g
def delegate(*file_list):
    s = 0
    for filename in file_list:
        print('sending data')
        res = yield from read_data(filename)
        s, res = res, s  # s: 0 , res: 55 --> s: 55, res: 0 --> s: 210, res: 55  --> 183 ,411 = 411, 183 --> s = 411, res = 183
        print(f'the total sum of {filename} : [{s - res}]')
    return 'There is no data left'

# 실제 연산을 담당하는 함수
def make_sum(gen):
        s = 0
        data = gen.send(None)   # data = read_data(filename) 에서 yield int(data)
        while data:  # data : 1 2 3 4... 10 11 ... 30
            s += data   # s : 1 3 6 10... 55 66... 411
            try:
                data = gen.send(s)  
            except StopIteration as exc: 
                print(exc)
                break

if __name__ == "__main__":
    make_sum(delegate('data1.txt', 'data2.txt', 'data3.txt'))

