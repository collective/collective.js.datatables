#!/bin/sh

FILE1='collective/js/datatables/resources/media/js/jquery.dataTables.js';
FILE2='collective/js/datatables/resources/media/js/jquery.dataTables.min.js';
VAL1=$(cat $FILE1);
VAL2=$(cat $FILE2);

printf "var orig_define, define; orig_define = define; define = undefined;\n%s\ndefine = orig_define;" "$VAL1" > $FILE1;
printf "var orig_define, define; orig_define = define; define = undefined;\n%s\ndefine = orig_define;" "$VAL2" > $FILE2;
