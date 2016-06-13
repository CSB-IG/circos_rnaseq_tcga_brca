all: sanos enfermos zoom

zoom: sanos_zoom enfermos_zoom

sanos:
	~/downloads/circos-0.69/bin/circos -conf circos_sanos.conf
enfermos:
	~/downloads/circos-0.69/bin/circos -conf circos_enfermos.conf

sanos_zoom:
	~/downloads/circos-0.69/bin/circos -conf circos_sanos_zoom.conf

enfermos_zoom:
	~/downloads/circos-0.69/bin/circos -conf circos_enfermos_zoom.conf
