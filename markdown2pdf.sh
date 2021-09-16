#!/usr/bin/env bash
# transfer all .md files to pdf files using pandoc and XETEX


#for i in *.md; do
#	echo -e "### $i ###"
#	pandoc "$i"  --standalone --from markdown --pdf-engine=xelatex -o "$i".pdf;
#done

pandoc "$1"  --standalone --from markdown+emoji --pdf-engine=xelatex \
-V geometry:a4paper \
-V colorlinks \
-V urlcolor=NavyBlue \
-V geometry:"top=2.5cm, bottom=1.5cm, left=3cm, right=2cm" \
-V mainfont="Liberation Serif" \
-V sansfont="Liberation Sans" \
--highlight-style tango \
-o "$1".pdf;
