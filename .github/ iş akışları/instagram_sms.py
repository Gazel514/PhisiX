#! / Usr / bin / python

ithalat  os
 kodekleri içe aktar
ithalat  zamanı
 alt işlemi içe aktar
ithalat  sys
 rastgele içe aktar
dan  pyvirtualdisplay  ithalat  Display
dan  selenyum  ithalat  webdriver
dan  selenyum . webdriver . firefox . firefox_binary  içe aktarma  FirefoxBinary

binary  =  FirefoxBinary ( 'base / firefox / firefox' )

Yeşil = " \ 033 [1; 33m"
Mavi = " \ 033 [1; 34m"
Gri = " \ 033 [1; 30m"
Sıfırla = " \ 033 [0m"
Kırmızı = " \ 033 [1; 31m"


SMS_AMNT  =  int ( giriş ( Gri + "[" + Mavi + "SMS" + Gri + "] - [" + Mavi + "10" + Gri + "]" + Yeşil + ":" + Sıfırla ))

#
zaman aşımı  =  60
iD  =  0

soyadı  =  rastgele . seçim ([ 'diana' , 'jakal' , 'boreson' , 'sinan' , 'zanyar' , 'lkafe' , 'kenny' , 'parker' , 'faye' , 'spivey' , 'simon' , 'miller' , 'wilson' , 'ryan' , 'jackson' , 'arkadaşlar' , 'tuckler' , 'turner' , 'counety' ,, 'andrews' , 'dunns' , 'barker' , 'reid' ])
rnd_char  =  rastgele . seçim ([ '2932' , '__837' , '9_82' , '29394' , '4_2_4' , '72' , '09' , '123' , '_0_' , '_9_' ])
rnd_char2  =  rastgele . seçim ([ '0' , '98' , 'lade' , 'sk' , 'ks' , 'de' , 'le' , 'qe' , 'sz' , 'mb' , 'lo' , 'kalem' , 'ku' , 'iq' ])

useragents  =  rasgele . seçim ([
	'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (GHTo gibi KHTML) Chrome / 59.0.3071.115 Safari / 537.36' ,
	'Mozilla / 5.0 (Windows NT 6.2; WOW64; rv: 50.0) Gecko / 20100101 Firefox / 50.0' ,
	'Mozilla / 5.0 (Windows NT 6.1) AppleWebKit / 537.36 (KHTML, Gecko gibi) Chrome / 60.0.3112.78 Safari / 537.36 OPR / 47.0.2631.55' ,
	'Mozilla / 5.0 (X11; Heathrow / 1.4; Linux i686; rv: 30) Gecko / 30 Firefox / 30' ,
	'Mozilla / 5.0 (Windows NT 6.1; WOW64; Trident / 7.0; rv: 11.0; MSN 9.0; MSN 9.1; MSN 9.6; MSN 10.0; MSN 10.2; MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'
])

şifre  =  rastgele . seçim ([ '75! x # + FmnfW3SK' , 'vL & pM2zVtV6NsEH4' , 'PKC-pK2XmfRG-7B' , 'UME * F4aKD! CV7' , 'eLU_U2 & # MsqT # @ 4 +' , 'xS? mVEy! d2khDsye' , 'L2tb + A97P = # s * WD $' , 'wv & + & sXhrWxw7cJ' , 'S + rD? R = z7? KaS2U' , 'Rj? HcnN7 * -jw = CKw' , 'SQ? 3Vx! J8vueyf2' , ' cunnsjs1736jn # ' , ' lmasdks128973 # !!! @ ' ])
info  =  open ( 'sms_support / phone' , 'r' )
info  =  bilgi . oku ()

telefon  =  bilgi . şerit (). bölünmüş ( ":" , 1 ) [ 0 ]
ad  =  bilgi . şerit (). bölünmüş ( ":" , 1 ) [ 1 ]
fullname  =  str ( ad + soyadı )
uname  =  str ( soyadı + rnd_char + rnd_char2 )

profile  =  web sürücüsü . FirefoxProfile ()
profili . set_preference ( "general.useragent.override" , kullanıcı aralıkları )

yazdırmak ( Gri + "KULLANMA:" + Reset + "" + Mavi + useragents + Reset )

display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
görüntüler . başlangıç ()

br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' , firefox_profile = profil )

zaman . uyku ( 2 )

br . get ( "https://www.instagram.com/" )

zaman . uyku ( 7 )

br . find_element_by_name ( "emailOrPhone" ). send_keys ( str ( telefon ))
br . find_element_by_name ( "tamAd" ). send_keys ( tamadı )

br . find_element_by_name ( "kullanıcı adı" ). send_keys ( 'uname )
br . find_element_by_name ( "şifre" ). send_keys ( şifre )

zaman . uyku ( 2 )

br . find_element_by_css_selector ( "span.Um91Z: nth-child (1)> düğmesi: nth-child (1)" ). tıklayın ()

zaman . uyku ( 7 )

 True iken :
	eğer  id  ==  SMS_AMNT :
		mola
	başka :
		br . find_element_by_link_text ( "Yeni Kod İste" ). tıklayın ()
		iD  =  iD  +  1
		baskı ( Gri + "[" + Mavi + str ( iD ) + Gri + "]" + Yeşil + "SMS gönderildi" )
		zaman . uyku ( zaman aşımı )


br . kapat ()
görüntüler . durdur ()
baskı ( Mavi + "bitmiş" )
sys . çıkış ( 0 )
