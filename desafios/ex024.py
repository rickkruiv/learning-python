city = str(input('Qual cidade você mora? ')).upper().strip()
find = city[:5] == 'SANTO'
print('Sua cidade tem santos no nome? {}'.format(find))