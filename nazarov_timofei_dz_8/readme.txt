# Домашнее задание к 8му уроку.
1
import re

RE_EMAIL_V = re.compile(r'((^[A-Za-z0-9])(?:[._-][A-Za-z0-9])[A-Za-z0-9_-]+(?:[._-][A-Za-z0-9])[A-Za-z0-9_-]+\@)(['
                        r'A-Za-z0-9]([A-Za-z0-9-]+)\.)[A-Za-z]+$')


# email = 'someone@geekbrains.ru' 'm_0li.il@mail.ru']:   'wапт.@.w'
def email_parse(mail):
   #for mail in ['s.omeo_ne@gg-b.ru', 'm_0li.il@mail.ru', 'wапт.@.w']:
    if RE_EMAIL_V.match(mail):
        #print(RE_EMAIL_V.match(mail))
        item = re.match(r'(?P<username>\S+)@(?P<domain>\S+)', mail)
        res = item.groupdict()
        print(res)
        return res
        #print(d)
    else:
        msg = f'wrong e-mail: {mail}'
        raise ValueError(msg)


email_parse('s.ome@geek.ru')

