import multiprocessing
import time

start_time = time.time()

def count(name):
    for i in range(1, 50001):
        print(name, " : ", i)

num_list =['p1', 'p2', 'p3', 'p4']

if __name__ == '__main__' : 

    pool = multiprocessing.Pool(processes=2)# mutiprocessing 패키지의 pool 객체 생성(프로세스는 2개 지정)
    pool.map(count, num_list) #pool의 map 메소드를 활용해서 실행 할 count 메소드와 num_list 전달.
    pool.close() #리소스 낭비를 방지하기 위해 close호출
    pool.join() #작업 완료 대기 위해 join호출

print("--- %s seconds --- " % (time.time() - start_time))