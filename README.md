# SSMTP Messenger 📲
A simple way for users to use a send-only sendmail emulator. 
## Abstract    
1. [Setup](#head1)    
2. [Weather Messaging](#head12)

## <a name= "head1"></a> Instructions

**1. Operating System**  
Before you start, you need to have at lease **one** of these platforms in place    
1. Windows 10 using a Linux subsystem
2. Ubuntu
3. Linux
4. Raspberry Pi 
  
**2. Google Account**    
1. Login to your **Gmail** account
2. Select **Security**.
3. Under "_Signing in to Google_" select 2-Step Verification.
4. At the bottom of the page, select App passwords.
5. Enter a name that helps you remember where you’ll use the app password.
6. Select **Generate**.
7. To enter the app password, follow the instructions on your screen. The app password is the 16-character code that will be used for your email password in the python script.
8. Select **Done**.   

**3. Open up your terminal**    
**Enter these commands below**   
```console 
foo@bar:~$ sudo apt update && sudo apt upgrade    
foo@bar:~$ sudo apt-get install ssmtp mailutils   
foo@bar:~$ sudo apt-get install postfix   
foo@bar:~$ sudo apt-get install ssmtp   
```
**4. Save original conf file**      
```console
foo@bar:~$ sudo mv /etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf.bak    
```
**5 . Create new conf file (with vi, or some other text editor)**    
```console
foo@bar:~$ sudo vi /etc/ssmtp/ssmtp.conf    
```
In your file content, apply these changes    
```shell
root=your_account@gmail.com
mailhub=smtp.gmail.com:587

FromLineOverride=YES
AuthUser=your_account@gmail.com
AuthPass=your_password
UseSTARTTLS=YES
UseTLS=YES

# Debug=Yes
```    
Now enter    
**ctrl o**     
**y** to save your file     
**ctrl x** to exit       

**6. Secure conf file**    
```console
foo@bar:~$ sudo groupadd ssmtp
foo@bar:~$ sudo chown :ssmtp /etc/ssmtp/ssmtp.conf
```    
Now lets create a text file to create some content for our message!    
```console
foo@bar:~$ nano test.txt
```    
In your file content, apply these changes  
```shell
Hello 1 2 3 
```   
Now enter    
**ctrl o**     
**y** to save your file     
**ctrl x** to exit   
 
**7. Last but not least, the test!**    
```console
foo@bar:~$ ssmtp recipient.address@some_domain.com < test.txt
```   

**Added bonus**    
Try texting from your computer to your phone! Look at link 3 for your carrier gateway            
```console
foo@bar:~$ ssmtp 1234567890@smsgateway < test.txt
```  
Try texting from your computer to your phone using shell!            
```console
foo@bar:~$ nano test.sh
```    
```bash 
#!/bin/bash
   ssmtp ssmtp 1234567890@smsgateway < test.txt
   echo "Message sent" #prints in console/terminal
```    
Now enter    
**ctrl o**     
**y** to save your file     
**ctrl x** to exit    
```console
foo@bar:~$ chmod 777 test.sh
foo@bar:~$ ./test.sh
Message sent
foo@bar:~$
```    

## <a name= "head12"></a> Weather    
Take your SSMTP messaging skills a bit further using the [OpenWeatherMap API](https://openweathermap.org/api)! After signing up for a free key,
you can use my [weatherapi.py](https://github.com/HerndonE/SSMTP-Messenger/blob/master/Code/weatherapi.py) script as a guide to get a weather report on your phone. The output for my code is  
<tr>
<th align="center"><img src="https://github.com/HerndonE/SSMTP-Messenger/blob/master/Images/WeatherOutput.jpg" width="100px;" style="max-width:100%;"><sub><br><b>Weather Output</b></sub></a><br></th>
</tr>

## References
[How to send mail from command line using gmail smtp server](https://stackoverflow.com/questions/38391412/raspberry-pi-send-mail-from-command-line-using-gmail-smtp-server
)    
[How to write a shell script](https://vitux.com/how-to-write-a-shell-script-in-ubuntu/)    
[SMS gateway lookup](https://en.wikipedia.org/wiki/SMS_gateway)    
[Cell phone lookup](https://www.spokeo.com/reverse-phone-lookup?g=phone_gs_bfree&campaignid=1814250205&adgroupid=70553735718&creative=344872239261&targetid=kwd-109356030&placement=&gclid=Cj0KCQiAqNPyBRCjARIsAKA-WFzNn2-wWRnofVmML69KbU-rKOqqAH2PDRCu0XjOvmMniAsEvSw2K-QaAojZEALw_wcB
)

## Terminology    
1. What is **ssmtp**?    
SSMTP is a send-only sendmail emulator for machines which normally pick their mail up from a centralized mailhub.    
2. What is **mailutils**?    
Mailutils is a _swiss army knife_ of electronic mail handling and offers a set of utilities and daemons for processing e-mail.    
3. What is **postfix**?    
Postfix is a free open-source mail transfer agent (MTA) that routes and delivers electronic mail.    
