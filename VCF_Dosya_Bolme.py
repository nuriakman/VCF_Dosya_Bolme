##############################################################################
# Kaynak Kodlar şu sayfadan alınıp düzenlenmiştir:                           #
#                                                                            #
# https://zedt.eu/tech/linux/split-multi-contact-vcf-file-individual-vcfs/   #
#                                                                            #
# Düzenleyen: nuriakman@gmail.com                                            #
#                                                                            #
# Bu program, .vcf dosyası içindeki kişilerin her birini kişiadi.vcf         #
# adında yeni bir dosyaya aktarır.                                           #
# Oluşturulan yeni dosyalar, cat *.vcf > sonuc.vcf gibi bir komut yardımı    #
# ile bir dosya altında birleştirilebilir                                    #
##############################################################################

import os

Dosya = raw_input('.VCF Dosyasının Adını Yazınız : ')

fopen = open(Dosya, 'r')

KartBaslangici = 'BEGIN:VCARD'
KartBitisi = 'END:VCARD'
i = 0
SATIR = 'ggghtekgqp'
while not SATIR == '':
    if SATIR[0:11] == KartBaslangici:
        print i
        i=i+1
        FileName='%i.vcf'%(i)
        testopen = open(FileName, 'w')
        while not SATIR[0:9] == KartBitisi:
            if SATIR[0:17] == "FN;CHARSET=UTF-8:":
                KisiAdi = SATIR[17:300]
            testopen.write(SATIR)
            SATIR = fopen.readline()
         
        if SATIR[0:9] == KartBitisi:
            testopen.write('END:VCARD')
            testopen.write('\n\n\n')
            testopen.close()

        NewFilName='%s.vcf'%(KisiAdi.strip())

        os.rename(FileName, NewFilName)

    SATIR = fopen.readline()

#EOF