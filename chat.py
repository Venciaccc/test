#_*_ encoding=utf-8 _*_
import itchat, time,re
import tuling
itchat.auto_login()
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    txt = msg['Text']
    output=tuling.get_response(txt, storageClass = None,userName = None, userid = 'ItChat')
    itchat.send(output, msg['FromUserName'])
@itchat.msg_register('Text', isGroupChat = True)
def text_reply(msg):
    ttt='找我干嘛'
    if msg['isAt']:
      if len(msg['Text'])>2:
         ttt=msg['Text'].split()[1:]
      txt=tuling.get_response(ttt, storageClass = None, userName = None, userid = 'ItChat')
      itchat.send(u'@%s\u2005 %s'%(msg['ActualNickName'],txt), msg['FromUserName'])
@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'欢迎关注微信公众号《启辰信通》\n'
        + u'查看《每天一课》课程 ：回复每天一课或第n课\n', msg['RecommendInfo']['UserName'])
itchat.run()
