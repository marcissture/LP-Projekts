# LP-Projekts
## Projekta apraksts
Projekta mērķis ir uzlabot studentu laika plānošanu, piedāvājot vienkāršu veidu, kā sekot līdzi darbu termiņiem. Projekta uzdevums ir izveidot programmatūru, kas automātiski iegūst datus no e-studijām un attēlo tos lietotāja saskarnē, kurā dod iespēju aizsūtīt attgādinājumu uz lietātāja ievadītu e-pastu.
## Izmantotās Python bibliotēkas
### Selenium
nepieciešams lai tiktu pie un iegūtu datus no e-studiju vides.
### time
nepieciešams lai ievadītu nepieciešamas pauzes kodā.
### PySimpleGUI
nepieciešams lai tiktu izveidota lietotāja saskarne.
### schedule
nepieciešams lai tiktu izsūtīts atgādinājums nepieciešamajā laikā.
### datetime
nepieciešams lai notiektu, kad ir jaizsūta atgādinājums.
### smtplib, email.mime.text un email.mime.multipart
nepieciešams lai varētu izsūtīt atgādinājumu.
## Izmatotās metodes
Lietotājs ievada savus ortus datus, lai tiktu pie e-studijām. Tālāk lietotājam ir jāievada e-pasts uz kuru tiks nosūtīts atgādinājums par darba termiņa beigām, ja to izvēlēsies. Pēc datu ievades tiek iegūti dati (darba nosaukums, kurss un termiņš) no e-studijas vides un tie tiek attēloti lietotāja saskarnē. Lietotājs pēc izvēles var pieprasīt atgādinājumu, kurš tiks atsūtīts dienu pirms darba nodošanas 12.00.
