all: sanos enfermos

sanos:
	~/downloads/circos-0.69/bin/circos -conf circos_sanos.conf
enfermos:
	~/downloads/circos-0.69/bin/circos -conf circos_enfermos.conf
