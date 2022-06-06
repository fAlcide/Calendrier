#! bin/bash

if test -f "File/calendar.ics"; then
    rm -r File/calendar.ics;
fi

echo "Mot de passe UPF et SFTP (==)";

read -s PASSWORD;

python3 scraperHtmlUnit.py $PASSWORD; 

mv *.ics File/calendar.ics;

lftp sftp://u97148976:$PASSWORD@access781503272.webspace-data.io:/Calendar_UPHF/ -e "put File/calendar.ics; bye" || echo "⚠ Fail ⚠" && exit

echo "<<>><<>><<>><<>><<>><<>><<>> Calendrier upload <<>><<>><<>><<>><<>><<>><<>><<>>";