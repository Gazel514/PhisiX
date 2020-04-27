#! / bin / bash

Eğer [ $ ( id-u )  -Ne 0] ;  sonra
	echo  " Yükleyici KÖK olarak çalıştırılmalıdır "
	çıkış 1
fi

Sıfırla
yankı  " "
echo  "                      ################################# "
echo  "                                  -PHISHX- "
echo  "                      ################################# "
echo  "                          [+]: WEEBSEC TARAFINDAN YAPILMIŞ: [+] "
echo  "                      ################################# "
yankı  " "
echo  "                            SADECE bunu KÖK olarak çalıştır "
echo  "                Kuruluma devam etmek için ENTER tuşuna basın "

varos oku

rm -r firefox & > / dev / null
rm -r base & > / dev / null
rm ngrok *  & > / dev / null

mkdir baz

yankı  " "



ARCH = " $ ( kemer ) "
echo  " Kemer Tespit Ediliyor: $ {ARCH} "
yankı  "  "
chmod -R 777 ./
apt-get update -y   & > / dev / null |  echo  " GÜNCELLENİYOR "
apt-get install python3 python3-setuptools python3-pip xvfb gönderen php xterm -y & > / dev / null |  echo  " BAĞIMSIZLIKLARI ÇÖZME "

pip3 kurulum pyvirtualdisplay & > / dev / null |  echo  " PİTON GEREKSİNİMLERİNİN KURULMASI "
pip3 install selenyum & > / dev / null
pip3 install procname & > / dev / null
pip3 yükleme istekleri & > / dev / null

eğer [[ $ {ARCH}  ==  " i686 "  ||  $ {ARCH}  ==  " i686 " ]] ;  sonra
	wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux32.tar.gz & > / dev / null |  echo  " GECKODRIVER KURMA "
Başka
	eğer [[ $ {ARCH}  ==  " i386 "  ||  $ {ARCH}  ==  " i386 " ]] ;  sonra
	        wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux32.tar.gz & > / dev / null |  echo  " GECKODRIVER KURMA "
	Başka
	        wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz & > / dev / null |  echo  " GECKODRIVER KURMA "
	fi
fi


tar xvzf GECKO.tar.gz & > / dev / null |  echo  " ÇEKİCİ GECKODRIVER "
chmod + x geckodriver
mv geckodriver tabanı / |  echo  " GECKODRIVER'I DOĞRU DİREKE HAREKET ETMEK "

eğer [[ $ {ARCH}  ==  " i686 "  ||  $ {ARCH}  ==  " i686 " ]] ;  sonra
        wget -O firefox.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/52.9.0esr/linux-i686/en-US/firefox-52.9.0esr.tar.bz2 & > / dev / null |  echo  " FIREFOX İNDİRME "
Başka
	wget https://ftp.mozilla.org/pub/firefox/releases/52.9.0esr/linux-x86_64/en-US/firefox-52.9.0esr.tar.bz2 -O firefox.tar.bz2 & > / dev / null |  echo  " FIREFOX İNDİRME "
fi


tar xvjf firefox.tar.bz2 & > / dev / null |  echo  " FIREFOX'İN ÇIKARILMASI "
chmod -R 777 firefox /
mv firefox base / & > / dev / null |  echo  " FIREFOX'u DOĞRU DİREKTE HAREKET ETMEK "

eğer [[ $ {ARCH}  ==  " i686 "  ||  $ {ARCH}  ==  " i686 " ]] ;  sonra
	wget -O NGROK.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip & > / dev / null |  echo  " NGROK'U KURMA "
Başka

	eğer [[ $ {ARCH}  ==  " i386 "  ||  $ {ARCH}  ==  " i386 " ]] ;  sonra
	        wget -O NGROK.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-i386.zip & > / dev / null |  echo  " NGROK'U KURMA "
	Başka
	        wget -O NGROK.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip & > / dev / null |  echo  " NGROK'U KURMA "
	fi
fi


unzip NGROK.zip & > / dev / null |  echo  " SİLİNDİR "

rm -r ngrok- *  & > / dev / null |  echo  " TEMİZLİK "
rm * .zip
rm * .tar.gz
rm * .tar.bz2

yankı  "  "
echo  " [YAPILDI] "
