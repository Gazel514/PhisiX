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



Kimlik  =  0
CALLID  =  0

soyadı  =  rastgele . seçim ([ 'diana' , 'jakal' , 'boreson' , 'sinan' , 'zanyar' , 'lkafe' , 'kenny' , 'parker' , 'faye' , 'spivey' , 'simon' , 'miller' , 'wilson' , 'ryan' , 'jackson' , 'arkadaşlar' , 'tuckler' , 'turner' , 'counety' ,, 'andrews' , 'dunns' , 'barker' , 'reid' ])
cinsiyet  =  rastgele . seçim ([ '1' , '2' ]) # Kadın, Erkek

# --------------------- [tarih için] ----------------------- #

ay  =  rastgele . seçim ([ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '11' ])
gün  =  rastgele . seçim ([ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '24' , '25' ,
yıl  =  rastgele . seçim ([ '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' , '26' , '27' , '28' , '29' ])

# ------------------------------------------------- --------- #


useragents  =  rasgele . seçim ([
	'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (GHTo gibi KHTML) Chrome / 59.0.3071.115 Safari / 537.36' ,
	'Mozilla / 5.0 (Windows NT 6.2; WOW64; rv: 50.0) Gecko / 20100101 Firefox / 50.0' ,
	'Mozilla / 5.0 (Windows NT 6.1) AppleWebKit / 537.36 (KHTML, Gecko gibi) Chrome / 60.0.3112.78 Safari / 537.36 OPR / 47.0.2631.55' ,
	'Mozilla / 5.0 (X11; Heathrow / 1.4; Linux i686; rv: 30) Gecko / 30 Firefox / 30' ,
	'Mozilla / 5.0 (Windows NT 6.1; WOW64; Trident / 7.0; rv: 11.0; MSN 9.0; MSN 9.1; MSN 9.6; MSN 10.0; MSN 10.2; MSN 10.5; MSNbMSNI; MSNmen-us; MSNcIA)'
]) # Facebooks boktan güvenlik atlamak için Rastgele bir kullanıcı seçer ...

şifre  =  rastgele . seçim ([ '75! x # + FmnfW3SK' , 'vL & pM2zVtV6NsEH4' , 'PKC-pK2XmfRG-7B' , 'UME * F4aKD! CV7' , 'eLU_U2 & # MsqT # @ 4 +' , 'xS? mVEy! d2khDsye' , 'L2tb + A97P = # s * WD $' , 'wv & + & sXhrWxw7cJ' , 'S + rD? R = z7? KaS2U' , 'Rj? HcnN7 * -jw = CKw' , 'SQ? 3Vx! J8vueyf2' , ' cunnsjs1736jn # ' , ' lmasdks128973 # !!! @ ' ])
info  =  open ( 'sms_support / phone' , 'r' )
info  =  bilgi . oku ()


telefon  =  bilgi . şerit (). bölünmüş ( ":" , 1 ) [ 0 ]
ad  =  bilgi . şerit (). bölünmüş ( ":" , 1 ) [ 1 ]




SMS_AMNT  =  int ( giriş ( Gri + "[" + Mavi + "SMS" + Gri + "] - [" + Mavi + "10" + Gri + "]" + Yeşil + ":" + Sıfırla ))
CALL_AMNT  =  int ( giriş ( Gri + "[" + Mavi + "ARAMA" + Gri + "] - [" + Mavi + "3" + Gri + "]" + Yeşil + ":" + Sıfırla ))	



profile  =  web sürücüsü . FirefoxProfile ()
profili . set_preference ( "general.useragent.override" , kullanıcı aralıkları )

display  =  Display ( görünür = 0 , boyut = ( 800 , 600 ))
görüntüler . başlangıç ()

br  =  web sürücüsü . Firefox ( firefox_binary = ikili , çalıştırılabilir_yol = 'temel / geckodriver' , firefox_profile = profil )

yazdırmak ( Gri + "KULLANMA:" + Reset + "" + Mavi + useragents + Reset )

br . get ( "https://mbasic.facebook.com/reg/" )
zaman . uyku ( 3 )

br . find_element_by_name ( "ad" ). send_keys ( str ( ad ))
br . find_element_by_name ( "soyadı" ). send_keys ( str ( soyadı ))
br . find_element_by_name ( "reg_email__" ). send_keys ( str ( telefon ))
br . find_elements_by_css_selector ( "girdi [type = 'radyo'] [değer = '" + seks + "']" ) [ 0 ]. tıklayın ()

br . find_element_by_css_selector ( '#month> seçenek: nth-child (' + ay + ')' ). tıklayın ()
br . find_element_by_css_selector ( '#day> seçenek: nth-child (' + gün + ')' ). tıklayın ()
br . find_element_by_css_selector ( '#year> seçenek: nth-child (' + yıl + ')' ). tıklayın ()

br . find_element_by_name ( 'reg_passwd__' ). send_keys ( str ( şifre ))
zaman . uyku ( 2 )
br . find_element_by_name ( 'gönder' ). tıklayın ()
zaman . uyku ( 16 )


 True iken :

	dene :
		br . get ( "https://www.facebook.com/" )
		zaman . uyku ( 11 )
		br . find_element_by_link_text ( " SMS'i almadınız mı?" ). tıklayın ()
		zaman . uyku ( 2 )
		Kimlik  =  Kimlik  +  1

		eğer  Kimlik  >  SMS_AMNT :
			CALLID  =  CALLID  +  1
			eğer  CallID  >  CALL_AMNT :
				mola

			başka :
				br . find_element_by_partial_link_text ( "Ara" ). tıklayın ()
				baskı ( Gri + "[" + Mavi + str ( CALLID ) + Gri + "]" + Kırmızı + "Aranan" )
				zaman . uyku ( 60 )


		başka :
			br . find_element_by_link_text ( "Tekrar SMS Gönder" ). tıklayın ()
			yazdır ( Gri + "[" + Mavi + str ( ID ) + Gri + "]" + Yeşil + "SMS gönderildi" )
			zaman . uyku ( 60 )

	 İstisna hariç :
		br . get ( "https://mbasic.facebook.com/" )
		zaman . uyku ( 11 )
		br . find_element_by_name ( "p_pn" ). send_keys ( str ( telefon ))
		br . find_element_by_id ( "checkpointSubmitButton-actual-button" ). tıklayın ()
		zaman . uyku ( 20 )

		 True iken :
			eğer  Kimlik  >  SMS_AMNT :
				mola
			başka :
				br . find_element_by_name ( "p_rl" ). tıklayın ()
				Kimlik  =  Kimlik  +  1
				yazdır ( Gri + "[" + Mavi + str ( ID ) + Gri + "]" + Yeşil + "SMS gönderildi" )
				zaman . uyku ( 60 )
		mola

br . kapat ()
görüntüler . durdur ()
sys . çıkış ( 0 )
