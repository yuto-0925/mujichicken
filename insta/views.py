from django.shortcuts import render as ds
import mujichicken

def post_list(request):
    return ds(request, 'blog/post_list.html', {})

ds.title('Auto Instagram by Mujichiken')

#設定ファイルからの読み込み
setting_list = []
with open('自動いいね設定.txt') as f:
    for setting in f.readlines():
        setting_list.append(setting.rstrip())

username=ds.text_input('アカウントID', setting_list[0])
password=ds.text_input('パスワード', setting_list[1])
tagName=ds.text_input('自動いいねするハッシュタグ', setting_list[2])
likedMax=ds.number_input('自動いいねする数', 10, 10000)

answer = ds.button('開始')

if answer == True:
     mujichicken.insta_auto_like(username, password, tagName, likedMax)
     ds.write('自動いいねを実行しました')
else:
     ds.write('')
