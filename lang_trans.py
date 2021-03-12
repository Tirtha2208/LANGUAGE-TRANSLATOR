from google_trans_new import google_translator,LANGUAGES


print("*********************************************")
print("*          THE LANGUAGE TRANSLATOR          *")
print("*********************************************\n\n")
key_list=list(LANGUAGES.keys())
val_list=list(LANGUAGES.values())
choice=1
while(choice!=3):
    print("1. All the languages available\n2. Translate a Sentence\n3. Exit\n\n")
    choice=int(input("Enter your choice\n"))

    if(choice==1):
        for i in val_list:
            print(i,end=" , ")
        print("\n")
        continue
    elif(choice==2):
        sor=input("Enter the source language\n")
        des=input("Enter the target language\n")
        sen=input("Enter the Sentence\n")
        sor=sor.lower()
        des=des.lower()
        sor=val_list.index(sor)
        des=val_list.index(des)
        sk=key_list[sor]
        dk=key_list[des]
        translator = google_translator()  
        translate_text = translator.translate(sen,lang_src=sk,lang_tgt=dk)  
        print("The Translated text is:")
        print(translate_text+"\n")
        continue
    elif(choice==3):
        print("Thank you for using the Language Translator\n")
        break
    else:
        print("Wrong Choice")
        continue

