#! / Usr / bin / python


ithalat  os
 kodekleri içe aktar
ithalat  zamanı
 alt işlemi içe aktar
ithalat  sys
 rastgele içe aktar
dan  pyvirtualdisplay  ithalat  Display
dan  selenyum . webdriver . firefox . seçenekler  içe aktarma  Seçenekler
dan  selenyum  ithalat  webdriver
dan  selenyum . webdriver . firefox . firefox_binary  içe aktarma  FirefoxBinary

binary  =  FirefoxBinary ( 'base / firefox / firefox' )

Yeşil = " \ 033 [1; 33m"
Mavi = " \ 033 [1; 34m"
Gri = " \ 033 [1; 30m"
Sıfırla = " \ 033 [0m"
Kırmızı = " \ 033 [1; 31m"

AĞAÇLAR = 0
Kimlik  =  0

soyadı  =  rastgele . seçim ([ 'diana' , 'jakal' , 'boreson' , 'sinan' , 'zanyar' , 'lkafe' , 'kenny' , 'parker' , 'faye' , 'spivey' , 'simon' , 'miller' , 'wilson' , 'ryan' , 'jackson' , 'arkadaşlar' , 'tuckler' , 'turner' , 'counety' ,, 'andrews' , 'dunns' , 'barker' , 'reid' ])
useragents  =  'Mozilla / 5.0 (Windows NT 6.1; WOW64; Trident / 7.0; rv: 11.0; MSN 9.0; MSN 9.1; MSN 9.6; MSN 10.0; MSN 10.2; MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'


info  =  open ( './sms_support/phone' , 'r' )
info  =  bilgi . oku ()


ay  =  rastgele . seçim ([ '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ])
gün  =  rastgele . seçim ([ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '24' , '25' ,
yıl  =  rastgele . seçim ([ '1990' , '1994' , '2000' , '1992' , '1984' , '1986' , '1983' , '1980' , '1997' , '1987' , '1966' , '1999' , '1988' , '1989' ])


let  =  rastgele . seçim ([ 'lk' , 'sa' , 'df' , 'kg' , 'jq' , 'qw' , '3r' , 'ks' , 'gt' , 'ws' , 'gt' , 'lo' , 'yh' , 'qw' ])
let1  =  rastgele . seçim ([ '3' , '9' , '2' , '6' , '4q' , 'qw5' , '31' , 'k4' , '6' , '8s' , '9t' , '1o' , '8h' , '4w' ])
num  =  rastgele . seçim ([ '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' , '26' , '27' , '28' , '29' ])

şifre  =  rastgele . seçim ([ '75! x # + FmnfW3SK' , 'vL & pM2zVtV6NsEH4' , 'PKC-pK2XmfRG-7B' , 'UME * F4aKD! CV7' , 'eLU_U2 & # MsqT # @ 4 +' , 'xS? mVEy! d2khDsye' , 'L2tb + A97P = # s * WD $' , 'wv & + & sXhrWxw7cJ' , 'S + rD? R = z7? KaS2U' , 'Rj? HcnN7 * -jw = CKw' , 'SQ? 3Vx! J8vueyf2' , ' cunnsjs1736jn # ' , ' lmasdks128973 # !!! @ ' ])


telefon  =  bilgi . şerit (). bölünmüş ( ":" , 1 ) [ 0 ]
ad  =  bilgi . şerit (). bölünmüş ( ":" , 1 ) [ 1 ]

SMS_AMNT  =  int ( giriş ( Gri + "[" + Mavi + "SMS" + Gri + "] - [" + Mavi + "10" + Gri + "]" + Yeşil + ":" + Sıfırla ))
CALL_AMNT  =  int ( giriş ( Gri + "[" + Mavi + "ARAMA" + Gri + "] - [" + Mavi + "3" + Gri + "]" + Yeşil + ":" + Sıfırla ))


profile  =  web sürücüsü . FirefoxProfile ()
profili . set_preference ( "general.useragent.override" , kullanıcı aralıkları )


display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
görüntüler . başlangıç ()
 

br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' , firefox_profile = profil )


yazdırmak ( Gri + "(" + Yeşil + "Olabilir değil İş Telefonu Doğrulama çok kez kullanılmış ise" + Gri + ")" )
yazdırmak ( Gri + "KULLANMA:" + Reset + "" + Mavi + useragents + Reset )

br . get ( "https://accounts.google.com/SignUp?hl=tr-GB" )

zaman . uyku ( 14 )

br . find_element_by_name ( "Adı" ). send_keys ( str ( ad ))
br . find_element_by_name ( "Soyadı" ). send_keys ( str ( soyadı ))

uname  =  str ( soyadı + adı + num + let1 + let )

br . find_element_by_name ( "GmailAddress" ). send_keys ( str ( uname ))
br . find_element_by_name ( " Parola " ). send_keys ( str ( şifre ))
br . find_element_by_name ( "PasswdAgain" ). send_keys ( str ( şifre ))
br . find_element_by_name ( "Doğum Günü" ). send_keys ( str ( gün ))
br . find_element_by_name ( "Doğum Yılı" ). send_keys ( str ( yıl ))


m  =  '# \\ :' + ay + '> div: nth-child (1)'

br . find_element_by_id ( "Doğum Günleri" ). tıklayın ()
br . find_element_by_css_selector ( m ). tıklayın ()
sex  =  ':' + rastgele . seçim ([ 'f' , 'e' ])
br . find_element_by_id ( 'Cinsiyet' ). tıklayın ()
br . find_element_by_id ( seks ). tıklayın ()

br . find_element_by_name ( 'RecoveryPhoneNumber' ). temizle ()
br . find_element_by_name ( 'RecoveryPhoneNumber' ). send_keys ( str ( telefon ))
zaman . uyku ( 10 )

br . find_element_by_name ( 'gönder düğmesi' ). tıklayın ()
zaman . uyku ( 7 )
 True iken :
	dene :
		br . find_element_by_id ( 'tos-scroll-button' ). tıklayın ()
		zaman . uyku ( 4 )
	 İstisna hariç :
		br . find_element_by_id ( 'iagreebutton' ). tıklayın ()
		zaman . uyku ( 20 )
		mola

 True iken :
	dene :
		Eğer  ID  ==  SMS_AMNT :
			mola

		başka :
			br . find_element_by_name ( "SendCode" ). tıklayın ()
			Kimlik  =  Kimlik  +  1
			yazdır ( Gri + "[" + Mavi + str ( ID ) + Gri + "]" + Yeşil + "SMS gönderildi" )
			zaman . uyku ( 55 )
			br . find_element_by_id ( 'tekrar dene' ). tıklayın ()
			zaman . uyku ( 15 )

	 İstisna hariç :
		mola


 True iken :
	dene :
		eğer  çalışırsa  ==  CALL_AMNT :
			mola

		başka :
			AĞAÇLAR  =  AĞAÇLAR  +  1
			br . find_element_by_id ( 'signupidvmethod-ses' ). tıklayın ()
			zaman . uyku ( 2 )
			br . find_element_by_name ( "SendCode" ). tıklayın ()
			baskı ( Gri + "[" + Mavi + str ( TRIES ) + Gri + "]" + Kırmızı + "Aranan" )
			zaman . uyku ( 55 )
			br . find_element_by_id ( 'tekrar dene' ). tıklayın ()
			zaman . uyku ( 15 )

	 İstisna hariç :
		print ( Yeşil + "Bitti" )
		br . kapat ()
		görüntüler . durdur ()
		zaman . uyku ( 10 )
		mola



sys . çıkış ( 0 )
