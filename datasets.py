def get_dataset(url: str = None, p: str = None):
    """Функция получает на вход HTTP ссылку на файл с данными и сохраняет его в соответствующий файл.
    Иногда функция пандас read_csv с переданным http выдет ошибку, данная функция это исправляет"""
    import requests
    file_name = url.split('/')[-1]
    try:
        resp = requests.get(url)
        status_code = resp.status_code
        if status_code == 200:
            with open(f'{p}/{file_name}', 'wb') as f:
                f.write(resp.content)

            print('Success!!!')
            return f'{p}/{file_name}'
        else:
            print(f'Somthing wrong with url: Error {status_code} !!!')
    except:
        print(f'Error of downloading file...')


if __name__ == "__main__":
    url = 'https://flibusta.site/b/534092/epub'
    p = 'Data'
    print(get_dataset(url, p))
