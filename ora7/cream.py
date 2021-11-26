from easygui import *

user_response = msgbox("Hello There!",title="Hello",ok_button="Hi",image="python_logo.png")
print(user_response)
flavor = buttonbox("What is your favourite flavor?",title="Icecream"
                           ,choices = ['Vanillia' ,'Chocolate','strawberry','cherry'],
                           default_choice="Vanillia")
msgbox("you picked: " + flavor)
flavor2 = choicebox("What is your favourite flavor?",title="Icecrea2m"
                           ,choices = ['Vanillia' ,'Chocolate','strawberry','cherry'],
                           preselect=2)
msgbox("you picked: " + flavor2)
flavor = enterbox("What is your favourite flavor?",title="Icecream",default="Körte")
if flavor is not None :
    msgbox("you picked: " + flavor)
else :
    msgbox("Cancel gombra nyomott")
