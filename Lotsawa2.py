#!/usr/bin/env python3
#print("Content-type: text/html") 
#-----------------------------------
import yaml
import re

strn='''༁ྃ༔ བླ་མའི་ཐུགས་སྒྲུབ་རྡོ་རྗེ་དྲག་རྩལ་ལས༔ ཞལ་གདམས་ལམ་རིམ་ཡེ་ཤེས་སྙིང་པོ་བཞུགས་སོ༔
སངས་རྒྱས་བསྟན་པའི་རྒྱལ་མཚན་ཕྱོགས་བཅུར་བསྒྲེངས༔ དང་པོ་༼མཚན་དངོས་བཀོད་༽ནི།  ལས་ཅན་སྨིན་གྲོལ་བྱང་ཆུབ་ལམ་ལ་བཀོད༔ 
འབྲེལ་ཚད་དོན་ལྡན་ངོ་མཚར་བསམ་ལས་འདས༔ 
མཚན་ལས་བརྩམས་པའི་མཐའ་དཔྱད་དོ། 
དང་པོ་༼མཚན་དངོས་བཀོད་༽ནི། བླ་མའི་ཐུགས་སྒྲུབ་རྡོ་རྗེ་དྲག་རྩལ་ལས༔ ཞལ་གདམས་ལམ་རིམ་ཡེ་ཤེས་སྙིང་པོ༔ ཞེས་པའོ།། །
བླ་མའི་ཐུགས་སྒྲུབ་རྡོ་རྗེ་དྲག་རྩལ་ལས༔ ཞལ་གདམས་ལམ་རིམ་ཡེ་ཤེས་སྙིང་པོ༔ ཞེས་པའོ།། །
ཞལ་གདམས་སྙིང་བྱང་ལས། རང་བྱུང་པདྨ་བདག་ཉིད་ཀྱི༔ དགོངས་པའི་ཀློང་ནས་རང་ཤར་བ༔ ཡང་ཟབ་ཐུགས་ཀྱི་གྲུབ་པ་ནི༔ ཞེས་དང༌། 
ཨོ་རྒྱན་བདག་གིས་རྒྱུད་ལུང་དང་༔ མན་ངག་གཞན་ལ་བརྟེན་ནས་ནི༔ འབྲེལ་བའི་ཚུལ་དུ་མ་བཀྲལ་བར༔ རྒྱུད་ལུང་མན་ངག་ངེས་པའི་དོན༔ སྙིང་པོ་ལས་ཀྱང་སྙིང་པོའི་བཅུད༔ 
ཐུགས་ཀྱི་ཐིག་ལེར་རབ་ཞུགས་པོ༔  ཆོས་ཉིད་རང་སྒྲར་སྣང་བས་ན༔ རྒྱུད་དང་མི་འགལ་ལུང་དང་མཐུན༔ མན་ངག་མྱོང་བས་ཁྱད་འཕགས་པ༔ ཞེས་གསུངས་པ་ལྟར་རོ། 
འབྲེལ་ཚད་དོན་ལྡན་ངོ་མཚར་བསམ་ལས་འདས༔ '''

# 0. Подготовка (форматирование) строки/текста
#strn=input()

# 0.1. Название
strn=re.sub(f'\n*(\S+?བཞུགས་སོ[།༔])\n*', r'<h1 class="Toc">\1</h1>\n',strn)

# 0.2. Тема - подзаголовок
strn=re.sub(f'\n*(\S+?ནི[།༔])\n*', r'\n<h4 class="Topic">\1</h4>\n',strn)   

# 0.3. из А (источник цитаты)
strn=re.sub(f'(\S+?ལས[།༔])', r'<div class="cite_src">\1</div>',strn)

#  0.4 Цитата
strn=re.sub(r'(ལས[༔།]</div>\s)(.+?[༔།]+)([\s།]+ཞེས)', '\\1<div class="cite">\\2</div>\\3',strn, 0)

# 0.5 Конец абзаца
strn=re.sub(f'(\S+?ོ[།༔]+\s+)', r'\1</br>',strn)    

print(strn)
#----------------------------------------------------------
 
# 1. Разбираем строку для перевода
# 1.1 отлепляем ->འི от слога
for syl in ['འི', 'འིས', 'འང', 'འམ', 'འོ']: # исключил доп.строк - 'ར', 'འུ'  
    strn=re.sub(f'([༄༅། ༿༧་|<\a-z>]*\S+?)({syl})([་༔།༾ཿ |]+)', r"\1་\2\3", strn) 

# 1.2. Парсим Строку для перевода -> list список слов из строки 
strn_lst=re.findall(r'[༄༅།༼༽ ༿༧་|<\a-z>]*(\S+?)[་༔།༾ཿ |]+', strn)

# 1.3. присоединяем персонификаторы к пред слогу в -> strn_lst
for ind, syl in enumerate(strn_lst):
    if syl in ['པོ', 'བ', 'བོ', 'མོ', 'ཀོ', 'ཅན', 'ལྡན', 'མཁན']: # исключил - མ, ཀ, ཁ, ག, པ
        strn_lst[ind-1]=strn_lst[ind-1]+'་'+strn_lst.pop(ind)

# TODO Усложняем логику парсинга
#print(res_strn)
strn_lst=list(set(strn_lst))
strn_lst.sort(key=len, reverse=True) # сортируем - max_len в начало
#print(strn_lst)

# --------------------------------------------------------

# 2. Разбираем строку для перевода
# strn              исходная строка для перевода
# strn_lst          список слов из строки для перевода
# dct_ptcl          словарь частиц из Dict.yaml
# sent_lst          список сочетаний со словом из strn_lst

res_strn=strn     # копия исходной строка для перевода
res_dct={}        # словарь найденных вхождений sent в исход строку 

#print(res_strn)
strn_lst=list(set(strn_lst))
strn_lst.sort(key=len, reverse=True) # сортируем - max_len в начало
#print(strn_lst)

# 2.А. Парсим Dict.yaml -> dict
with open('Dict.yaml', 'r', encoding='utf-8') as f:
    dct_ptcl=yaml.full_load(f)
    
for ind, syl in enumerate(strn_lst): # по кажд уник слогу в strn_lst
    pattern=f'\'(\S*{syl}\S*?)[་།༔]*\':'

    # 2.Б. Поиск по Dict.dict всех вариантов куда входит слог из strn_lst -> sent_lst[список_словосочетаний]
    sent_lst=list(set(re.findall(pattern, str(dct_ptcl))))
    sent_lst.sort(key=len, reverse=True) # сортируем - max_len в начало

    # 2.В. Поиск по strn каждого уник из sent_lst в строке
    for sent in sent_lst:
        if sent in strn and sent not in res_dct: # если sent в исход строке И sent не находили ранее
            strn=re.sub(f'([་།༽༼ ༿]+)({str(sent)})([་༽།༔༾]+)', r'\1|\3', strn) # из исход строки убираем найденное sent         
            res_strn=re.sub(f'([་།༔༽༼]+)({str(sent)})([༔་༽།]+)', '\\1[\\2]\\3', res_strn, 0, re.MULTILINE) #в дубль_строке заменяем sent
            res_dct[sent]=dct_ptcl[sent] # словарь найденных вхождений sent в исход строку

#----------------------------------------------------------------------------------

#3. Создаем строки вывода с HTML тегами
dct_str=""
lst=list(dict.fromkeys(re.findall(r'\[(\S+?)\]', res_strn)))
#print(lst)
cnt=1
for ind, k in enumerate(lst): # идем по строке
    # создаем тэги для строки
    res_strn=res_strn.replace(f'[{k}]', f'<dfn class="cc" title="{res_dct[k]}"><a id="{cnt}_" href="#_{cnt}">{k}</a></dfn>')
    #создаем тэги для словарика
    dct_str+=f'<p id="_{cnt}">{cnt} <a lang="bo" href="#{cnt}_">{k}</a> = {res_dct[k]}</p>\n'#завернуть в тиб тег
    cnt+=1
#print(res_strn)
#print(dct_str)

#----------------------------------------------------------------------------------

#4.а) Запись в HTML файл
from IPython.core.display import display, HTML

with open('Result_Lotsawa.html', 'r', encoding='utf-8') as f:
    res_html=f.read()       
    
    #пишем тэги для строки
    res_html=re.sub(r'<section lang="bo">\n([\s\S]*?)</section>', f'<section lang="bo">\n{res_strn}\n</section>',res_html)
    #пишем тэги для словарика
    res_html=re.sub(r'<section class="dict">\n([\s\S]*?)</section>', f'<section class="dict">\n{dct_str}</section>',res_html)

with open('Result_Lotsawa.html', 'w', encoding='utf-8') as wf:   
    wf.write(res_html)

# ИЛИ 4.б) Вывод во фрейме если работаем в JypyterLab
#from IPython.display import IFrame
#IFrame(src='\Result_Lotsawa.html', width=910, height=600)
	
print (color.BOLD + strn + color.END) 
print (color.BOLD + res_strn + color.END) 
print(*res_dct.items(), sep="\n")