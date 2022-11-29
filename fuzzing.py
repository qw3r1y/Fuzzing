import requests  
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = []
#It will be added here with the file location where our urls are.
with open("C:\\Users\\example\\example\\Python\\Tools\\urller.txt","r+") as file:
    for row in file:
        urls.append(row.split("\n")[0])

fuzzing = []      
#Here we will add the payload file with the location of the list we want our urls to come to the end. 
with open("C:\\Users\\example\\example\\Python\\Tools\\fuzzing.txt","r+") as filex:
    for row in filex:
        fuzzing.append(row.split("\n")[0])

    for y in fuzzing:
        try:
            for xi in urls:
                url_istek = xi+str(y)
                sonuc=requests.get(url_istek , allow_redirects=False, verify=False, timeout=5)
            
                if(sonuc.status_code == 200):
                    ths = open("fuzzz.txt", "a")
                    ths.writelines(url_istek +"\n")
                    ths.close()
                    print(url_istek)
                    
        except:
            print("Error")

        finally:
            pass

sensitive = []
#Here we will add the payload file with the location of the list we want our urls to come to the end.
with open("C:\\Users\\example\\v\\Python\\Tools\\sensitive.txt","r+") as filec:
    for row in filec:
        sensitive.append(row.split("\n")[0])

    for i in sensitive:
        try:
            for xi in urls:
                url_istek = xi+str(i)
                sonuc=requests.get(url_istek , allow_redirects=False, verify=False, timeout=5)
            
                if(sonuc.status_code == 200):
                    ths = open("vaov.txt", "a")
                    ths.writelines(url_istek +"\n")
                    ths.close()
                    print(url_istek)
                    
        except:
            print("Error")

        finally:
            pass
