# Time
## date command
```
[tony@stapp01 ~]$ date
Tue Sep 26 15:42:11 UTC 2023
```

## Timezone, timedatectl
```
[tony@stapp01 ~]$ timedatectl
               Local time: Tue 2023-09-26 15:43:10 UTC
           Universal time: Tue 2023-09-26 15:43:10 UTC
                 RTC time: n/a
                Time zone: Etc/UTC (UTC, +0000)
System clock synchronized: yes
              NTP service: n/a
          RTC in local TZ: no
```

## Set timezone, tzselect
```
[tony@stapp01 ~]$ timedatectl
               Local time: Tue 2023-09-26 12:49:13 -03
           Universal time: Tue 2023-09-26 15:49:13 UTC
                 RTC time: n/a
                Time zone: America/Argentina/La_Rioja (-03, -0300)
System clock synchronized: yes
              NTP service: n/a
          RTC in local TZ: no
[tony@stapp01 ~]$ sudo timedatectl set-timezone America/Argentina/La_Rioja
```

```
tzselect
Please identify a location so that time zone rules can be set correctly.
Please select a continent, ocean, "coord", or "TZ".
 1) Africa
 2) Americas
 3) Antarctica
 4) Asia
 5) Atlantic Ocean
 6) Australia
 7) Europe
 8) Indian Ocean
 9) Pacific Ocean
10) coord - I want to use geographical coordinates.
11) TZ - I want to specify the time zone using the Posix TZ format.
#? 2
Please select a country whose clocks agree with yours.
 1) Anguilla              19) Dominican Republic    37) Peru
 2) Antigua & Barbuda     20) Ecuador               38) Puerto Rico
 3) Argentina             21) El Salvador           39) St Barthelemy
 4) Aruba                 22) French Guiana         40) St Kitts & Nevis
 5) Bahamas               23) Greenland             41) St Lucia
 6) Barbados              24) Grenada               42) St Maarten (Dutch)
 7) Belize                25) Guadeloupe            43) St Martin (French)
 8) Bolivia               26) Guatemala             44) St Pierre & Miquelon
 9) Brazil                27) Guyana                45) St Vincent
10) Canada                28) Haiti                 46) Suriname
11) Caribbean NL          29) Honduras              47) Trinidad & Tobago
12) Cayman Islands        30) Jamaica               48) Turks & Caicos Is
13) Chile                 31) Martinique            49) United States
14) Colombia              32) Mexico                50) Uruguay
15) Costa Rica            33) Montserrat            51) Venezuela
16) Cuba                  34) Nicaragua             52) Virgin Islands (UK)
17) Cura?ao               35) Panama                53) Virgin Islands (US)
18) Dominica              36) Paraguay
#? 3
Please select one of the following time zone regions.
 1) Buenos Aires (BA, CF)
 2) Argentina (most areas: CB, CC, CN, ER, FM, MN, SE, SF)
 3) Salta (SA, LP, NQ, RN)
 4) Jujuy (JY)
 5) Tucum?n (TM)
 6) Catamarca (CT); Chubut (CH)
 7) La Rioja (LR)
 8) San Juan (SJ)
 9) Mendoza (MZ)
10) San Luis (SL)
11) Santa Cruz (SC)
12) Tierra del Fuego (TF)
#? 7

The following information has been given:

        Argentina
        La Rioja (LR)

Therefore TZ='America/Argentina/La_Rioja' will be used.
Selected time is now:   Tue Sep 26 12:45:28 -03 2023.
Universal Time is now:  Tue Sep 26 15:45:28 UTC 2023.
Is the above information OK?
1) Yes
2) No
#? yes
Please enter a number in range.
#? 1

You can make this change permanent for yourself by appending the line
        TZ='America/Argentina/La_Rioja'; export TZ
to the file '.profile' in your home directory; then log out and log in again.

Here is that TZ value again, this time on standard output so that you
can use the /usr/bin/tzselect command in shell scripts:
America/Argentina/La_Rioja
```
