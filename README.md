# Abstract    
1. [Setup](#head1)    
2. [Weather Messaging](#head12)

# <a name= "head1"></a> Instructions

**Before you start, you need to have one of these platforms in place**    
Platforms    
 Windows 10 using a Linux subsystem, Ubuntu, Linux, Raspberry Pi   
 
**1. Google account setting**    
1. Login to your **Gmail** account
2. Go to: **Settings** -> **Accounts and Import** -> **Other Google Account settings**    
3. Go to: **Personal info & privacy** -> **Account overview**    
4. Go to: **Sign-in & security** -> **Connect apps & sites**    
5. Set option _Allow less secure apps_ to **ON**    

**2. Open up your terminal**    
**Enter these commands below**   
```console 
foo@bar:~$ sudo apt update && sudo apt upgrade    
foo@bar:~$ sudo apt-get install ssmtp mailutils   
foo@bar:~$ sudo apt-get install postfix   
foo@bar:~$ sudo apt-get install ssmtp   
```
**3. Save original conf file**      
```console
foo@bar:~$ sudo mv /etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf.bak    
```
**4 . Create new conf file (with vi, or some other text editor)**    
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

**5. Secure conf file**    
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
 
**6. Last but not least, the test!**    
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

# <a name= "head12"></a> Weather    
Take your SSMTP messaging skills a bit further using the [OpenWeatherMap API](https://openweathermap.org/api) ! After signing up for a free key
you can use my [weatherapi.py]() script as a guide to get a weather report on your phone. The output for my code is  
<tr>
<th align="center"><img src="" width="100px;" style="max-width:100%;"><sub><br><b>Weather Output</b></sub></a><br></th>
</tr>

# References
Link 1. [How to send mail from command line using gmail smtp server](https://stackoverflow.com/questions/38391412/raspberry-pi-send-mail-from-command-line-using-gmail-smtp-server
)    
Link 2. [How to write a shell script](https://vitux.com/how-to-write-a-shell-script-in-ubuntu/)    
Link 3. [SMS gateway lookup](https://en.wikipedia.org/wiki/SMS_gateway)    
Link 4. [Cell phone lookup](https://www.spokeo.com/reverse-phone-lookup?g=phone_gs_bfree&campaignid=1814250205&adgroupid=70553735718&creative=344872239261&targetid=kwd-109356030&placement=&gclid=Cj0KCQiAqNPyBRCjARIsAKA-WFzNn2-wWRnofVmML69KbU-rKOqqAH2PDRCu0XjOvmMniAsEvSw2K-QaAojZEALw_wcB
)

# Terminology    
1. What is **ssmtp**?    
SSMTP is a send-only sendmail emulator for machines which normally pick their mail up from a centralized mailhub.    
2. What is **mailutils**?    
Mailutils is a _swiss army knife_ of electronic mail handling and offers a set of utilities and daemons for processing e-mail.    
3. What is **postfix**?    
Postfix is a free open-source mail transfer agent (MTA) that routes and delivers electronic mail.    
