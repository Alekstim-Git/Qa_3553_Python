# with - контекстный менеджер. Создали файл greeting.txt
with open('greeting.txt','w',encoding='utf-8') as file:
    file.write('Hello, automated tests!\n')
    file.write('Second line')

#file = open(.....)  раньше так писали старые коды
#file.close()

# 'r' - read -->
# 'w' - write -->
# 'a' - append -->
# 'r+' - read & write
# 'rb', 'wb' - pdf, screenshots

# Режим 'r' (read — чтение) — это режим, который открывает
# файл исключительно для выверения и чтения информации из него.
# В этом режиме Python не позволит тебе ничего записать или изменить внутри файла.

#(write — запись) — это режим, который открывает файл исключительно для
# записи данных.

#(append — добавление) — это режим, который открывает файл для дозаписи
# данных в самый конец.


def log_test_result(test_name, status):
    with open('test_run.log','a',encoding='utf-8') as log_file:
        log_file.write(f'{test_name}:{status}\n')

log_test_result('test_login','passed')
log_test_result('test_registration','FAILED')
log_test_result('test_logout','Passed')

