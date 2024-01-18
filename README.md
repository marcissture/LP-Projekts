# LP-Projekts
## Projekta apraksts
Projekta mērķis ir uzlabot studentu laika plānošanu, piedāvājot vienkāršu veidu, kā sekot līdzi darbu termiņiem. Projekta uzdevums ir izveidot programmatūru, kas automātiski iegūst datus no e-studijām un attēlo tos lietotāja saskarnē, kurā dod iespēju aizsūtīt attgādinājumu uz lietātāja ievadītu e-pastu.
## Izmantotās Python bibliotēkas
### Selenium
Nepieciešams lai tiktu pie un iegūtu datus no e-studiju vides, izmantojot HTML identifikatorus - ID, NAME, LINK_TEXT un XPATH
### time
Nepieciešams lai ievadītu pauzes kodā, šajā gadījumā tas tiek izmantots, lai pārlūks paspēj ielādēt lapu pirms tālākas koda izpildes.
### PySimpleGUI
Nepieciešams lai tiktu izveidota lietotāja saskarne, kas paātrina un atvieglo gala lietotāja darbību programmā.
### schedule
Nodrošina atgādinājuma izsūtīšanu noteiktā laikā.
### datetime
Nepieciešams lai notiektu, kad ir jaizsūta atgādinājums.
### smtplib, email.mime.text un email.mime.multipart
Nepieciešams lai varētu izsūtīt atgādinājumu. Saderības nolūkiem šajā gadījumā tiek izmantots SMTP protokols nevis kāda noteikta e-pasta pakalpojuma API.
## Izmatotās metodes
Lietotājs ievada savus ortus datus, lai tiktu pie e-studijām. Tālāk lietotājam ir jāievada e-pasts uz kuru tiks nosūtīts atgādinājums par darba termiņa beigām, ja to izvēlēsies. Pēc datu ievades tiek iegūti dati (darba nosaukums, kurss un termiņš) no e-studijas vides un tie tiek attēloti lietotāja saskarnē. Lietotājs pēc izvēles var pieprasīt atgādinājumu, kurš tiks atsūtīts dienu pirms darba nodošanas 12.00. Katrs no šiem soļiem ir definēts kā funkcija, kas tiek attiecīgi izsaukta atkarībā no lietotāja darbībām.
![programmatūras dzīves cikls](https://github.com/marcissture/LP-Projekts/assets/79980809/8cc694e8-311e-4fec-b1fc-b69df62b99fc)
## Secinājumi
izveidotais labāk strādātu ar datubāzi, jo nepatērētu datora resursus un atgādinājuma sistēma varētu strādāt efektīvāk.
