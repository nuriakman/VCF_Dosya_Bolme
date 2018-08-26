# VCF_Dosya_Bolme

## Amaç

Akıllı telefonunuzdaki kişileriniz google, icloud ve diğer hesaplarda mükerrer olarak yer alması halinde bu kişilerin tek bir hesap altında toplanması problem olmaktadır. 

Bu programın amacı, farklı hesaplarda kayıtlı aynı kişilerin tek bir liste altında toplanmasını sağlamaktır.


## Nasıl Çalışır?

Bu program ile MCBackup veya benzeri bir kişi kartlarını yedekleme programı ile aldığınız .VCF türündeki dosyanızda kayıtlı kişileriniz alınır.

Her kişi için, o kişi adında bir .VCF dosyası oluşturulur.

Oluşan dosyalarınız ```cat *.vcf > sonuc.VCF``` gibi bir komutla tek bir dosyada birleştirilebilir.


## UYARI

Eğer, aynı kişi adı ile kayıtlı FARKLI kişiler varsa bu program bu kişilerin sadece 1 tanesini alır!

BU nedenle dikkat edilmesi gerekir.


## Teşekkkür

Bu programın özgün hali https://zedt.eu/tech/linux/split-multi-contact-vcf-file-individual-vcfs/ adresinden alınmıştır.


## Lisans

MIT Lisansı ile lisanslanmıştır